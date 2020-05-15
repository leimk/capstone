from flask import Flask, request 
import sqlite3
import pandas as pd
conn = sqlite3.connect("data/chinook.db")
sqlStat_salesByMonth = "SELECT * FROM INVOICES order by invoiceDate"
sales_df = pd.read_sql_query(sqlStat_salesByMonth, conn,parse_dates='InvoiceDate')
app = Flask(__name__) 

@app.route('/sale/byMonth')
def sales():
	sales_df['bulan'] = sales_df['InvoiceDate'].dt.month_name()
	salesByMonth = sales_df.groupby('bulan').sum()
	salesbyMonthdf = pd.DataFrame(salesByMonth,columns=['Total'])
	
	return salesbyMonthdf.to_json()

if __name__ == '__main__':
    app.run(debug=True, port=5000)