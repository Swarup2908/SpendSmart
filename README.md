
# SpendSmart: Expense Tracker Dashboard

SpendSmart is an interactive expense tracker dashboard built with Streamlit. It provides insightful visualizations and data analysis tools to help users better manage their finances by analyzing their daily transactions.

---

## Features

- **Upload Dataset:** Upload your CSV file containing transaction data.
- **Customizable Visualizations:** Choose your preferred color schemes and adjust axis font sizes for the graphs.
- **Key Metrics:** View total income, total expenses, and other financial metrics.
- **Data Cleaning & Transformation:** Automatically handles missing values and formats your data for seamless analysis.
- **Interactive Filters:** Filter data by transaction amount and explore customized insights.
- **Dynamic Visualizations:**
  - Transaction amount distribution
  - Amount spent per category with mode comparison
  - Monthly expense trends
  - Correlation matrix
  - Income vs. Expense pie chart
- **Top Insights:** Analyze top spending categories and high vs. low expense distributions.
- **Monthly Overview:** Compare average monthly income and expenses.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/spendsmart.git
   ```
2. Navigate to the project directory:
   ```bash
   cd spendsmart
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Open the app in your browser (usually at `http://localhost:8501`).

---

## Dataset Requirements

The uploaded CSV file should have the following columns:
- `Date` (Transaction date in any standard format)
- `Amount` (Transaction amount in numeric format)
- `Category` (e.g., Food, Rent, Utilities)
- `Subcategory` (Optional, e.g., Groceries under Food)
- `Income/Expense` (Specifies whether the transaction is an "Income" or "Expense")
- `Mode` (Optional, e.g., Cash, Credit Card, Debit Card)

**Note:** Ensure the dataset contains valid data for accurate analysis.

---

## File Structure

- **`app.py`**: Main application file for the Streamlit dashboard.
- **`requirements.txt`**: List of dependencies required for the project.
- **`README.md`**: Documentation file for the project.

---

## Visualizations

1. **Transaction Amount Distribution:** A histogram showcasing transaction frequency by amount.
2. **Amount Spent Per Category:** Boxplot comparing amounts spent across categories and modes.
3. **Correlation Matrix:** Heatmap showing relationships between numeric variables.
4. **Monthly Expenses:** Bar chart summarizing monthly expenses.
5. **Income vs. Expense:** Pie chart visualizing the proportion of income to expenses.
6. **Top Spending Categories:** Bar chart of the top categories by expense.
7. **High vs. Low Expense Count:** Bar chart categorizing expenses as high or low based on a threshold.

---

## Customization Options

- Adjust color schemes for the visualizations.
- Modify axis font sizes for better readability.
- Filter data dynamically using the sidebar sliders.

---

## Key Metrics

- **Total Expense:** INR [Calculated Total Expense]
- **Total Income:** INR [Calculated Total Income]
- **Average Monthly Income vs. Expenses:** Insight into surplus or deficit trends.

---

## Example CSV File Format

```csv
Date,Amount,Category,Subcategory,Income/Expense,Mode,Currency,Note
2024-01-01,500,Food,Groceries,Expense,Credit Card,INR,Weekly shopping
2024-01-02,2000,Salary,,Income,Bank Transfer,INR,January Salary
```

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as per the license terms.

---

## Author

Developed by [Swarup](https://github.com/Swarup2908).  
For any queries or contributions, feel free to open an issue or reach out.
