import calendar # Core python module
from datetime import datetime # Core python module
import streamlit as st #pip install streamlit
import plotly.graph_objects as go #pip install plotly 
import plotly.express as px # Import plotly express
from streamlit_option_menu import option_menu #pip install streamlit_option_menu 
import database as db # Import database functions
import pandas as pd # Import pandas library

# -------------- SETTINGS --------------------
incomes = ["Salary", "Side hustle"]
expenses = ["Home", "Utilities", "Groceries", "Car", "Other expenses", "Savings"]
groceries = ["Food", "Beverages", "Other grocery expenses"]
car = ["Car payment", "Fuel", "Misc car expenses"]
utilities = ["Electricity", "Water", "Other utility expenses"] 
currency = "EUR"
page_title = "Income and Expenses tracker"
page_icon = "💶" # ":euro_banknote:" Emoji https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"
# --------------------------------------------
# Initialize variables
grocery_total, car_total, utilities_total, groceries_full, car_full, utilities_full = 0, 0, 0, 0, 0, 0
#Color palette
color_palet = ['rgba(31, 119, 180, 0.8)', 'rgba(255, 127, 14, 0.8)', 'rgba(44, 160, 44, 0.8)', \
               'rgba(214, 39, 40, 0.8)', 'rgba(148, 103, 189, 0.8)', 'rgba(140, 86, 75, 0.8)', \
                'rgba(227, 119, 194, 0.8)', 'rgba(127, 127, 127, 0.8)', 'rgba(188, 189, 34, 0.8)', \
                'rgba(23, 190, 207, 0.8)', 'rgba(31, 119, 180, 0.8)', 'rgba(255, 127, 14, 0.8)', \
                'rgba(44, 160, 44, 0.8)', 'rgba(214, 39, 40, 0.8)', 'rgba(148, 103, 189, 0.8)', \
                'magenta', 'rgba(227, 119, 194, 0.8)', 'rgba(127, 127, 127, 0.8)', \
                'rgba(188, 189, 34, 0.8)', 'rgba(23, 190, 207, 0.8)', 'rgba(31, 119, 180, 0.8)', \
                'rgba(255, 127, 14, 0.8)', 'rgba(44, 160, 44, 0.8)', 'rgba(214, 39, 40, 0.8)', \
                'rgba(148, 103, 189, 0.8)', 'rgba(140, 86, 75, 0.8)', 'rgba(227, 119, 194, 0.8)', \
                'rgba(127, 127, 127, 0.8)', 'rgba(31, 119, 180, 0.8)', 'rgba(255, 127, 14, 0.8)', \
                'rgba(44, 160, 44, 0.8)', 'rgba(214, 39, 40, 0.8)', 'rgba(148, 103, 189, 0.8)', \
                'rgba(140, 86, 75, 0.8)', 'rgba(227, 119, 194, 0.8)', 'rgba(127, 127, 127, 0.8)', \
                'rgba(188, 189, 34, 0.8)', 'rgba(23, 190, 207, 0.8)', 'rgba(31, 119, 180, 0.8)', \
                'rgba(255, 127, 14, 0.8)', 'rgba(44, 160, 44, 0.8)', 'rgba(214, 39, 40, 0.8)', \
                'rgba(148, 103, 189, 0.8)', 'rgba(140, 86, 75, 0.8)', 'rgba(227, 119, 194, 0.8)', \
                'rgba(127, 127, 127, 0.8)', 'rgba(188, 189, 34, 0.8)', 'rgba(23, 190, 207, 0.8)' ]

# to override gray link colors with 'source' colors with opacity
opacity = 0.1

def main():
    st.set_page_config(page_title = page_title, page_icon = page_icon, layout = layout)
    st.title(page_title +  ' ' + page_icon)

if __name__ == '__main__':
    main()

# ----Drop down values for selecting the period ----
years = [datetime.today().year, datetime.today().year - 1, datetime.today().year - 2 ] # list of two revious years along with current year
months = list(calendar.month_name[1:]) # list of months in a year

# --- Database interface ---
def get_all_periods():
    items = db.fetch_all_periods()
    periods = [item["key"] for item in items]
    return periods

