# 💰 Buy or Wait

## AI-Powered Financial Decision Agent

> **Before you buy something, ask: Can I safely afford it?**

Buy or Wait is an AI-powered financial decision assistant that analyzes a user's current balance, purchase amount, upcoming expenses, confirmed income, pending payments, minimum balance requirements, and installment options to determine whether a purchase is financially safe.

Instead of simply asking:

> "Do I have enough money right now?"

Buy or Wait asks:

> "If I make this purchase today, will I still be financially safe after considering everything that is coming up?"

---

## 🌐 Live Demo

🚀 Live Application:

https://buy-or-wait.onrender.com

💻 GitHub Repository:

https://github.com/abhishekam26/buy-or-wait

---

## 🎯 Problem Statement

People often decide whether they can afford a purchase by looking only at their current account balance.

For example:

Current Balance: ₹1,20,000

Laptop Price: ₹80,000

At first glance, the purchase looks affordable.

However, the user may also have upcoming obligations:

- Rent: ₹25,000
- Credit Card Bill: ₹12,000
- Minimum Safe Balance: ₹20,000

After considering these obligations:

₹1,20,000  
- ₹80,000 Laptop  
- ₹25,000 Rent  
- ₹12,000 Credit Card  
= ₹3,000

Required minimum balance = ₹20,000

Therefore, the purchase is not financially safe.

This is the problem that Buy or Wait solves.

---

## 💡 Our Solution

Buy or Wait combines AI-powered natural language understanding with a deterministic financial affordability engine.

The system considers:

- Current account balance
- Purchase amount
- Upcoming rent and bills
- Credit card payments
- Essential expenses
- Confirmed future income
- EMI and installment options
- Minimum balance requirement
- User payment preferences

It then provides a clear recommendation:

**BUY NOW**

**OR**

**BUY WITH PAYMENT PLAN**

**OR**

**WAIT**

---

## ✨ Key Features

### 🤖 Natural Language Financial Input

Users do not need to fill complicated financial forms.

They can simply describe their financial situation in natural language.

Example:

Na account lo 120000 undi. 80000 laptop konali. September 15th rent 25000 pay cheyyali. September 18th credit card 12000 pay cheyyali. September 30th salary 70000 vastundi.

The AI extracts the relevant financial information automatically.

### 💰 Cash-Flow Based Affordability

The system does not look only at the current balance.

It creates a future cash-flow timeline containing:

- Income
- Expenses
- Bills
- Rent
- Credit card payments
- Installments

This allows the system to evaluate the user's financial position over time.

### 🛡️ Minimum Balance Protection

The system protects a configurable minimum balance.

Example:

Minimum Safe Balance = ₹20,000

A purchase is considered unsafe if the projected balance falls below this threshold.

### 💼 Future Income Awareness

Confirmed future income is included in the financial forecast.

Current Balance  
↓  
Upcoming Expenses  
↓  
Confirmed Salary  
↓  
EMI Payments  
↓  
Projected Balance

This helps determine whether waiting for future income could make a purchase safer.

### 💳 EMI / Installment Evaluation

If paying the full amount immediately is unsafe, the system can evaluate installment options.

Example:

Laptop Price: ₹80,000

4 Month EMI:

₹20,000  
₹20,000  
₹20,000  
₹20,000

The affordability engine checks whether the installment plan can be completed while protecting the minimum balance.

---

# 🏗️ System Architecture

