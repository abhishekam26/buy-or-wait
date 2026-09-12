from ai_parser import router, extract_financial_data
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from datetime import date
import calendar
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/ai")


# -----------------------------
# FINANCIAL EVENT
# -----------------------------

class FinancialEvent(BaseModel):
    date: str
    amount: float
    description: str
    type: str
    essential: bool = False


# -----------------------------
# RECURRING EXPENSE
# -----------------------------

class RecurringExpense(BaseModel):
    name: str
    amount: float
    next_due_date: str
    frequency: str = "MONTHLY"
    essential: bool = True


# -----------------------------
# PENDING PAYMENT
# -----------------------------

class PendingPayment(BaseModel):
    name: str
    amount: float
    due_date: str
    essential: bool = True


# -----------------------------
# PAYMENT OPTION
# -----------------------------

class PaymentOption(BaseModel):
    name: str
    first_payment: float
    installment_amount: float = 0
    number_of_installments: int = 1
    first_payment_date: str


# -----------------------------
# USER PREFERENCES
# -----------------------------

class UserPreferences(BaseModel):
    preferred_payment_method: str = "ANY"
    max_installments: int = 4
    avoid_debt: bool = True
    allow_discretionary_cuts: bool = True


# -----------------------------
# MAIN REQUEST
# -----------------------------

class AffordabilityRequest(BaseModel):

    current_balance: float
    purchase_amount: float
    minimum_balance: float

    events: list[FinancialEvent] = Field(
        default_factory=list
    )

    recurring_expenses: list[RecurringExpense] = Field(
        default_factory=list
    )

    pending_payments: list[PendingPayment] = Field(
        default_factory=list
    )

    payment_options: list[PaymentOption] = Field(
        default_factory=list
    )

    user_preferences: UserPreferences = Field(
        default_factory=UserPreferences
    )


# -----------------------------
# HOME
# -----------------------------

@app.get("/")
def home():
    return {
        "message": "Buy or Wait AI Agent is running!"
    }


# -----------------------------
# ADD MONTHS
# -----------------------------

def add_months(original_date, months):

    month = original_date.month + months
    year = original_date.year

    while month > 12:
        month -= 12
        year += 1

    day = min(
        original_date.day,
        calendar.monthrange(year, month)[1]
    )

    return date(year, month, day)


# -----------------------------
# BUILD FUTURE EVENTS
# -----------------------------

def build_future_events(request):

    today = date.today()

    events = []

    # Normal events
    for event in request.events:

        event_date = date.fromisoformat(event.date)

        if event_date >= today:

            events.append({
                "date": event_date,
                "amount": event.amount,
                "description": event.description,
                "type": event.type,
                "essential": event.essential
            })

    # Pending payments
    for payment in request.pending_payments:

        payment_date = date.fromisoformat(
            payment.due_date
        )

        if payment_date >= today:

            events.append({
                "date": payment_date,
                "amount": -payment.amount,
                "description":
                    "Pending: " + payment.name,
                "type": "PENDING_PAYMENT",
                "essential":
                    payment.essential
            })

    # Recurring expenses
    for expense in request.recurring_expenses:

        start_date = date.fromisoformat(
            expense.next_due_date
        )

        for i in range(6):

            if expense.frequency == "MONTHLY":

                occurrence = add_months(
                    start_date,
                    i
                )

            else:

                occurrence = start_date

            if occurrence >= today:

                events.append({
                    "date": occurrence,
                    "amount": -expense.amount,
                    "description":
                        "Recurring: " + expense.name,
                    "type":
                        "RECURRING_EXPENSE",
                    "essential":
                        expense.essential
                })

    events.sort(
        key=lambda x: x["date"]
    )

    return events


# -----------------------------
# BUILD COMPLETE TIMELINE
# -----------------------------

