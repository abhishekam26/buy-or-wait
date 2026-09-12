async function checkDecision() {

    const message = document.getElementById("message").value;

    if (!message.trim()) {
        alert("Please enter your financial information.");
        return;
    }

    const loading = document.getElementById("loading");
    const resultBox = document.getElementById("result");

    loading.style.display = "block";
    resultBox.style.display = "none";

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/ai/decision",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    message: message,
                    payment_options: [
                        {
                            name: "4 Month EMI",
                            first_payment: 20000,
                            installment_amount: 20000,
                            number_of_installments: 4,
                            first_payment_date: "2026-09-30"
                        }
                    ]
                })
            }
        );

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Something went wrong");
        }

        const decision = data.affordability_result;

        const statusElement = document.getElementById("status");

statusElement.textContent = decision.affordability_status;

if (decision.affordability_status === "AFFORDABLE_NOW") {
    statusElement.style.background = "#ecfdf3";
    statusElement.style.color = "#087443";
    statusElement.style.borderColor = "#b7ebcd";
}
else if (decision.affordability_status === "AFFORDABLE_WITH_PLAN") {
    statusElement.style.background = "#fffaeb";
    statusElement.style.color = "#b54708";
    statusElement.style.borderColor = "#fedf89";
}
else if (decision.affordability_status === "NOT_AFFORDABLE") {
    statusElement.style.background = "#fef3f2";
    statusElement.style.color = "#b42318";
    statusElement.style.borderColor = "#fecdca";
}

        document.getElementById("paymentMethod").textContent =
            decision.recommended_payment_method;

        document.getElementById("explanation").textContent =
            decision.decision_explanation;

        const paymentPlan = document.getElementById("paymentPlan");

        paymentPlan.innerHTML = "";

        decision.payment_plan.forEach(payment => {

            const div = document.createElement("div");

            div.className = "payment-item";

            div.textContent =
                `${payment.date} → ₹${Math.abs(payment.amount)} → ${payment.description}`;

            paymentPlan.appendChild(div);
        });

        resultBox.style.display = "block";

    } catch (error) {

        alert("Error: " + error.message);

    } finally {

        loading.style.display = "none";
    }
}