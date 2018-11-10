#!/usr/bin/python
from flask import Flask, jsonify, abort, make_response, request, render_template
import pandas as pd
import io
import matplotlib.pyplot as plt
import base64

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
	fieldArrays = field.split(",")
	data = {}
	for indexFieldArray in fieldArrays:
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
	groupByArray = groupBy.split(",")
	data = {}
	data.update({'mean':df.groupby(groupByArray)[field].mean()})
	data.update({'min':df.groupby(groupByArray)[field].min()})
	data.update({'max':df.groupby(groupByArray)[field].max()})
	data.update({'median':df.groupby(groupByArray)[field].median()})
	return str(data)

@app.route('/fig')
def fig():
	groupBy = request.args.get('groupBy',default = 'year')
	field = request.args.get('field',default = 'pop')
	groupByArray = groupBy.split(",")
	ax = df.groupby(groupByArray)[field].mean().plot(kind='bar', figsize=(15, 10), fontsize=12)
	img = io.BytesIO()
	plt.savefig(img,format='png')
	img.seek(0)
	plot_url = base64.b64encode(img.getvalue()).decode()
	return render_template('test.html',plot_url=plot_url)

if __name__ == '__main__':
    df = pd.read_csv('/myapp/gapminder.tsv', sep='\t')
    app.run(host='0.0.0.0',debug=True)