def build_timeline(
    request,
    payment_option=None
):

    events = build_future_events(request)

    if payment_option:

        first_date = date.fromisoformat(
            payment_option.first_payment_date
        )

        for i in range(
            payment_option.number_of_installments
        ):

            payment_date = add_months(
                first_date,
                i
            )

            if i == 0:

                amount = (
                    payment_option.first_payment
                )

                description = (
                    payment_option.name
                )

            else:

                amount = (
                    payment_option.installment_amount
                )

                description = (
                    f"{payment_option.name} "
                    f"installment {i + 1}"
                )

            if payment_date >= date.today():

                events.append({
                    "date": payment_date,
                    "amount": -amount,
                    "description": description,
                    "type": "PURCHASE_PAYMENT",
                    "essential": False
                })

    events.sort(
        key=lambda x: x["date"]
    )

    return events


# -----------------------------
# EVALUATE PAYMENT OPTION
# -----------------------------

def evaluate_payment_option(
    request,
    option
):

    balance = request.current_balance

    timeline = build_timeline(
        request,
        option
    )

    lowest_balance = balance
    lowest_date = None

    for event in timeline:

        balance += event["amount"]

        if balance < lowest_balance:

            lowest_balance = balance
            lowest_date = event["date"]

        if balance < request.minimum_balance:

            return {
                "safe": False,
                "lowest_balance":
                    lowest_balance,
                "lowest_balance_date":
                    str(lowest_date)
                    if lowest_date
                    else None,
                "timeline": timeline
            }

    return {
        "safe": True,
        "lowest_balance":
            lowest_balance,
        "lowest_balance_date":
            str(lowest_date)
            if lowest_date
            else None,
        "timeline": timeline
    }


# -----------------------------
# SPENDING CHANGES
# -----------------------------

def calculate_spending_changes(request):

    discretionary_total = 0

    for event in request.events:

        if (
            event.amount < 0
            and not event.essential
        ):

            discretionary_total += abs(
                event.amount
            )

    if discretionary_total == 0:

        return {
            "needed": False,
            "amount": 0,
            "message":
                "No discretionary spending cuts identified."
        }

    safe_today = (
        request.current_balance
        - request.minimum_balance
    )

    required = max(
        0,
        request.purchase_amount - safe_today
    )

    cut = min(
        discretionary_total,
        required
    )

    if cut <= 0:

        return {
            "needed": False,
            "amount": 0,
            "message":
                "No spending reduction is currently required."
        }

    if not request.user_preferences.allow_discretionary_cuts:

        return {
            "needed": False,
            "amount": 0,
            "message":
                "User does not allow discretionary spending cuts."
        }

    return {
        "needed": True,
        "amount": cut,
        "message":
            f"Reduce discretionary spending by ₹{cut:.2f}."
    }


# -----------------------------
# MAIN CHECK
# -----------------------------

