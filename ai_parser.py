from fastapi import APIRouter
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

router = APIRouter()


class NaturalLanguageRequest(BaseModel):
    message: str


def extract_financial_data(message: str):

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=[
            {
                "role": "system",
                "content": """
You are a financial information extraction assistant.

Read the user's message and extract financial information.

Return ONLY valid JSON.

Use this exact structure:

{
  "current_balance": number or null,
  "purchase_amount": number or null,
  "item": string or null,
  "events": [
    {
      "date": "YYYY-MM-DD",
      "amount": number,
      "description": string,
      "type": "CONFIRMED_INCOME" or "EXPENSE",
      "essential": true or false
    }
  ]
}

Rules:

1. current_balance means the user's current available money.
2. purchase_amount means the amount of the item they want to buy.
3. item means the item being purchased.
4. Salary or confirmed income must have a POSITIVE amount and essential must be true.
5. Expenses and bills must have a NEGATIVE amount.
6. Rent, insurance, loan payments and credit card bills are essential.
7. Shopping, entertainment and subscriptions are normally non-essential unless the user says they are essential.
8. Convert dates to YYYY-MM-DD.
9. Today's date is 2026-09-12. If the year is not mentioned, use 2026.
10. If information is missing, use null or an empty list.
11. Do not calculate affordability.
12. Do not give financial advice.
13. Return ONLY JSON.
"""
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )

    return response.output_text


@router.post("/parse")
def parse_message(request: NaturalLanguageRequest):

    extracted_data = extract_financial_data(request.message)

    return {
        "message_received": request.message,
        "extracted_data": extracted_data
    }