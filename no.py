import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Set up Streamlit page configuration
st.set_page_config(page_title="SpendSmart", layout="wide")

# Sidebar Configuration
st.sidebar.title("Expense Tracker Dashboard")
st.sidebar.write("Navigate through different sections")

# Welcome Message at the top with white text and dark blue background
st.markdown("<h1 style='text-align: center; color: white;  padding: 10px;'>Welcome to the Expense Tracker!</h1>", unsafe_allow_html=True)
st.write("This dashboard provides insights into your daily transactions, helping you understand and manage your finances effectively.")

# File Upload
st.sidebar.subheader("Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Choose a file", type="csv")
if uploaded_file:
    data_df = pd.read_csv(uploaded_file)
else:
    st.write("Please upload a CSV file to continue.")
    st.stop()

# Visualization Customization Options
st.sidebar.subheader("Visualization Customizations")
color_option = st.sidebar.selectbox("Select Color Scheme", ["mediumseagreen", "lightblue", "salmon", "coral", "orange"])
font_size = st.sidebar.slider("Adjust Axis Font Size", 8, 14, 10)

# Initial Data Preview
st.write("## Dataset Overview")
st.write(data_df.head())

# Display data shape
st.write(f"**Dataset Shape:** {data_df.shape[0]} rows and {data_df.shape[1]} columns")

# Display summary statistics and info
st.write("### Summary Statistics")
st.write(data_df.describe())

# Check for missing values
st.write("### Missing Values Summary")
st.write(data_df.isnull().sum())

# Clean and Transform Data
data_df = data_df[data_df['Amount'] > 0]
data_df['Subcategory'] = data_df['Subcategory'].fillna('Unknown')
data_df['Note'] = data_df['Note'].fillna('')
data_df['Mode'] = data_df['Mode'].str.strip()
data_df['Category'] = data_df['Category'].str.strip()
data_df['Subcategory'] = data_df['Subcategory'].str.strip()
data_df['Income/Expense'] = data_df['Income/Expense'].str.strip()
data_df['Currency'] = data_df['Currency'].str.strip()
data_df = data_df.dropna()

# Convert Date and extract Day, Month, Year, and Time
if 'Date' in data_df.columns:
    data_df['Date'] = pd.to_datetime(data_df['Date'], errors='coerce')
    data_df['Day'] = data_df['Date'].dt.day
    data_df['Month'] = data_df['Date'].dt.month
    data_df['Year'] = data_df['Date'].dt.year
    data_df['Time'] = data_df['Date'].dt.strftime('%H:%M:%S').fillna('00:00:00')
else:
    st.error("The 'Date' column does not exist in the dataset.")

# Filter data based on amount
filtered_data = data_df[data_df['Amount'] < 2000]

# Sidebar filters
st.sidebar.subheader("Data Filters")
min_amount, max_amount = st.sidebar.slider("Filter by Amount", min_value=0, max_value=int(data_df['Amount'].max()), value=(0, 2000))
filtered_data = data_df[(data_df['Amount'] >= min_amount) & (data_df['Amount'] <= max_amount)]

# Main Metrics
st.write("## Key Metrics")
total_expense = data_df[data_df['Income/Expense'] == 'Expense']['Amount'].sum()
total_income = data_df[data_df['Income/Expense'] == 'Income']['Amount'].sum()
st.write(f"**Total Expense:** INR {total_expense}")
st.write(f"**Total Income:** INR {total_income}")

# Data Visualizations in two columns
st.write("## Data Visualizations")

# Set up columns for side-by-side plotting
col1, col2 = st.columns(2)

with col1:
    st.subheader("Transaction Amount Distribution")
    fig, ax = plt.subplots(figsize=(5, 4))
    sns.histplot(filtered_data['Amount'], bins=30, color=color_option, kde=True)
    ax.set_title("Transaction Amount Distribution")
    ax.set_xlabel("Amount", fontsize=font_size)
    ax.set_ylabel("Frequency", fontsize=font_size)
    plt.xticks(fontsize=font_size)
    plt.yticks(fontsize=font_size)
    st.pyplot(fig)

