# proyecto-cloud

## Introduccion

Este proyecto realiza las siguientes funcionalidades:

	•	Cargar datos en formato CSV o TSV desde un URL.
	•	Consultar el número de filas y columnas que tienen esos datos.
	•	Mostrar el nombre de los atributos de los datos.
	•	Mostrar el tipo de datos de los atributos.
	•	Permite calcular funciones de agregación (media, mediana, mayor, menor) sobre al menos un dato. Dos o más datos a la vez. 
	•	Permite la agrupación de una columna o más y con los datos agrupados aplicar una función de agregación.
	•	Permite graficar dados unos datos. 
  
  ## Url disponibles 
  
  [/](http://localhost:5000/) Consultar el número de filas y columnas que tienen esos datos
```
curl -i http://localhost:5000
```

* [/encabezado](http://localhost:5000/encabezado) este URI permite ver los nombres de los atributos del *dataframe*.
```
curl -i http://localhost:5000/encabezado
```
* [/imprimirtipos](http://localhost:5000/imprimirtipos) este URI permite conocer el tipo de los datos de los atributos del *dataframe*.
```
curl -i http://localhost:5000/imprimirtipos
```
* [/seturl](http://localhost:5000/seturl) este URI permite acceder a un archivo CSV o TSV que se encuentre accesible a traves de Internet
```
curl -i -H "Content-Type: application/json" -X POST -d '{ "url": "https://raw.githubusercontent.com/jennybc/gapminder/master/inst/extdata/gapminder.tsv", "sep": "\t"}' http://localhost:5000/seturl
```
* [/getGroupByAggregationsByFields](http://localhost:5000/getGroupByAggregationsByFields) este URI permite  la agrupacion de una columna o más y con los datos agrupados aplicar una función de agregación *dataframe*. 
El acceso a este *end-point* se hace a traves del metodo POST de la siguiente manera.
```
curl -i -H "Content-Type: application/json" -X POST -d '{ "field": "pop" , "groupBy":"continent"}' http://localhost:5000/getGroupByAggregationsByFields
curl -i -H "Content-Type: application/json" -X POST -d '{ "field": "pop" , "groupBy":"continent,year"}' http://localhost:5000/getGroupByAggregationsByFields
```
* [/getAggregationsByFields](http://localhost:5000/getAggregationsByFields) este URI permite calcular funciones de agregación (media, mediana, mayor, menor) sobre al menos un dato. Dos o más datos a la vez *dataframe*. 
El acceso a este *end-point* se hace a traves del metodo POST de la siguiente manera.
```
curl -i -H "Content-Type: application/json" -X POST -d '{ "field": "pop"}' http://localhost:5000/getAggregationsByFields
curl -i -H "Content-Type: application/json" -X POST -d '{ "field": "pop,year"}' http://localhost:5000/getAggregationsByFields
```

* [/fig](http://localhost:5000/fig) este URI permite graficar un par de datos y sacar el promedio  *dataframe*. 
El acceso a este *end-point* se hace a traves del metodo GET de la siguiente manera.
```
curl -i http://localhost:5000/fig?field=pop&groupBy=year,continent
```

