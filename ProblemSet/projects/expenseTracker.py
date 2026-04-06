import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import os
from pathlib import Path

# ==================== Configuration ====================
PAGE_TITLE = "💰 Expense Tracker"
PAGE_ICON = "💰"
CURRENCY = "Rs"
DATA_FILE = "expenses_data.csv"
CATEGORIES = ["Food & Dining", "Transport", "Entertainment", "Shopping", "Bills & Utilities", 
              "Healthcare", "Education", "Personal Care", "Gifts & Donations", "Other"]

# ==================== Page Configuration ====================
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide", initial_sidebar_state="expanded")

# ==================== Load/Initialize Data ====================
def load_expenses():
    """Load expenses from CSV file"""
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)
        df['Date'] = pd.to_datetime(df['Date'])
        return df.sort_values('Date', ascending=False)
    else:
        return pd.DataFrame(columns=['Date', 'Category', 'Amount', 'Description', 'Payment_Method'])

def save_expenses(df):
    """Save expenses to CSV file"""
    df_save = df.copy()
    df_save['Date'] = df_save['Date'].dt.strftime('%Y-%m-%d %H:%M:%S')
    df_save.to_csv(DATA_FILE, index=False)

# ==================== Initialize Session State ====================
if "df" not in st.session_state:
    st.session_state.df = load_expenses()

# ==================== Utility Functions ====================
def add_expense(date, category, amount, description, payment_method):
    """Add a new expense"""
    new_expense = pd.DataFrame({
        'Date': [pd.to_datetime(date)],
        'Category': [category],
        'Amount': [float(amount)],
        'Description': [description],
        'Payment_Method': [payment_method]
    })
    st.session_state.df = pd.concat([st.session_state.df, new_expense], ignore_index=True)
    st.session_state.df = st.session_state.df.sort_values('Date', ascending=False).reset_index(drop=True)
    save_expenses(st.session_state.df)
    return True

def delete_expense(index):
    """Delete an expense by index"""
    st.session_state.df = st.session_state.df.drop(index).reset_index(drop=True)
    save_expenses(st.session_state.df)
    return True

def get_summary_stats(df):
    """Calculate summary statistics"""
    if df.empty:
        return {
            'total': 0,
            'avg': 0,
            'max': 0,
            'count': 0
        }
    return {
        'total': df['Amount'].sum(),
        'avg': df['Amount'].mean(),
        'max': df['Amount'].max(),
        'count': len(df)
    }

def get_monthly_summary(df):
    """Get monthly spending summary"""
    if df.empty:
        return pd.DataFrame()
    monthly = df.copy()
    monthly['Month'] = pd.to_datetime(monthly['Date']).dt.to_period('M')
    return monthly.groupby('Month')['Amount'].sum().reset_index()

def get_category_summary(df):
    """Get spending by category"""
    if df.empty:
        return pd.DataFrame()
    return df.groupby('Category')['Amount'].sum().reset_index().sort_values('Amount', ascending=False)

# ==================== Sidebar Navigation ====================
st.sidebar.title("🎯 Navigation")
page = st.sidebar.radio("Select Page", 
                       ["📊 Dashboard", "➕ Add Expense", "📋 View Expenses", 
                        "📈 Analytics", "💼 Budget Tracker", "⚙️ Settings"])

