#!/usr/bin/python
from flask import Flask, jsonify, abort, make_response, request
import pandas as pd

app = Flask(__name__)
df = None
url = None

@app.route('/')
def index():
	global df
	return str(df.shape)

@app.route('/getAggregationsByFields', methods = ['POST'])
def getAggregationsByFields():
	global df
	field = request.json.get('field',"")
	data = {}
	for indexFieldArray in fieldArray:
		data.update({'mean'+indexFieldArray:df[indexFieldArray].mean()})
		data.update({'min'+indexFieldArray:df[indexFieldArray].min()})
		data.update({'max'+indexFieldArray:df[indexFieldArray].max()})
		data.update({'median'+indexFieldArray:df[indexFieldArray].median()})
	return str(data)

@app.route("/encabezado", methods = [ 'GET' ])
def encabezado():
	global df
	return str(df.columns)

@app.route("/imprimirtipos", methods = ['GET'])
def imprimirtipos():
	global df
	return str(df.dtypes)

@app.route('/seturl', methods = ['POST'])
def seturl():
	global url
	global df
	url = request.json.get('url',"")
	c = request.json.get('sep',"\t")
	print("Nuevo url %s separador %s\n"%(url,c))
	df = pd.read_csv(url,sep=c)
	return "OK"

@app.route('/getGroupByAggregationsByFields', methods = ['POST'])
def getGroupByAggregationsByFields():
	global df
	field = request.json.get('field',"")
	groupBy = request.json.get('groupBy',"")
	data = {}
	data.update({'mean':df.groupby(groupBy)[field].mean()})
	data.update({'min':df.groupby(groupBy)[field].min()})
	data.update({'max':df.groupby(groupBy)[field].max()})
	data.update({'median':df.groupby(groupBy)[field].median()})
	return str(data)

if __name__ == '__main__':
    df = pd.read_csv('/myapp/gapminder.tsv', sep='\t')
    app.run(host='0.0.0.0',debug=True)