```text
┌──────────────────────────────────────────────┐
│                    USER                      │
│                                              │
│  "Na account lo 120000 undi.                 │
│   80000 laptop konali..."                    │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│               WEB FRONTEND                   │
│                                              │
│            HTML + CSS + JavaScript           │
│                                              │
│       User enters financial information      │
└──────────────────────┬───────────────────────┘
                       │
                       │ HTTP POST
                       ▼
┌──────────────────────────────────────────────┐
│                 FASTAPI                      │
│                                              │
│              /ai/decision                    │
│              /ai/parse                       │
│              /check                          │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│                 AI PARSER                    │
│                                              │
│                OpenAI API                    │
│                                              │
│ Natural Language → Financial Information     │
│                                              │
│ • Current Balance                            │
│ • Purchase Amount                            │
│ • Expenses                                   │
│ • Income                                     │
│ • Financial Events                           │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│           AFFORDABILITY ENGINE               │
│                                              │
│ • Cash Flow Timeline                         │
│ • Future Income                              │
│ • Upcoming Expenses                          │
│ • Essential Payments                         │
│ • Minimum Balance Protection                 │
│ • EMI / Installment Evaluation               │
│ • Payment Preferences                        │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│              DECISION LAYER                  │
│                                              │
│        ┌─────────────────────┐               │
│        │   AFFORDABLE_NOW    │               │
│        └─────────────────────┘               │
│                                              │
│        ┌─────────────────────┐               │
│        │ AFFORDABLE_WITH_PLAN│               │
│        └─────────────────────┘               │
│                                              │
│        ┌─────────────────────┐               │
│        │   NOT_AFFORDABLE    │               │
│        └─────────────────────┘               │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│                  WEB UI                      │
│                                              │
│ • Recommended Payment Method                 │
│ • Payment Plan                               │
│ • Decision Explanation                       │
│ • Earliest Full Payment Date                 │
│ • Spending Changes                           │
└──────────────────────────────────────────────┘


🔄 Application Flow

User
  ↓
Natural Language Input
  ↓
Web Frontend
  ↓
FastAPI Backend
  ↓
OpenAI Financial Parser
  ↓
Structured Financial Data
  ↓
Cash-Flow Timeline
  ↓
Affordability Engine
  ↓
Minimum Balance Check
  ↓
Payment Plan Evaluation
  ↓
Final Decision
  ↓
Web UI

☁️ Deployment Architecture
┌─────────────────────┐
│       GitHub        │
│                     │
│    Source Code      │
└──────────┬──────────┘
           │
           │ Auto Deploy
           ▼
┌─────────────────────┐
│       Render        │
│                     │
│    Cloud Hosting    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      FastAPI        │
│     Web Server      │
└──────────┬──────────┘
           │
           ├──────────────────┐
           │                  │
           ▼                  ▼
┌─────────────────┐   ┌─────────────────┐
│   OpenAI API    │   │   Web Browser   │
│                 │   │                 │
│ AI Extraction   │   │     User UI     │
└─────────────────┘   └─────────────────┘


📊 Example

User Input

Na account lo 120000 undi. 80000 laptop konali. September 15th rent 25000 pay cheyyali. September 18th credit card 12000 pay cheyyali. September 30th salary 70000 vastundi.

Extracted Information

Current Balance: ₹1,20,000

Purchase:

Laptop - ₹80,000

Upcoming Expenses:

Rent - ₹25,000
Credit Card - ₹12,000

Confirmed Income:

Salary - ₹70,000

Full Payment Analysis

Starting Balance = ₹1,20,000

Laptop = -₹80,000

Rent = -₹25,000

Credit Card = -₹12,000

Projected Balance = ₹3,000

Minimum Required Balance = ₹20,000

Therefore:

Full payment is NOT financially safe.

The system can then evaluate an available EMI plan.

💳 Payment Plan Example

Purchase Amount: ₹80,000

4 Month EMI:

September 30 → ₹20,000
October 30 → ₹20,000
November 30 → ₹20,000
December 30 → ₹20,000

The engine checks every payment against the future cash-flow timeline.

The goal is to complete the purchase without violating the minimum balance requirement.


🔌 API Endpoints

POST /ai/decision

Main AI-powered financial decision endpoint.

Example request:

{
  "message": "Na account lo 120000 undi. 80000 laptop konali.",
  "payment_options": []
}

The response contains:

Extracted financial data
Affordability status
Recommended payment method
Payment plan
Earliest full-payment date
Spending changes
Decision explanation
POST /ai/parse

Extracts structured financial information from natural language.

Example request:

{
  "message": "Na account lo 120000 undi. 80000 laptop konali."
}
POST /check

Runs the core affordability engine using structured financial information.

It evaluates:

Current balance
Purchase amount
Future events
Recurring expenses
Pending payments
Payment options
User preferences

📁 Project Structure
buy-or-wait/
│
├── main.py
├── ai_parser.py
├── index.html
├── style.css
├── script.js
├── requirements.txt
├── .gitignore
└── README.md

▶️ Run Locally

1. Clone the repository
git clone https://github.com/abhishekam26/buy-or-wait.git
2. Enter the project
cd buy-or-wait
3. Create a virtual environment
python -m venv venv
4. Activate the environment

Windows:

venv\Scripts\activate
5. Install dependencies
pip install -r requirements.txt
6. Configure the OpenAI API key

Create a .env file:

OPENAI_API_KEY=your_api_key_here

Never commit your API key to GitHub.

7. Start the application
uvicorn main:app --reload
8. Open the application

http://127.0.0.1:8000

🚀 Deployment

The application is deployed on Render.

Deployment flow:

GitHub Repository
       ↓
Render
       ↓
Install Dependencies
       ↓
Start FastAPI
       ↓
Live Application
Build Command
pip install -r requirements.txt
Start Command
uvicorn main:app --host 0.0.0.0 --port $PORT

Live Application

https://buy-or-wait.onrender.com

⭐ Support

If you find this project interesting, consider giving the GitHub repository a ⭐.

Thank you for checking out Buy or Wait! 🚀