# --- Hide Streamlit Style ---
hide_st_style = """
                <style>
                #MainMenu {Visibility: hidden;}
                footer {Visibility: hidden;}
                header {Visibility: hidden;}
                </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# ---Navigation Menu---
selected = option_menu(
    menu_title=None,
    options=['Data Entry', 'Data Visualisation'],
    icons=['pencil-fill', 'file-earmark-bar-graph-fill'], #https://icons.getbootstrap.com/
    orientation='horizontal'
)

def expensedetail(*args):
    if expense == 'Groceries':        
        for grocery in groceries:
            st.number_input(f"{grocery}:", min_value = 0.00, format = "%.2f", step = 0.01, key = grocery)
            
    elif expense == 'Car':        
        for cardetail in car:
            st.number_input(f"{cardetail}:", min_value = 0.00, format = "%.2f", step = 0.01, key = cardetail)
            
    elif expense == 'Utilities':        
        for utility in utilities:
            st.number_input(f"{utility}:", min_value = 0.00, format = "%.2f", step = 0.01, key = utility)
            

if selected == 'Data Entry':
    # Input and save periods
    st.header(f'Data entry in {currency}')
    # ---Check box to select if detailed expenses is wanted ---
    agree = st.checkbox('Detailed expenses chosen')
    with st.form("entry_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        col1.selectbox("Select Month", months, key = "month")
        col2.selectbox("Select Year", years, key = "year")
        
        "---"
        with st.expander("Income"):
            for income in incomes:
                st.number_input(f"{income}:", min_value = 0.00, format = "%.2f", step = 0.01, key = income)
        with st.expander("Expenses"):
            for expense in expenses:
                st.number_input(f"{expense}:", min_value = 0.00, format = "%.2f", step = 0.01, key = expense)
                #print(expenses, expense)
                if (expense == 'Groceries' or expense == 'Car' or expense == 'Utilities') and agree:
                    # Call function to enter detailed breakdown of some expenses
                    expensedetail(expense)

        with st.expander("Comment"):
            comment = st.text_area("", "Enter a comment here")

        "---"
        submitted = st.form_submit_button("Save Data")
        if submitted:
            period = str(st.session_state["year"]) + "_" + str(st.session_state["month"])
            incomes = {income: st.session_state[income] for income in incomes}
            expenses = {expense: st.session_state[expense] for expense in expenses}
            for idx_e, (ke, ve) in enumerate(expenses.items()):
                print (f'expenses and expense', expenses, expense)
                if ke == 'Groceries': 
                    groceries_full = ve
                    print (f'Groceries full', ve)
                elif ke == 'Car': 
                    car_full = ve
                elif ke == 'Utilities':
                    utilities_full = ve
                #grocery_full = grocery_sum + grocery
            #if st.session_state[expense] != grocery_sum:
            groceries = {grocery: st.session_state[grocery] for grocery in groceries}
            for idx_g, (kg, vg) in enumerate(groceries.items()):
                grocery_total = grocery_total + vg
            if groceries_full != grocery_total:
                st.error('Check total groceries expenses value is equal to full grocery value', icon="🚨")
                print (f'Groceries full2', groceries_full)
                print (f"Grocery total and full", grocery_total , groceries_full)
            
            car = {cardetail: st.session_state[cardetail] for cardetail in car}
            for idx_c, (kc, vc) in enumerate(car.items()):
                car_total = car_total + vc
            if (car_full != car_total) and (st.error(' ')):
                st.error('Check total car expenses value is equal to full car value', icon="🚨")
                print (f"car total and full", car_total, car_full)

            utilities = {utility: st.session_state[utility] for utility in utilities}
            for idx_u, (ku, vu) in enumerate(utilities.items()):
                utilities_total = utilities_total + vu
            if (utilities_full != utilities_total) and (st.error(' ')):
                st.error('Check total utilities expenses value is equal to full untilities value', icon="🚨")
                print (f"Utilities total and full", utilities_total, utilities_full)

            #TODO: Insert values in a database if there is no error in the values entered
            if st.error(' '):
                db.insert_period(period, incomes, expenses, groceries, car, utilities, comment)
            #st.write(f"Incomes: {incomes}")
            #st.write(f"Expenses: {expenses}")
                st.success("Data Saved!")


# Display the income and expenses     
if selected == 'Data Visualisation':
    # --- Plot Periods ---
    st.header("Data Visualisation")
    with st.form("Saved periods"):
        # TODO : Get periods from database
        period = st.selectbox("Select period :", get_all_periods())
        submitted = st.form_submit_button("Plot Period")
        if submitted:
            # TODO : Get data from database
            period_data = db.get_period(period)
            comment = period_data.get("comment")
            expenses = period_data.get("expenses")
            incomes = period_data.get("incomes")
            groceries = period_data.get("groceries")
            car = period_data.get("car")
            utilities = period_data.get("utilities")

            #Create metrics
            total_income = sum(incomes.values())
            total_expense = sum(expenses.values())
            remaining_budget = total_income - total_expense
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Income:", f"{total_income} {currency}")
            col2.metric("Total Expenses:", f"{total_expense} {currency}")
            col3.metric("Remaining amount:", f"{remaining_budget} {currency}")

            # Create Sankey Chart
            label = list(incomes.keys()) + ["Total Income"] + list(expenses.keys()) + \
                    list(groceries.keys()) + list(car.keys()) + list(utilities.keys())
                    
            source = list(range(len(incomes))) + [len(incomes)] * len(expenses) + \
                    [label.index('Groceries')] * len(groceries) + [label.index('Car')] * len(car) + \
                    [label.index('Utilities')] * len(utilities)
                    
                    
            target = [len(incomes)] * len(incomes) + [label.index(expense) for expense in expenses] + \
                [label.index(groceryitem) for groceryitem in groceries] + \
                [label.index(caritem) for caritem in car] + \
                [label.index(utility) for utility in utilities]
            
            value = list(incomes.values()) + list(expenses.values())  + list(groceries.values()) + list(car.values()) + list(utilities.values())                    
                    
            # Data to dictionary, dictionary to Sankey chart
            node = dict(label=label, pad=20, thickness=30, color =  ['rgba(255,0,255, 0.8)' \
                                if color_palet == "magenta" else color for color in color_palet])
            
            nodecolor =  ['rgba(255,0,255, 0.8)' if color_palet == "magenta" else \
                          color for color in color_palet]
            linkcolor = [nodecolor[src].replace("0.8", str(opacity)) for src in source]
                
            link = dict(source=source, target=target, value=value, color =  linkcolor )
                    
            data = go.Sankey(link=link, node=node)

            # Plot the data to a Sankey chart
            fig = go.Figure(data)
            fig.update_layout(title_text = f'Income and expenses Sankey chart for period {period}', \
                              title_x = 0.25)
            st.write(' ')
            fig.update_layout(margin=dict(l=0, r=0, t=25, b=5))
            st.plotly_chart(fig, use_container_width=True)

            # Plot expenses in a pie chart
            # creating a transposed data frame from expenses dictionary 
            expenses_df = pd.DataFrame([expenses.keys(), expenses.values()]).T
            expenses_df.columns= ['Expense category', 'Amount']  # renaming column name
            # Display expenses dataframe
            st.write(f'Expense data for period {period}')
            st.write(expenses_df)
            fig2 = px.pie(expenses_df, names = 'Expense category', values = 'Amount', hole = 0.6)
            fig2.update_traces(textinfo='percent + value')
            fig2.update_layout(title_text = f'Expense breakdown for period {period}', title_x = 0.25)
            fig2.update_layout(legend=dict(orientation='h',yanchor='bottom',  \
                                           xanchor='center', x=0.5))
            st.plotly_chart(fig2, use_container_width=True)

            # Plot grocery expenses in a pie chart
            # creating a transposed data frame from grocery expenses dictionary 
            groceries_df = pd.DataFrame([groceries.keys(), groceries.values()]).T
            groceries_df.columns= ['Grocery expense category', 'Amount']  # renaming column name
            # Display grocery expenses dataframe
            st.write(f'Grocery expense data for period {period}')
            st.write(groceries_df)
            fig3 = px.pie(groceries_df, names = 'Grocery expense category', values = 'Amount', hole = 0.6)
            fig3.update_traces(textinfo='percent + value')
            fig3.update_layout(title_text = f'Grocery expense breakdown for period {period}', title_x = 0.25)
            fig3.update_layout(legend=dict(orientation='h',yanchor='bottom',  \
                                           xanchor='center', x=0.5))
            st.plotly_chart(fig3, use_container_width=True)

            # Plot car expenses in a pie chart
            # creating a transposed data frame from car expenses dictionary 
            car_df = pd.DataFrame([car.keys(), car.values()]).T
            car_df.columns= ['Car expense category', 'Amount']  # renaming column name
            # Display car expenses dataframe
            st.write(f'Car expense data for period {period}')
            st.write(car_df)
            fig4 = px.pie(car_df, names = 'Car expense category', values = 'Amount', hole = 0.6)
            fig4.update_traces(textinfo='percent + value')
            fig4.update_layout(title_text = f'Car expense breakdown for period {period}', title_x = 0.25)
            fig4.update_layout(legend=dict(orientation='h',yanchor='bottom',  \
                                           xanchor='center', x=0.5))
            st.plotly_chart(fig4, use_container_width=True)

            # Plot utilities expenses in a pie chart
            # creating a transposed data frame from utilities expenses dictionary 
            utilities_df = pd.DataFrame([utilities.keys(), utilities.values()]).T
            utilities_df.columns= ['Utilities expense category', 'Amount']  # renaming column name
            # Display utilities expenses dataframe
            st.write(f'Utilities expense data for period {period}')
            st.write(utilities_df)
            fig5 = px.pie(utilities_df, names = 'Utilities expense category', values = 'Amount', hole = 0.6)
            fig5.update_traces(textinfo='percent + value')
            fig5.update_layout(title_text = f'utilities expense breakdown for period {period}', title_x = 0.25)
            fig5.update_layout(legend=dict(orientation='h',yanchor='bottom',  \
                                           xanchor='center', x=0.5))
            st.plotly_chart(fig5, use_container_width=True)