with col2:
    st.subheader("Amount Spent per Category")

    # Select the top 12 categories based on total amount spent
    top_categories = data_df.groupby('Category')['Amount'].sum().nlargest(12).index
    filtered_data = data_df[data_df['Category'].isin(top_categories)]

    # Select the top 3 modes based on total amount spent
    top_modes = (
        filtered_data.groupby('Mode')['Amount']
        .sum()
        .nlargest(3)  # Adjust this number to limit the modes shown
        .index
    )
    filtered_data = filtered_data[filtered_data['Mode'].isin(top_modes)]

    fig, ax = plt.subplots(figsize=(5, 4))
    sns.boxplot(x='Category', y='Amount', data=filtered_data, hue='Mode', palette='Set2')
    ax.set_ylim(0, 5000)
    plt.xticks(rotation=45, fontsize=font_size, ha='right')
    plt.yticks(fontsize=font_size)
    ax.legend(title="Mode", loc="upper right")  # Position the legend in the top right
    plt.tight_layout()
    st.pyplot(fig)



col3, col4 = st.columns(2)

with col3:
    st.subheader("Correlation Matrix")
    fig, ax = plt.subplots(figsize=(5, 4))
    numerical_df = data_df.select_dtypes(include=['number'])
    correlation_matrix = numerical_df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    plt.xticks(fontsize=font_size)
    plt.yticks(fontsize=font_size)
    st.pyplot(fig)

with col4:
    st.subheader("Monthly Expenses")
    fig, ax = plt.subplots(figsize=(5, 4))
    monthly_expenses = data_df[data_df['Income/Expense'] == 'Expense'].groupby('Month')['Amount'].sum()
    monthly_expenses.plot(kind='bar', color=color_option, ax=ax)
    ax.set_title("Monthly Expenses")
    ax.set_xlabel("Month", fontsize=font_size)
    ax.set_ylabel("Total Expense (INR)", fontsize=font_size)
    plt.xticks(rotation=45, fontsize=font_size)
    plt.yticks(fontsize=font_size)
    st.pyplot(fig)

col5, col6 = st.columns(2)

with col5:
    st.subheader("Expenses by Category")

    # Select the top N categories based on total expense amount (e.g., top 10)
    top_n_categories = 10  # Adjust this number to reduce the categories as desired
    category_expenses = (
        data_df[data_df['Income/Expense'] == 'Expense']
        .groupby('Category')['Amount']
        .sum()
        .nlargest(top_n_categories)
    )

    fig, ax = plt.subplots(figsize=(5, 4))
    category_expenses.plot(kind='bar', color=color_option, ax=ax)
    ax.set_title("Expenses by Category")
    ax.set_xlabel("Category", fontsize=font_size)
    ax.set_ylabel("Total Expense (INR)", fontsize=font_size)
    plt.xticks(rotation=45, fontsize=font_size)
    plt.yticks(fontsize=font_size)
    plt.tight_layout()
    st.pyplot(fig)



with col6:
    st.subheader("Income vs Expense Distribution")
    fig, ax = plt.subplots(figsize=(5, 4))
    labels = ['Income', 'Expense']
    sizes = [total_income, total_expense]
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'coral'], wedgeprops={'edgecolor': 'black'})
    st.pyplot(fig)

# Additional Insights in two columns
st.write("## Additional Insights")

col7, col8 = st.columns(2)

with col7:
    st.subheader("Top Spending Categories")
    top_categories = data_df[data_df['Income/Expense'] == 'Expense'].groupby('Category')['Amount'].sum().sort_values(ascending=False).head(5)
    st.write(top_categories)

with col8:
    st.subheader("High vs. Low Expenses")
    expense_threshold = 1000
    data_df['Expense Type'] = data_df['Amount'].apply(lambda x: 'High' if x > expense_threshold else 'Low')
    expense_type_counts = data_df['Expense Type'].value_counts()
    fig, ax = plt.subplots(figsize=(5, 4))
    expense_type_counts.plot(kind='bar', color=[color_option, 'lightgreen'], ax=ax)
    ax.set_title("High vs. Low Expense Count")
    plt.xticks(fontsize=font_size)
    plt.yticks(fontsize=font_size)
    st.pyplot(fig)

# Average Monthly Income vs Expenses in single column
st.subheader("Average Monthly Income vs Expenses")
monthly_income = data_df[data_df['Income/Expense'] == 'Income'].groupby(['Year', 'Month'])['Amount'].sum().mean()
monthly_expense = data_df[data_df['Income/Expense'] == 'Expense'].groupby(['Year', 'Month'])['Amount'].sum().mean()
st.write(f"Average Monthly Income: INR {monthly_income:.2f}")
st.write(f"Average Monthly Expense: INR {monthly_expense:.2f}")
if monthly_income > monthly_expense:
    st.success("On average, there is a monthly surplus!")
else:
    st.error("On average, there is a monthly deficit.")

# Thank You Message
st.markdown("<h2 style='text-align: center; color: darkgreen;'>Thank you for using SpendSmart!</h2>", unsafe_allow_html=True)
