from flask import Flask, request,jsonify
from flask_api import status 
from werkzeug.http import HTTP_STATUS_CODES
# from swagger_ui import flask_api_doc
# api_doc(app, config_path='./config/test.yaml', url_prefix='/api/doc', title='API doc')
import sqlite3
# import requests
import pandas as pd
# conn = sqlite3.connect("data/chinook.db")

# def error_response(status_code,message=None):
# 	payload = {'error', HTTP_STATUS_CODES.get(status_code, 'Unknown Error')}
# 	if message:
# 		payload['message'] = message
# 	response = jsonify(payload)
# 	response.status_code = status_code
# 	return response

app = Flask(__name__) 

@app.route('/sale/by/<choice>/<waktu>',methods=['GET'])
def sales(choice):
	if(choice == 'bulan') :
		# /sales/by/bulan
		conn = sqlite3.connect("data/chinook.db")
		sqlStat_salesByMonth = "SELECT * FROM INVOICES order by invoiceDate"
		sales_df = pd.read_sql_query(sqlStat_salesByMonth, conn,parse_dates='InvoiceDate')
		sales_df['bulan'] = sales_df['InvoiceDate'].dt.month_name()
		salesByMonth = sales_df.groupby('bulan').sum()
		salesbyMonthdf = pd.DataFrame(salesByMonth,columns=['Total'])
		
		return salesbyMonthdf.to_json()
	elif (choice == 'kuartal'):
		# /sales/by/kuartal
		conn = sqlite3.connect("data/chinook.db")
		sqlStat_salesByQ = "SELECT * FROM INVOICES order by invoiceDate"
		salesByQ = pd.read_sql_query(sqlStat_salesByQ,conn,parse_dates='InvoiceDate')
		salesByQ['quarter']  = salesByQ['InvoiceDate'].dt.quarter
		salesByQ = salesByQ.groupby('quarter').sum()
		salesByQ_df = pd.DataFrame(salesByQ,columns=['Total'])
		return salesByQ_df.to_json()
	
	elif (choice == 'tahun'):
		# /sales/by/tahun
		conn = sqlite3.connect('data/chinook.db')
		sqlStat_salesByYear="SELECT * FROM INVOICES ORDER BY InvoiceDate"
		salesByYr = pd.read_sql_query(sqlStat_salesByYear,conn,parse_dates='InvoiceDate')
		salesByYr['tahun'] = salesByYr['InvoiceDate'].dt.year
		salesByYr = salesByYr.groupby('tahun').sum()
		salesByYr_df = pd.DataFrame(salesByYr,columns=['Total'])

		return salesByYr_df.to_json()

	elif (choice == 'negara'):
		# /sales/by/tahun
		conn = sqlite3.connect('data/chinook.db')
		sqlStat_salesByYear="SELECT * FROM INVOICES ORDER BY InvoiceDate"
		salesByCountry = pd.read_sql_query(sqlStat_salesByYear,conn,parse_dates='InvoiceDate')
		salesByCountry['tahun'] = salesByCountry['InvoiceDate'].dt.year
		salesByCountry = salesByCountry.groupby('Country').sum()
		salesByYr_df = pd.DataFrame(salesByYr,columns=['Total'])

		return salesByYr_df.to_json()

	else:
		return
		{'status_code' : 404,
		 'message' : 'Path Not Found'		
		}
@app.route('/top/<pilih>',methods=['GET'])
def ranking(pilih):
	if(pilih == 'customer'):
		# /top/customer
		conn = sqlite3.connect('data/chinook.db')
		sql = """
				SELECT c.customerId,c.FirstName || ' ' || c.LastName as NamaCustomer, sum(i.Total) as Sales from INVOICES i \
					join customers c on i.customerId = c.customerId group by c.customerId order by sum(i.Total) desc limit 10"""
		hasil = pd.read_sql_query(sql,conn)
		hasil_df = pd.DataFrame(hasil,columns=['NamaCustomer','Sales'])

		return hasil_df.to_json()	
		

	

if __name__ == '__main__':
    app.run(debug=False, port=5000)