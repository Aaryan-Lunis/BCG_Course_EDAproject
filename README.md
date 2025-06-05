
# 💼 BCG GenAI Job Simulation – Financial Data Cleaning & AI Chatbot

This project is part of a job simulation course offered by **BCG (Boston Consulting Group)** in collaboration with **Forage**. The goal of the project was to simulate a real-world business scenario where raw financial data is cleaned, analyzed, and used to power a simple AI chatbot for answering key financial questions.

---

## 📌 Project Overview

The project involved the following key steps:

1. **Manual Data Extraction**

   * Financial data was manually extracted from 10-K reports of Microsoft, Tesla, and Apple.
   * Metrics collected: Total Revenue, Net Income, Total Assets, Total Liabilities, and Cash Flow from Operating Activities for the past three fiscal years.

2. **Data Cleaning & Analysis (Python, Pandas)**

   * Loaded the financial data into a pandas DataFrame.
   * Cleaned and structured the data for trend analysis.
   * Calculated year-over-year growth metrics.
   * Insights derived were used to inform chatbot responses.

3. **AI Chatbot Prototype (Streamlit)**

   * Built a **Streamlit web app** simulating an AI-powered chatbot.
   * Responds to 3–5 predefined financial queries using the cleaned data.
   * Basic logic built with `if-else` statements for structured, quick responses.

---

## 🚀 Features

* 📊 Clean and structured financial dataset from real 10-K filings
* 📈 Trend analysis using pandas (e.g., revenue growth, net income change)
* 🤖 Streamlit chatbot that answers predefined financial questions
* 💬 Easy-to-use interface with instant responses
* 📝 Fully documented code and logic for beginner-friendly understanding

---

## 📂 Project Structure

```
├── data/
│   └── financial_data.csv            # Cleaned financial data
├── notebook/
│   └── financial_analysis.ipynb      # Jupyter notebook with analysis
├── app/
│   └── chatbot.py                # Streamlit chatbot script
├── screenshots/
│   └── *.png                         # UI snapshots (optional)
├── README.md                         # This file
```

---

## 🛠 Technologies Used

* **Python**
* **Pandas**
* **Streamlit**
* **Jupyter Notebook**
* **Git & GitHub**

---

## 💡 Sample Queries the Chatbot Can Handle

* "What is the total revenue of Tesla?"
* "How has Apple’s net income changed over the last year?"
* "What are the total assets of Microsoft?"
* "How much is the operating cash flow of Apple?"
* "What are the liabilities of Tesla?"

---

## 📸 Screenshots (Optional)

> ![image](https://github.com/user-attachments/assets/caa2cf24-7e5b-4029-ba1a-88b54d5cb5ec)

---

## ✅ How to Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/Aaryan-Lunis/bcg-genai-simulation.git
   cd BCG_Course_EDAproject
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the chatbot app**

   ```bash
   streamlit run chatbot.py
   ```

---

## 📄 License

This project is for educational purposes only as part of a simulation experience through BCG x Forage. All trademarks and copyrights belong to their respective owners.

---
