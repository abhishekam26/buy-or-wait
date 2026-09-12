# Buy or Wait



\# 💰 Buy or Wait



AI-powered financial decision assistant that helps users decide whether they can safely afford a purchase.



\## 🚀 What it does



Buy or Wait analyzes:



\- Current account balance

\- Purchase amount

\- Upcoming rent and bills

\- Credit card payments

\- Confirmed future income

\- EMI / installment options

\- Minimum balance requirement



It then gives a clear financial decision.



\## ✨ Key Features



\- Natural language financial input

\- AI-powered financial information extraction

\- Cash-flow based affordability analysis

\- Minimum balance protection

\- EMI/payment-plan evaluation

\- Buy now vs wait decision

\- Simple fintech-style web interface

\- Live cloud deployment



\## 🧠 How it works



User Input

&#x20;   ↓

AI Financial Data Extraction

&#x20;   ↓

Cash Flow Timeline

&#x20;   ↓

Affordability Engine

&#x20;   ↓

Payment Plan Evaluation

&#x20;   ↓

Buy or Wait Decision

&#x20;   ↓

Web UI



\## 🛠️ Tech Stack



\- Python

\- FastAPI

\- OpenAI API

\- HTML

\- CSS

\- JavaScript

\- Render

\- GitHub



\## 📊 Example



User:



"Na account lo 120000 undi. 80000 laptop konali.

September 15th rent 25000 pay cheyyali.

September 18th credit card 12000 pay cheyyali.

September 30th salary 70000 vastundi."



The system evaluates the complete cash-flow timeline and can recommend:



AFFORDABLE\_WITH\_PLAN



4 Month EMI



while protecting the configured minimum balance.



\## 🔐 Security



API keys are stored using environment variables.



.env is excluded from Git using .gitignore.



Never commit API keys or other secrets to GitHub.



\## 🌐 Live Demo



https://buy-or-wait.onrender.com



\## 📁 Project Structure



buy-or-wait/

│

├── main.py

├── ai\_parser.py

├── index.html

├── style.css

├── script.js

├── requirements.txt

├── .gitignore

└── README.md



\## ▶️ Run Locally



Create and activate a virtual environment:



python -m venv venv



venv\\Scripts\\activate



Install dependencies:



pip install -r requirements.txt



Set your OpenAI API key in .env:



OPENAI\_API\_KEY=your\_api\_key\_here



Run the application:



uvicorn main:app --reload



Open:



http://127.0.0.1:8000



\## 🎯 Project Goal



The goal of Buy or Wait is to move beyond simple balance checking and make purchase decisions using the user's complete financial timeline, upcoming obligations, confirmed income, and payment preferences.