# ==================== PAGE: Dashboard ====================
if page == "📊 Dashboard":
    st.title("📊 Dashboard")
    
    if st.session_state.df.empty:
        st.info("📭 No expenses recorded yet. Start by adding your first expense!")
    else:
        # Summary Cards
        col1, col2, col3, col4 = st.columns(4)
        
        stats = get_summary_stats(st.session_state.df)
        
        with col1:
            st.metric("💵 Total Spent", f"{CURRENCY} {stats['total']:.2f}")
        
        with col2:
            st.metric("📊 Avg Expense", f"{CURRENCY} {stats['avg']:.2f}")
        
        with col3:
            st.metric("📈 Max Expense", f"{CURRENCY} {stats['max']:.2f}")
        
        with col4:
            st.metric("🔢 Total Entries", stats['count'])
        
        st.divider()
        
        # Time Period Selection
        col1, col2 = st.columns(2)
        with col1:
            time_period = st.radio("Filter by:", ["All Time", "Last 30 Days", "Last 90 Days", "This Month", "Last Month"])
        
        # Filter data based on time period
        filtered_df = st.session_state.df.copy()
        today = pd.to_datetime('today')
        
        if time_period == "Last 30 Days":
            filtered_df = filtered_df[filtered_df['Date'] >= today - timedelta(days=30)]
        elif time_period == "Last 90 Days":
            filtered_df = filtered_df[filtered_df['Date'] >= today - timedelta(days=90)]
        elif time_period == "This Month":
            filtered_df = filtered_df[(filtered_df['Date'].dt.month == today.month) & 
                                     (filtered_df['Date'].dt.year == today.year)]
        elif time_period == "Last Month":
            last_month = today - timedelta(days=today.day)
            filtered_df = filtered_df[(filtered_df['Date'].dt.month == last_month.month) & 
                                     (filtered_df['Date'].dt.year == last_month.year)]
        
        # Top Categories
        st.subheader("🏆 Top Spending Categories")
        if not filtered_df.empty:
            category_stats = get_category_summary(filtered_df)
            col1, col2 = st.columns(2)
            
            with col1:
                fig_pie = px.pie(category_stats, values='Amount', names='Category', 
                                title="Spending Distribution")
                st.plotly_chart(fig_pie, use_container_width=True)
            
            with col2:
                fig_bar = px.bar(category_stats, x='Category', y='Amount',
                                title="Amount by Category", color='Amount',
                                color_continuous_scale='Viridis')
                st.plotly_chart(fig_bar, use_container_width=True)

