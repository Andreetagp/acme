# acme
- [Introducción](#introducción)
  - [Proyecto](#proyecto)
    - queries.py
    - query_utils.py
    - test_queries.py
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
  - queries.py
  - query_utils.py
  - test_queries.py
 
 Dónde en la carpeta **csv** están los archivos proporcionados para realizar las consultas, y en **results** se encuentran los archivos .csv obtenidos después de la realización de las mismas. 

### queries.py

En este script es donde se he realizado las tres consultas solicitadas.

He realizado tres métodos, uno para cada consulta, con un esquema básico de abrir los archivos .csv necesarios, crear un archivo .csv para escribir en él, realizar la consulta y introducir los datos.

Los archivos generados en estas consultas se guardan en la carpeta **results** como he comentado anteriormente. 

### query_utils.py

En este script he realizado dos métodos auxiliares para la realización de las consultas.

#### from_list_of_dict_to_dict (list_of_dict, primary_key='id')

Este método sirve para convertir una lista de diccionarios en un diccionario de diccionarios con la clave de 'id' de forma predeterminada. Se utiliza en las consultas cuando se está leyendo un archivo .csv, para poder acceder a los datos más fácilmente. 

#### total_price_orders (order_string, products_by_id)

Este método sirve para cálcular el total de un pedido, recibiendo como argumentos un string con el pedido, y un diccionario de los productos que forman ese pedido. Se ha realizado debido a que este dato se necesita en dos de las consultas.

### test_queries.py

Este script se ha utilizado para comprobar que los métodos auxiliares que se han realizado funcionan correctamente. He utilizado la libreria **unittest**.

Para ejecutar el test se realiza desde el terminal en la carpeta del proyecto con:

python .\test_queries.py

Si se desea realizar con verbosidad para recibir más información:

python .\test_queries.py -v

# Documentación

* https://docs.python.org/3/library/csv.html

* https://docs.python.org/3/library/unittest.html#test-cases
