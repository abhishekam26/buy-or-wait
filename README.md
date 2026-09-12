\# 💰 Buy or Wait



\### AI-Powered Financial Decision Agent



> \*\*Before you buy something, ask: Can I safely afford it?\*\*



Buy or Wait is an AI-powered financial decision assistant that analyzes a user's \*\*current balance, upcoming expenses, confirmed income, pending payments, minimum balance requirements, and installment options\*\* to determine whether a purchase is financially safe.



Instead of simply checking:



> "Do I have enough money right now?"



Buy or Wait asks:



> \*\*"If I make this purchase today, will I still be financially safe after considering everything that is coming up?"\*\*



\---



\## 🌐 Live Demo



🚀 \*\*Try Buy or Wait:\*\*  

https://buy-or-wait.onrender.com



\---



\# 🎯 Problem



Traditional budgeting tools often focus on the current account balance.



For example:



```text

Current Balance: ₹1,20,000

Laptop: ₹80,000



Available Balance:

₹1,20,000 - ₹80,000 = ₹40,000



Looks affordable.



But what if the user also has:



Rent              ₹25,000

Credit Card       ₹12,000

Minimum Balance   ₹20,000



Now the real financial situation becomes:



₹1,20,000

&#x20;  ↓

\- ₹80,000 Laptop

&#x20;  ↓

\- ₹25,000 Rent

&#x20;  ↓

\- ₹12,000 Credit Card

&#x20;  ↓

= ₹3,000



Minimum required = ₹20,000



❌ Purchase is NOT financially safe.



This is the problem Buy or Wait is designed to solve.



💡 Solution



Buy or Wait combines:



🤖 AI-powered financial information extraction

💰 Current account balance

🧾 Upcoming bills

🏠 Rent and essential expenses

💳 Credit card payments

💼 Confirmed future income

📅 Cash-flow timeline

💵 Minimum balance protection

📆 EMI / installment options

🧠 User payment preferences



The system evaluates the complete financial timeline before making a recommendation.



🧠 How It Works

&#x20;               USER MESSAGE

&#x20;                    │

&#x20;                    ▼

&#x20;         ┌─────────────────────┐

&#x20;         │   AI Information    │

&#x20;         │     Extraction      │

&#x20;         └──────────┬──────────┘

&#x20;                    │

&#x20;                    ▼

&#x20;         Financial Information

&#x20;                    │

&#x20;         ┌──────────┴──────────┐

&#x20;         │                     │

&#x20;         ▼                     ▼

&#x20;   Current Balance       Future Events

&#x20;                             │

&#x20;                   ┌─────────┴─────────┐

&#x20;                   │                   │

&#x20;                   ▼                   ▼

&#x20;               Expenses             Income

&#x20;                   │                   │

&#x20;                   └─────────┬─────────┘

&#x20;                             │

&#x20;                             ▼

&#x20;                  Cash Flow Timeline

&#x20;                             │

&#x20;                             ▼

&#x20;                Affordability Engine

&#x20;                             │

&#x20;                   ┌─────────┴─────────┐

&#x20;                   │                   │

&#x20;                   ▼                   ▼

&#x20;              Full Payment          EMI Plan

&#x20;                   │                   │

&#x20;                   └─────────┬─────────┘

&#x20;                             │

&#x20;                             ▼

&#x20;                   BUY OR WAIT DECISION

&#x20;                             │

&#x20;                             ▼

&#x20;                        WEB UI

✨ Key Features

🤖 Natural Language Input



Users don't need to fill complicated financial forms.



They can simply type:



Na account lo 120000 undi.

80000 laptop konali.

September 15th rent 25000 pay cheyyali.

September 18th credit card 12000 pay cheyyali.

September 30th salary 70000 vastundi.



The AI extracts the important financial information automatically.



💰 Cash-Flow Based Affordability



The system doesn't look only at the current balance.



It considers future:



Expenses

Bills

Rent

Credit card payments

Confirmed income

Installments



This creates a future financial timeline.



🛡️ Minimum Balance Protection



Users can define a minimum amount that should remain available.



Example:



Minimum Safe Balance = ₹20,000



The system avoids recommending a purchase if the projected balance falls below this threshold.



📅 Future Income Awareness



Confirmed future income is included in the financial forecast.



Example:



Current Balance

&#x20;     ↓

Upcoming Expenses

&#x20;     ↓

Future Salary

&#x20;     ↓

EMI Payments

&#x20;     ↓

Projected Balance



This allows the system to determine whether waiting for future income could make a purchase safer.



💳 EMI / Installment Evaluation



If paying the full amount is unsafe, Buy or Wait can evaluate installment options.



Example:



Laptop Price: ₹80,000



4 Month EMI:



₹20,000

₹20,000

₹20,000

₹20,000



The affordability engine checks whether the installment plan can be completed while protecting the minimum balance.



🧠 Decision Engine



The system produces clear decisions instead of overwhelming users with raw calculations.



Possible outcomes:



🟢 AFFORDABLE\_NOW



The purchase can be made safely now.



🟡 AFFORDABLE\_WITH\_PLAN



Full payment may not be ideal, but an installment plan can work safely.



🔴 NOT\_AFFORDABLE



The purchase would violate the user's financial safety constraints.



📊 Example

User Input

Na account lo 120000 undi.

80000 laptop konali.



September 15th rent 25000 pay cheyyali.



September 18th credit card 12000 pay cheyyali.



September 30th salary 70000 vastundi.

AI Extracts

Current Balance

₹1,20,000



Purchase

₹80,000 Laptop



Upcoming Expenses

₹25,000 Rent

₹12,000 Credit Card



Future Income

₹70,000 Salary

Full Payment Analysis

Starting Balance      ₹1,20,000

Laptop                -₹80,000

Rent                  -₹25,000

Credit Card           -₹12,000

\--------------------------------

Projected Balance      ₹3,000



Minimum safe balance:



₹20,000



Therefore:



❌ Full payment is not safe.

EMI Analysis

4 Month EMI



₹20,000 × 4 months



If the timeline remains above the required minimum balance:



🟡 AFFORDABLE\_WITH\_PLAN



The system recommends the installment plan instead of immediate full payment.



🔐 Financial Safety Logic



Buy or Wait considers a purchase safe only when the financial forecast satisfies the configured constraints.



Conceptually:



Projected Balance

&#x20;       ≥

Minimum Required Balance



for the relevant payment timeline.



The system also considers:



Existing obligations

Essential expenses

Confirmed income

Installment commitments

Maximum allowed installments

Payment preferences



This makes the decision cash-flow aware rather than balance-only.



🏗️ System Architecture

┌───────────────────────────────┐

│           Web UI              │

│       HTML / CSS / JS         │

└───────────────┬───────────────┘

&#x20;               │

&#x20;               │ HTTP POST

&#x20;               ▼

┌───────────────────────────────┐

│          FastAPI              │

│                               │

│   /ai/decision                │

│   /ai/parse                   │

│   /check                      │

└───────────────┬───────────────┘

&#x20;               │

&#x20;               ▼

┌───────────────────────────────┐

│      AI Financial Parser      │

│                               │

│       OpenAI API              │

└───────────────┬───────────────┘

&#x20;               │

&#x20;               ▼

┌───────────────────────────────┐

│     Affordability Engine      │

│                               │

│ • Cash Flow Timeline          │

│ • Expense Analysis            │

│ • Income Analysis             │

│ • Minimum Balance Protection  │

│ • EMI Evaluation              │

└───────────────┬───────────────┘

&#x20;               │

&#x20;               ▼

┌───────────────────────────────┐

│       Decision Response       │

│                               │

│ AFFORDABLE\_NOW                │

│ AFFORDABLE\_WITH\_PLAN          │

│ NOT\_AFFORDABLE                │

└───────────────────────────────┘

🔄 Decision Flow

User enters financial information

&#x20;             ↓

AI extracts financial data

&#x20;             ↓

Validate required information

&#x20;             ↓

Build future cash-flow timeline

&#x20;             ↓

Evaluate full payment

&#x20;             ↓

Is minimum balance protected?

&#x20;       ┌─────┴─────┐

&#x20;      YES          NO

&#x20;       │            │

&#x20;       ▼            ▼

AFFORDABLE\_NOW   Check EMI Options

&#x20;                    │

&#x20;                    ▼

&#x20;             Is EMI affordable?

&#x20;               ┌────┴────┐

&#x20;              YES        NO

&#x20;               │          │

&#x20;               ▼          ▼

&#x20;       AFFORDABLE\_     NOT\_

&#x20;       WITH\_PLAN      AFFORDABLE

🛠️ Tech Stack

Technology	Purpose

🐍 Python	Backend development

⚡ FastAPI	REST API

🤖 OpenAI API	Natural language financial extraction

🌐 HTML	Frontend structure

🎨 CSS	UI styling

⚙️ JavaScript	Frontend logic and API communication

🚀 Render	Cloud deployment

🐙 GitHub	Source code and version control

📁 Project Structure

buy-or-wait/

│

├── main.py

│       └── FastAPI application

│

├── ai\_parser.py

│       └── AI financial information extraction

│

├── index.html

│       └── Web interface

│

├── style.css

│       └── Fintech UI styling

│

├── script.js

│       └── Frontend API integration

│

├── requirements.txt

│       └── Python dependencies

│

├── .gitignore

│       └── Prevents secrets and virtual environment from Git

│

└── README.md

&#x20;       └── Project documentation

🔌 API Endpoints

POST /ai/decision



Main AI-powered decision endpoint.



Request

{

&#x20; "message": "Na account lo 120000 undi. 80000 laptop konali.",

&#x20; "payment\_options": \[]

}

Response



The API returns:



{

&#x20; "user\_message": "...",

&#x20; "extracted\_data": {},

&#x20; "affordability\_result": {}

}



The affordability result includes important decision information such as:



amount\_safe\_to\_pay

affordability\_status

recommended\_payment\_method

payment\_plan

earliest\_date\_for\_full\_payment

spending\_changes\_needed

decision\_explanation

POST /ai/parse



Extracts financial information from natural language.



Example:



{

&#x20; "message": "Na account lo 120000 undi. 80000 laptop konali."

}



The AI converts the natural language into structured financial data.



POST /check



Runs the core affordability engine using structured financial information.



This endpoint evaluates:



Current balance

Purchase amount

Future events

Recurring expenses

Pending payments

Payment options

User preferences

▶️ Run Locally

1\. Clone the repository

git clone https://github.com/abhishekam26/buy-or-wait.git



Move into the project:



cd buy-or-wait

2\. Create Virtual Environment

python -m venv venv



Activate it on Windows:



venv\\Scripts\\activate

3\. Install Dependencies

pip install -r requirements.txt

4\. Configure Environment Variables



Create a .env file:



OPENAI\_API\_KEY=your\_api\_key\_here



Never commit your API key to GitHub.



5\. Start the Application

uvicorn main:app --reload

6\. Open the Application

http://127.0.0.1:8000

🚀 Deployment



The application is deployed using Render.



Deployment flow:



Developer

&#x20;   │

&#x20;   ▼

GitHub Repository

&#x20;   │

&#x20;   ▼

Render

&#x20;   │

&#x20;   ├── Install dependencies

&#x20;   │

&#x20;   ├── Start FastAPI

&#x20;   │

&#x20;   └── Deploy application

&#x20;            │

&#x20;            ▼

&#x20;       Live Web App

Build Command

pip install -r requirements.txt

Start Command

uvicorn main:app --host 0.0.0.0 --port $PORT

🔒 Security



Security considerations implemented in the project:



API keys are stored using environment variables.

.env is excluded using .gitignore.

Secrets are not hard-coded into source code.

The OpenAI API key is not exposed to the frontend.

Only required frontend files are served by the FastAPI application.



Example .gitignore:



.env

venv/

\_\_pycache\_\_/

🧪 Example Test Scenarios

Scenario 1 — Buy Now

Na account lo 150000 undi.

50000 laptop konali.



Expected:



AFFORDABLE\_NOW

Scenario 2 — Buy With EMI

Na account lo 120000 undi.

80000 laptop konali.



September 15th rent 25000 pay cheyyali.

September 18th credit card 12000 pay cheyyali.

September 30th salary 70000 vastundi.



With a suitable EMI option:



AFFORDABLE\_WITH\_PLAN

Scenario 3 — Wait

Na account lo 50000 undi.

80000 phone konali.



September 15th rent 25000 pay cheyyali.



Expected:



NOT\_AFFORDABLE

🌟 Why Buy or Wait?



Most purchase decisions are based on:



"Do I have enough money right now?"



Buy or Wait changes the question to:



"Can I afford this purchase while

still meeting my future financial obligations?"



This makes the system:



More practical

More cash-flow aware

More personalized

More safety-focused

More useful for real-world spending decisions

🏆 Hackathon Value



Buy or Wait demonstrates how AI can be combined with deterministic financial logic.



AI handles:

Natural Language

&#x20;      ↓

Financial Information Extraction

The application handles:

Financial Rules

&#x20;      ↓

Cash Flow Forecasting

&#x20;      ↓

Affordability Calculation

&#x20;      ↓

Payment Plan Evaluation



This separation is important because the AI does not make the final affordability calculation.



Instead:



AI

&#x20;↓

Extract structured data



Deterministic Engine

&#x20;↓

Calculate financial safety



Decision Layer

&#x20;↓

Recommend Buy / Wait / EMI



This architecture makes the system easier to reason about and reduces the risk of relying on an AI model for arithmetic and financial rule enforcement.



🔮 Future Improvements



Possible future versions could include:



📸 Receipt and invoice image understanding

🏦 Bank transaction integration

📱 WhatsApp / Telegram interface

📊 Spending analytics dashboard

🔔 Upcoming payment reminders

📈 Monthly financial health score

🧠 Personalized spending recommendations

💳 Real-time payment option comparison

👤 User accounts and saved financial profiles

📅 Calendar integration for bills and income

🔐 Secure financial-data storage

📱 Mobile application

🎯 Project Goal



The goal of Buy or Wait is to build an intelligent financial decision agent that helps people make better purchase decisions by considering their entire financial timeline instead of only their current account balance.



The system aims to answer one simple question:



"Should I buy it now, use a payment plan, or wait?"

👨‍💻 Built With

Python

FastAPI

OpenAI API

HTML

CSS

JavaScript

GitHub

Render

📜 Disclaimer



Buy or Wait is a hackathon / educational project intended to demonstrate AI-powered financial decision support.



It does not provide professional financial, investment, tax, or legal advice.



Users should independently verify financial decisions before making payments or taking on debt.



⭐ If You Like This Project



If you find the idea interesting, consider giving the repository a ⭐ on GitHub.



Repository:

https://github.com/abhishekam26/buy-or-wait



Live Demo:

https://buy-or-wait.onrender.com

