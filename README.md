# Web de películas creada con Django
## Proyecto final coderhouse 

Esta es la primera entrega del proyecto final de CoderHouse del curso de programación en Python. 

El equipo de trabajo está conformado por **Adrián Santander Ibarra** y **Agustina López Tejera**. 

A partir de nuestros intereses en común decidimos crear una plataforma de alquiler de series y películas con una sección para dejar reseñas.  

Comenzamos creando un repositorio colaborativo en github. 
Creamos una app para cada función de nuestra plataforma, tenemos una app de *películas*, una para *series*, y una para *reseñas*. En cada una de las apps creamos un modelo con los campos que debe tener cada serie, película o reseña. Estos campos se ingresan mediante un formulario. Además se pueden visualizar las series, películas y reseñas en listas.
Para navegar a través de la plataforma incluímos una barra de navegación, un footer y una barra de búsqueda. Estos son heredados por todos los templates. 

Pasos para correr el código:
1) Colocarse en el directorio raiz.
2) Desde consola ejecutar el comando ``python manage.py runserver``
3) Ir a la ruta localhost en el navegador, por ejemplo http://127.0.0.1:8000/

Se puede navegar libremente entre las vistas y la función busqueda del navbar nos permite encontrar cualquier pelicula, serie o Review. Además, contamos con 3 opciones distintas en el navbar para realizar un registro nuevo desde el form correspondiente.


### Vista filsm
![vista films](https://user-images.githubusercontent.com/35971687/183787566-54a8c649-27a1-4512-b86a-18991d61cad6.png)

### Vista Series
![vista series](https://user-images.githubusercontent.com/35971687/183787646-fff0173f-6da9-437e-95ce-b3bf40e13425.png)

### Vista Reviews
![vista reviews](https://user-images.githubusercontent.com/35971687/183787652-6dbdfe32-6101-4846-94fc-04a46037687b.png)

### Vista form
![form](https://user-images.githubusercontent.com/35971687/183787696-bcb29dde-6420-43bf-a698-7d8b93c4a6c8.png)

