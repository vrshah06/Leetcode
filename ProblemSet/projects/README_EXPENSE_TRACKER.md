# 💰 Expense Tracker - Streamlit App

A comprehensive expense tracking application built with Python and Streamlit that helps you manage and analyze your spending habits.

## ✨ Features

### 📊 Dashboard
- **Overview Cards**: Quick view of total spent, average expense, max expense, and total entries
- **Time-based Filtering**: View spending data for All Time, Last 30/90 Days, This Month, or Last Month
- **Top Categories**: Visual distribution of spending by category with pie and bar charts

### ➕ Add Expense
- **Easy Data Entry**: Simple form to add new expenses
- **Date & Time Tracking**: Record exact date and time of each transaction
- **Category Selection**: Choose from 10 pre-defined categories or custom ones
- **Payment Methods**: Track payment type (Cash, Cards, UPI, Net Banking, etc.)
- **Description Support**: Add notes for each expense

### 📋 View Expenses
- **Multi-filter Support**: Filter by category, payment method, and date range
- **Data Table**: View all expenses with detailed information
- **Summary Stats**: See total, average, and count of filtered expenses
- **Delete Function**: Remove individual expenses when needed

### 📈 Analytics
- **Monthly Trend**: Line chart showing spending patterns over time
- **Category Analysis**: Pie and bar charts for category-wise breakdown
- **Payment Method Analysis**: Visualize payment method usage and frequency
- **Daily Spending**: Bar chart showing daily spending patterns
- **Customizable Range**: Analyze data from 1 to 24 months

### 💼 Budget Tracker
- **Set Monthly Budgets**: Define budgets for each category
- **Progress Monitoring**: Visual progress bars showing budget usage
- **Alert System**: Warnings when budget is exceeded
- **Budget Status**: Real-time view of spent vs. budgeted amounts

### ⚙️ Settings
- **Data Export**: Download your expense data as CSV
- **Data Refresh**: Reload data from disk
- **Bulk Operations**: Delete all data with confirmation
- **Statistics**: View total expenses, date range, and categories used

## 📦 Installation

### Requirements
- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone/Navigate to project directory**
   ```bash
   cd "path/to/Leetcode Problems/ProblemSet/projects"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run expenseTracker.py
   ```

4. The app will open in your default browser (usually at `http://localhost:8501`)

## 🚀 Usage Guide

### Adding Your First Expense
1. Navigate to "➕ Add Expense" page
2. Select the date and time
3. Choose a category from the dropdown
4. Enter the amount
5. Select payment method
6. Add a description/note
7. Click "✅ Add Expense"

### Viewing & Managing Expenses
1. Go to "📋 View Expenses"
2. Use filters to narrow down your search
3. View summary statistics
4. Delete individual expenses using the delete selector

### Analyzing Spending
1. Open "📈 Analytics" tab
2. Choose analysis type (Monthly Trend, Category Distribution, etc.)
3. Adjust number of months to analyze
4. View interactive charts and insights

### Setting Budgets
1. Go to "💼 Budget Tracker"
2. Select a category
3. Enter your monthly budget amount
4. Click "💾 Set Budget"
5. Monitor your spending progress with visual indicators

## 📁 File Structure

```
expenseTracker.py          # Main application file
requirements.txt           # Python dependencies
README.md                  # This file
expenses_data.csv          # Data file (created automatically)
```

## 💾 Data Storage

- Expenses are stored in `expenses_data.csv` in the same directory
- Data persists between sessions
- Supports CSV export for backup

## 🎨 Categories

Default categories include:
- Food & Dining
- Transport
- Entertainment
- Shopping
- Bills & Utilities
- Healthcare
- Education
- Personal Care
- Gifts & Donations
- Other

You can easily add more categories by modifying the `CATEGORIES` list in the code.

## 💳 Payment Methods Supported

- Cash
- Debit Card
- Credit Card
- UPI
- Net Banking
- Other

## 🔍 Key Statistics Tracked

- **Total Spent**: Sum of all expenses
- **Average Expense**: Mean expense amount
- **Maximum Expense**: Highest expense amount
- **Number of Entries**: Total transaction count
- **Category-wise Breakdown**: Spending by category
- **Monthly Trends**: Month-over-month spending analysis
- **Payment Method Distribution**: Which payment method is used most

## ⚠️ Important Notes

1. **Data Backup**: Regularly export your data as CSV for backup
2. **Currency**: Default currency is "Rs" (Indian Rupees). Change it in the code if needed
3. **Date Handling**: Dates are stored with timestamps for accuracy
4. **Budget Reset**: Monthly budgets reset automatically every month

## 🐛 Troubleshooting

**Q: App won't start**
- Ensure all requirements are installed: `pip install -r requirements.txt`
- Check Python version is 3.8+: `python --version`

**Q: Data not saving**
- Check file permissions in the project directory
- Ensure `expenses_data.csv` is not open in another program

**Q: Charts not displaying**
- Plotly may need to be reinstalled: `pip install --upgrade plotly`

**Q: Streamlit port already in use**
- Run on different port: `streamlit run expenseTracker.py --server.port 8502`

## 🤝 Future Enhancements

- 🔐 User authentication and multi-user support
- 📊 Advanced ML-based spending predictions
- 📲 Mobile app version
- 🌐 Cloud sync support
- 📧 Email notifications for budget alerts
- 📈 Recurring expenses automation
- 💰 Multi-currency support

## 📝 License

Open source - Feel free to modify and use as needed

## 👨‍💻 Author

Created as a practical expense management solution

---

**Happy Expense Tracking! 💰**
