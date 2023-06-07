import pandas as pd
import sqlite3

sales_data = {
    'SaleID': [1, 2, 3, 4, 5],
    'ProductID': [101, 102, 103, 101, 104],
    'CustomerID': [1, 2, 3, 1, 4],
    'DateID': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-03', '2023-01-03'],
    'QuantitySold': [5, 3, 2, 7, 4],
    'SalesAmount': [100, 50, 75, 120, 80]
}

# Convert the dictionary to a Pandas DataFrame
df_sales = pd.DataFrame(sales_data)

df_product = pd.DataFrame({
    'ProductID': [101, 102, 103, 104],
    'ProductName': ['Product A', 'Product B', 'Product C', 'Product D'],
    'Category': ['Category X', 'Category Y', 'Category X', 'Category Z'],
    'Brand': ['Brand 1', 'Brand 2', 'Brand 1', 'Brand 3'],
    'Price': [20, 15, 25, 30]
})

df_customer = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4],
    'CustomerName': ['John', 'Jane', 'David', 'Emily'],
    'Address': ['Address 1', 'Address 2', 'Address 3', 'Address 4'],
    'Age': [25, 35, 30, 40],
    'Gender': ['Male', 'Female', 'Male', 'Female']
})

df_date = pd.DataFrame({
    'DateID': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'Date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']),
    'DayOfWeek': ['Monday', 'Tuesday', 'Wednesday'],
    'Month': ['January', 'January', 'January'],
    'Year': [2023, 2023, 2023],
    'Quarter': [1, 1, 1]
})

conn = sqlite3.connect('sales.db')

df_sales.to_sql('sales', conn, index=False, if_exists='replace')
df_product.to_sql('product', conn, index=False, if_exists='replace')
df_customer.to_sql('customer', conn, index=False, if_exists='replace')
df_date.to_sql('date', conn, index=False, if_exists='replace')

query = '''
SELECT p.Category, d.Month, SUM(s.SalesAmount) AS TotalSales
FROM sales s
JOIN product p ON s.ProductID = p.ProductID
JOIN date d ON s.DateID = d.DateID
GROUP BY p.Category, d.Month
'''

df_analysis = pd.read_sql_query(query,
