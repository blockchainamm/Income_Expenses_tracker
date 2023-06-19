# Income Expenses tracker
This application is an income expenses tracker along with sankey chart to give insights into the flow of expenses

This web application is divided into two main parts
- Data Entry : This page permits the user to input the data for income and expenses categories
- Data Visualization : This page is used display the income and expense by means of a Sankey chart

## **Data Entry section**

The income category is subdivided into different specific items

The expenses category is subdivided into specific items.

A comment items allows the user to enter a comment associated with the enetered income and expenses.
For certain categories of expenses, the details are further subdivided into corresponding associated items.

Once the data in both income and expense categories are entered and upon clicking of the SUBMIT button the entered values are created as a record in an NOSQL database. 

## **Data Visualisation section**

This section retrives the data of income and expenses for a specific month in a given year stored in an NOSQL database in Deta cloud.

From the data retrived for the chosen period of year and month, a Sankey chart is plotted which shows the flow of distribution of each expenses from the income source.

Some donut charts are displayed to further give a breakdown of expenses

### Sample of Sankey chart
![Sankey chart](https://github.com/blockchainamm/Income_Expenses_tracker/assets/82846751/0a2ab904-6694-4d63-8184-2a2a40cbd880)

### Sample of donut chart
![Donut chart](https://github.com/blockchainamm/Income_Expenses_tracker/assets/82846751/409b9354-8b88-402c-a17f-5df3446768d8)
