import streamlit as st
import pandas as pd

# Load financial data
df = pd.read_csv('financial_data.csv')

# Get latest year data
latest_year = df['Fiscal Year'].max()
latest_data = df[df['Fiscal Year'] == latest_year]

# Calculate YoY Net Income change
df_sorted = df.sort_values(by=['Company', 'Fiscal Year'])
df_sorted['Net Income Change'] = df_sorted.groupby('Company')['Net Income'].diff()

# Create response mapping
responses = {
    "What is the total revenue?": "\n".join(
        f"{row['Company']}: ${row['Total Revenue']:,} million" for _, row in latest_data.iterrows()
    ),
    "How has net income changed over the last year?": "\n".join(
        f"{row['Company']}: ${row['Net Income Change']:,} million change"
        for _, row in df_sorted[df_sorted['Fiscal Year'] == latest_year].iterrows()
    ),
    "What is the total assets value?": "\n".join(
        f"{row['Company']}: ${row['Total Assets']:,} million" for _, row in latest_data.iterrows()
    ),
    "What is the total liabilities?": "\n".join(
        f"{row['Company']}: ${row['Total Liabilities']:,} million" for _, row in latest_data.iterrows()
    ),
    "How much cash flow from operating activities?": "\n".join(
        f"{row['Company']}: ${row['Cash Flow from Operating Activities']:,} million"
        for _, row in latest_data.iterrows()
    )
}

# Streamlit UI
st.title("📊 Financial Data Chatbot")
st.markdown("Ask one of the predefined questions about financial metrics for Microsoft, Tesla, and Apple (2023).")

query = st.text_input("Enter your question:")

if query:
    response = responses.get(query, "❌ Sorry, I can only answer predefined queries.")
    st.text_area("Chatbot Response", response, height=150)