# ==================== PAGE: Add Expense ====================
elif page == "➕ Add Expense":
    st.title("➕ Add New Expense")
    
    with st.form("expense_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            expense_date = st.date_input("Date", value=pd.to_datetime('today'))
            expense_time = st.time_input("Time", value=pd.to_datetime('today').time())
        
        with col2:
            category = st.selectbox("Category", CATEGORIES)
            amount = st.number_input("Amount", min_value=0.0, step=0.01, format="%.2f")
        
        col3, col4 = st.columns(2)
        
        with col3:
            payment_method = st.selectbox("Payment Method", 
                                         ["Cash", "Debit Card", "Credit Card", "UPI", "Net Banking", "Other"])
        
        with col4:
            description = st.text_input("Description/Note", placeholder="e.g., Lunch at restaurant")
        
        col5, col6 = st.columns(2)
        
        with col5:
            submit = st.form_submit_button("✅ Add Expense", use_container_width=True)
        
        with col6:
            st.form_submit_button("🔄 Reset", use_container_width=True)
        
        if submit:
            if amount > 0 and description:
                combined_datetime = datetime.combine(expense_date, expense_time)
                if add_expense(combined_datetime, category, amount, description, payment_method):
                    st.success(f"✅ Expense of {CURRENCY} {amount:.2f} added successfully!")
            else:
                st.error("❌ Please enter valid amount and description")

# ==================== PAGE: View Expenses ====================
elif page == "📋 View Expenses":
    st.title("📋 View All Expenses")
    
    if st.session_state.df.empty:
        st.info("📭 No expenses to display")
    else:
        # Filters
        col1, col2, col3 = st.columns(3)
        
        with col1:
            filter_category = st.multiselect("Filter by Category", 
                                            ["All"] + CATEGORIES, 
                                            default="All")
        
        with col2:
            filter_payment = st.multiselect("Filter by Payment Method",
                                           ["All"] + ["Cash", "Debit Card", "Credit Card", "UPI", "Net Banking", "Other"],
                                           default="All")
        
        with col3:
            date_range = st.date_input("Date Range", 
                                      value=[st.session_state.df['Date'].min().date(), 
                                             st.session_state.df['Date'].max().date()],
                                      max_value=pd.to_datetime('today'))
        
        # Apply filters
        filtered_df = st.session_state.df.copy()
        
        if "All" not in filter_category:
            filtered_df = filtered_df[filtered_df['Category'].isin(filter_category)]
        
        if "All" not in filter_payment:
            filtered_df = filtered_df[filtered_df['Payment_Method'].isin(filter_payment)]
        
        if len(date_range) == 2:
            start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
            filtered_df = filtered_df[(filtered_df['Date'] >= start_date) & 
                                     (filtered_df['Date'] <= end_date + timedelta(days=1))]
        
        # Display stats
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total", f"{CURRENCY} {filtered_df['Amount'].sum():.2f}")
        with col2:
            st.metric("Average", f"{CURRENCY} {filtered_df['Amount'].mean():.2f}" if not filtered_df.empty else "N/A")
        with col3:
            st.metric("Count", len(filtered_df))
        
        st.divider()
        
        # Display table
        display_df = filtered_df.copy()
        display_df['Date'] = display_df['Date'].dt.strftime('%Y-%m-%d %H:%M')
        display_df['Amount'] = display_df['Amount'].apply(lambda x: f"{CURRENCY} {x:.2f}")
        
        st.dataframe(display_df, use_container_width=True, hide_index=True)
        
        # Delete expense option
        st.subheader("🗑️ Delete Expense")
        col1, col2 = st.columns(2)
        
        with col1:
            expense_to_delete = st.selectbox("Select expense to delete",
                                            range(len(st.session_state.df)),
                                            format_func=lambda i: f"{st.session_state.df.iloc[i]['Date'].strftime('%Y-%m-%d')} - {st.session_state.df.iloc[i]['Category']} - {CURRENCY} {st.session_state.df.iloc[i]['Amount']:.2f}")
        
        with col2:
            if st.button("🗑️ Delete", use_container_width=True):
                if delete_expense(expense_to_delete):
                    st.success("✅ Expense deleted successfully!")
                    st.rerun()

# ==================== PAGE: Analytics ====================
elif page == "📈 Analytics":
    st.title("📈 Analytics & Insights")
    
    if st.session_state.df.empty:
        st.info("📭 No data to analyze. Start adding expenses!")
    else:
        # Analysis period
        col1, col2 = st.columns(2)
        
        with col1:
            analysis_type = st.radio("Analysis Type", ["Monthly Trend", "Category Distribution", "Payment Method Analysis", "Daily Spending"])
        
        with col2:
            months_back = st.slider("Months to analyze", 1, 24, 6)
        
        cutoff_date = pd.to_datetime('today') - timedelta(days=30*months_back)
        analysis_df = st.session_state.df[st.session_state.df['Date'] >= cutoff_date]
        
        if analysis_type == "Monthly Trend":
            st.subheader("📅 Monthly Spending Trend")
            monthly = analysis_df.copy()
            monthly['Month'] = monthly['Date'].dt.to_period('M').astype(str)
            monthly_sum = monthly.groupby('Month')['Amount'].sum().reset_index()
            
            fig = px.line(monthly_sum, x='Month', y='Amount', 
                         title="Monthly Spending Trend", markers=True,
                         labels={'Amount': f'Amount ({CURRENCY})'})
            st.plotly_chart(fig, use_container_width=True)
        
        elif analysis_type == "Category Distribution":
            st.subheader("🎯 Spending by Category")
            category_dist = analysis_df.groupby('Category')['Amount'].sum().reset_index().sort_values('Amount', ascending=False)
            
            col1, col2 = st.columns(2)
            
            with col1:
                fig = px.pie(category_dist, values='Amount', names='Category',
                            title="Category Distribution")
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                fig = px.bar(category_dist, x='Amount', y='Category', orientation='h',
                            title="Spending by Category", color='Amount',
                            color_continuous_scale='Viridis')
                st.plotly_chart(fig, use_container_width=True)
        
        elif analysis_type == "Payment Method Analysis":
            st.subheader("💳 Payment Method Usage")
            payment_dist = analysis_df.groupby('Payment_Method')['Amount'].agg(['sum', 'count']).reset_index()
            payment_dist.columns = ['Payment_Method', 'Total_Amount', 'Count']
            
            col1, col2 = st.columns(2)
            
            with col1:
                fig = px.pie(payment_dist, values='Total_Amount', names='Payment_Method',
                            title="Amount by Payment Method")
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                fig = px.bar(payment_dist, x='Payment_Method', y='Count',
                            title="Number of Transactions", color='Count',
                            color_continuous_scale='Blues')
                st.plotly_chart(fig, use_container_width=True)
        
        elif analysis_type == "Daily Spending":
            st.subheader("📆 Daily Spending Pattern")
            daily = analysis_df.copy()
            daily['Date_only'] = daily['Date'].dt.date
            daily_sum = daily.groupby('Date_only')['Amount'].sum().reset_index()
            daily_sum.columns = ['Date', 'Amount']
            
            fig = px.bar(daily_sum, x='Date', y='Amount',
                        title="Daily Spending Amount",
                        labels={'Amount': f'Amount ({CURRENCY})'})
            st.plotly_chart(fig, use_container_width=True)

# ==================== PAGE: Budget Tracker ====================
elif page == "💼 Budget Tracker":
    st.title("💼 Budget Tracker")
    
    st.subheader("📋 Set Monthly Budgets")
    
    # Initialize budget session
    if "budgets" not in st.session_state:
        st.session_state.budgets = {}
    
    col1, col2 = st.columns(2)
    
    with col1:
        budget_category = st.selectbox("Select Category", CATEGORIES)
    
    with col2:
        budget_amount = st.number_input("Budget Amount", min_value=0.0, step=100.0)
    
    if st.button("💾 Set Budget"):
        st.session_state.budgets[budget_category] = budget_amount
        st.success(f"Budget set for {budget_category}: {CURRENCY} {budget_amount:.2f}")
    
    st.divider()
    
    # Display budget status
    if st.session_state.budgets:
        st.subheader("📊 Budget Status")
        
        current_month = datetime.now()
        month_df = st.session_state.df[(st.session_state.df['Date'].dt.month == current_month.month) &
                                       (st.session_state.df['Date'].dt.year == current_month.year)]
        
        budget_data = []
        for category, budget in st.session_state.budgets.items():
            spent = month_df[month_df['Category'] == category]['Amount'].sum()
            remaining = budget - spent
            percentage = (spent / budget * 100) if budget > 0 else 0
            
            budget_data.append({
                'Category': category,
                'Budget': budget,
                'Spent': spent,
                'Remaining': remaining,
                'Percentage': percentage
            })
        
        budget_df = pd.DataFrame(budget_data)
        
        for _, row in budget_df.iterrows():
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.write(f"**{row['Category']}**")
            
            with col2:
                progress = min(row['Percentage'] / 100, 1.0)
                color = '🟢' if row['Percentage'] < 75 else '🟡' if row['Percentage'] < 100 else '🔴'
                st.progress(progress, text=f"{color} {row['Percentage']:.1f}%")
            
            with col3:
                st.write(f"{CURRENCY} {row['Spent']:.2f} / {CURRENCY} {row['Budget']:.2f}")
            
            if row['Remaining'] < 0:
                st.warning(f"⚠️ Budget exceeded by {CURRENCY} {abs(row['Remaining']):.2f}")
    else:
        st.info("No budgets set yet. Create your first budget above!")

# ==================== PAGE: Settings ====================
elif page == "⚙️ Settings":
    st.title("⚙️ Settings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Data Management")
        
        if st.button("📥 Export Data to CSV", use_container_width=True):
            csv = st.session_state.df.to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name=f"expenses_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )
        
        if st.button("🔄 Refresh Data", use_container_width=True):
            st.session_state.df = load_expenses()
            st.rerun()
    
    with col2:
        st.subheader("⚠️ Danger Zone")
        
        if st.button("🗑️ Delete All Data", use_container_width=True):
            if os.path.exists(DATA_FILE):
                if st.checkbox("I understand this action is irreversible"):
                    if st.button("Confirm Delete All"):
                        os.remove(DATA_FILE)
                        st.session_state.df = pd.DataFrame(columns=['Date', 'Category', 'Amount', 'Description', 'Payment_Method'])
                        st.success("✅ All data deleted successfully!")
                        st.rerun()
    
    st.divider()
    
    st.subheader("📈 Statistics")
    if not st.session_state.df.empty:
        col1, col2 = st.columns(2)
        
        with col1:
            st.write(f"**Total Expenses:** {len(st.session_state.df)}")
            st.write(f"**Total Spent:** {CURRENCY} {st.session_state.df['Amount'].sum():.2f}")
        
        with col2:
            st.write(f"**Date Range:** {st.session_state.df['Date'].min().date()} to {st.session_state.df['Date'].max().date()}")
            st.write(f"**Categories Used:** {st.session_state.df['Category'].nunique()}")
    
    st.divider()
    
    st.subheader("ℹ️ About")
    st.info("""
    **💰 Expense Tracker v1.0**
    
    A comprehensive expense tracking application built with Streamlit.
    
    **Features:**
    - ✅ Add and manage expenses
    - ✅ Categorize expenses
    - ✅ Track by payment method
    - ✅ Visual analytics and charts
    - ✅ Monthly budget tracking
    - ✅ Data export functionality
    - ✅ Responsive design
    """)