@app.post("/check")
def check_affordability(request):

    today = date.today()

    safe_today = max(
        0,
        request.current_balance
        - request.minimum_balance
    )

    preferences = request.user_preferences

    # --------------------------------
    # FULL PAYMENT
    # --------------------------------

    full_payment = PaymentOption(

        name="Pay full amount today",

        first_payment=
            request.purchase_amount,

        installment_amount=0,

        number_of_installments=1,

        first_payment_date=
            str(today)
    )

    full_result = evaluate_payment_option(
        request,
        full_payment
    )

    # User prefers full payment
    if (
        full_result["safe"]
        and preferences.preferred_payment_method
        == "PAY_IN_FULL"
    ):

        return {
            "amount_safe_to_pay": safe_today,

            "affordability_status":
                "AFFORDABLE_NOW",

            "recommended_payment_method":
                "PAY_IN_FULL",

            "payment_plan": [
                {
                    "date": str(today),
                    "amount":
                        request.purchase_amount
                }
            ],

            "earliest_date_for_full_payment":
                str(today),

            "spending_changes_needed":
                calculate_spending_changes(request),

            "decision_explanation":
                "Full payment is safe and matches your preference."
        }

    # --------------------------------
    # FULL PAYMENT SAFE
    # --------------------------------

    if (
        full_result["safe"]
        and preferences.preferred_payment_method
        == "ANY"
    ):

        return {
            "amount_safe_to_pay": safe_today,

            "affordability_status":
                "AFFORDABLE_NOW",

            "recommended_payment_method":
                "PAY_IN_FULL",

            "payment_plan": [
                {
                    "date": str(today),
                    "amount":
                        request.purchase_amount
                }
            ],

            "earliest_date_for_full_payment":
                str(today),

            "spending_changes_needed":
                calculate_spending_changes(request),

            "decision_explanation":
                "You can safely pay the full amount today."
        }

    # --------------------------------
    # INSTALLMENTS
    # --------------------------------

    safe_options = []

    for option in request.payment_options:

        if (
            option.number_of_installments
            > preferences.max_installments
        ):
            continue

        if preferences.avoid_debt:
            continue

        result = evaluate_payment_option(
            request,
            option
        )

        if result["safe"]:

            safe_options.append({
                "name": option.name,
                "payment_plan":
                    result["timeline"],
                "lowest_balance":
                    result["lowest_balance"]
            })

    # --------------------------------
    # SAFE INSTALLMENT
    # --------------------------------

    if safe_options:

        best = safe_options[0]

        return {

            "amount_safe_to_pay":
                safe_today,

            "affordability_status":
                "AFFORDABLE_WITH_PLAN",

            "recommended_payment_method":
                best["name"],

            "payment_plan":
                best["payment_plan"],

            "earliest_date_for_full_payment":
                str(
                    best["payment_plan"][-1]["date"]
                ),

            "spending_changes_needed":
                calculate_spending_changes(request),

            "decision_explanation":
                (
                    f"{best['name']} is affordable "
                    "while protecting your minimum balance."
                )
        }

    # --------------------------------
    # NOT AFFORDABLE
    # --------------------------------

    return {

        "amount_safe_to_pay":
            safe_today,

        "affordability_status":
            "NOT_AFFORDABLE",

        "recommended_payment_method":
            "WAIT_OR_DO_NOT_PROCEED",

        "payment_plan": [],

        "earliest_date_for_full_payment":
            None,

        "spending_changes_needed":
            calculate_spending_changes(request),

        "decision_explanation":
            (
                "The purchase is not safely affordable "
                "with the current cash-flow forecast."
            )
    }

# -----------------------------
# AI DECISION
# -----------------------------

class AIDecisionRequest(BaseModel):
    message: str
    payment_options: list[PaymentOption] = []


@app.post("/ai/decision")
def ai_decision(request: AIDecisionRequest):

    extracted_text = extract_financial_data(request.message)
    extracted = json.loads(extracted_text)

    current_balance = extracted.get("current_balance")
    purchase_amount = extracted.get("purchase_amount")

    if current_balance is None:
        return {
            "status": "ERROR",
            "message": "Current balance could not be identified.",
            "extracted_data": extracted
        }

    if purchase_amount is None:
        return {
            "status": "ERROR",
            "message": "Purchase amount could not be identified.",
            "extracted_data": extracted
        }

    events = []

    for event in extracted.get("events", []):
        events.append(
            FinancialEvent(
                date=event["date"],
                amount=event["amount"],
                description=event["description"],
                type=event["type"],
                essential=event["essential"]
            )
        )

    affordability_request = AffordabilityRequest(
        current_balance=current_balance,
        purchase_amount=purchase_amount,
        minimum_balance=20000,
        events=events,
        payment_options=request.payment_options,
        user_preferences=UserPreferences(
            preferred_payment_method="INSTALLMENTS",
            max_installments=4,
            avoid_debt=False,
            allow_discretionary_cuts=True
        )
    )

    result = check_affordability(affordability_request)

    return {
        "user_message": request.message,
        "extracted_data": extracted,
        "affordability_result": result
    }