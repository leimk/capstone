from flask import Flask, request 
# from swagger_ui import flask_api_doc
# api_doc(app, config_path='./config/test.yaml', url_prefix='/api/doc', title='API doc')
import sqlite3
import requests
import pandas as pd
# conn = sqlite3.connect("data/chinook.db")

app = Flask(__name__) 

@app.route('/sale/by/<choice>',methods=['GET'])
def sales(choice):
	if(choice == 'bulan') :
		conn = sqlite3.connect("data/chinook.db")
		sqlStat_salesByMonth = "SELECT * FROM INVOICES order by invoiceDate"
		sales_df = pd.read_sql_query(sqlStat_salesByMonth, conn,parse_dates='InvoiceDate')
		sales_df['bulan'] = sales_df['InvoiceDate'].dt.month_name()
		salesByMonth = sales_df.groupby('bulan').sum()
		salesbyMonthdf = pd.DataFrame(salesByMonth,columns=['Total'])
		
		return salesbyMonthdf.to_json()
	elif (choice == 'kuartal'):
		conn = sqlite3.connect("data/chinook.db")
		sqlStat_salesByQ = "SELECT * FROM INVOICES order by invoiceDate"
		salesByQ = pd.read_sql_query(sqlStat_salesByQ,conn,parse_dates='InvoiceDate')
		salesByQ['quarter']  = salesByQ['InvoiceDate'].dt.quarter
		salesByQ = salesByQ.groupby('quarter').sum()
		salesByQ_df = pd.DataFrame(salesByQ,columns=['Total'])
		return salesByQ_df.to_json()

if __name__ == '__main__':
    app.run(debug=True, port=5000)