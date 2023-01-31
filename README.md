# acme
- [Introducción](#introducción)
  - [Proyecto](#proyecto)
    - queries.py
    - query_utils.py   
  - [Ampliaciones] (#ampliaciones)
    - test_queries.py
    - frontend
- [Documentación](#documentación)

# Introducción

He decidido realizar la prueba en Python, debido a que es un lenguaje muy extendido ahora mismo, con mucha documentación y con el que he trabajado bastante últimamente.

Para poder trabajar cómodamente com archivos .csv, he trabajado con la librería **csv**, con la que se puede realizar cómodamente la lectura y escritura en este tipo de archivos. 
 
## Proyecto

El esquema de carpetas y los archivos realizados es el siguiente:

- acme
  - csv
    - customers.csv
    - orders.csv
    - products.csv
  - results
    - customer_ranking.csv
    - order_prices.csv
    - product_customers.csv
  - frontend
    - index-html
  - queries.py
  - query_utils.py
  - test_queries.py
  - server.py
 
 Dónde en la carpeta **csv** están los archivos proporcionados para realizar las consultas, y en **results** se encuentran los archivos .csv obtenidos después de la realización de las mismas. 

### queries.py

En este script es donde se he realizado las tres consultas solicitadas.

He realizado tres métodos, uno para cada consulta, con un esquema básico de abrir los archivos .csv necesarios, crear un archivo .csv para escribir en él, realizar la consulta y introducir los datos.

Los archivos generados en estas consultas se guardan en la carpeta **results** como he comentado anteriormente.

Este archivo también se puede ejecutar desde el terminal con:

python .\queries.py

Donde saldrá un menú para seleccionar la consulta que queramos generar.

### query_utils.py

En este script he realizado dos métodos auxiliares para la realización de las consultas.

#### from_list_of_dict_to_dict (list_of_dict, primary_key='id')

Este método sirve para convertir una lista de diccionarios en un diccionario de diccionarios con la clave de 'id' de forma predeterminada. Se utiliza en las consultas cuando se está leyendo un archivo .csv, para poder acceder a los datos más fácilmente. 

#### total_price_orders (order_string, products_by_id)

Este método sirve para cálcular el total de un pedido, recibiendo como argumentos un string con el pedido, y un diccionario de los productos que forman ese pedido. Se ha realizado debido a que este dato se necesita en dos de las consultas.

## Proyecto

### test_queries.py

Este script se ha utilizado para comprobar que los métodos auxiliares que se han realizado funcionan correctamente. He utilizado la libreria **unittest**.

Para ejecutar el test se realiza desde el terminal en la carpeta del proyecto con:

python .\test_queries.py

Si se desea realizar con verbosidad para recibir más información:

python .\test_queries.py -v

### Frontend

He realizado un pequeño servidor para generar un html y controlar las peticiones de la descarga
de los elementos.

En la carpeta de frontend se encuentra el archivo index.html, que contiene el css y el JavaScript
necesarios para el correcto funcionamiento de la página. Soy consciente de que no es la mejor práctica
que estos dos elementos se encuentren dentro del archivo html, pero al llamarlo desde el servidor
estos no se indexaban correctamente. 

Para su funcionamiento simplemente se debe llamar al server desde el terminal:

python .\server.py

y posteriormente, abrir en un navegador la ruta:

http://localhost:8080/

De esto modo, ya se podrá visualizar el contenido del frontend, y al pulsar en el botón correspondiente
para cada consulta, se descargará el archivo .csv

# Documentación

* https://docs.python.org/3/library/csv.html

* https://docs.python.org/3/library/unittest.html#test-cases

* https://docs.python.org/3/library/http.server.html

* https://plainenglish.io/blog/how-to-download-a-file-using-javascript-fec4685c0a22
