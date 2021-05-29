# Simple setup para FastAPI con Autenticación

![](https://magickode2publicmedia.s3.us-east-2.amazonaws.com/logo.png)


### Descripción del proyecto
Una base contruida en el framework  [FastAPI](https://fastapi.tiangolo.com/), implementando
autenticación Oauth2.
La conexión con base de datos se especifica en el directorio config, donde también 
se setea una database para testeos.
El proyecto base se conforma de dos apps , en los respectivos directorios users y cryptos.
La app Cryptos es una sencilla aplicacion para hacer consultas sobre unas pocas criptomonedas. Esta incorporada a modo el ejemplo y facilmente puedes eliminarla e iniciar tus propias aplicaciones, ya que esta totalmente desacoplada de users.


###Links
Puedes ver este proyecto live e interactuar con la documentación autogenerada por fastAPI:
[Documentacion](https://hb5vni.deta.dev/docs)

### Correr el proyecto

###Varaibles de entorno
Debes crear un archivo con variables de entorno (.env) que especifiquen los siguientes
dos campos, tu secretkey para encryptar y el algoritmo que prefieras, ejemplo:
1. .env
>SECRET_KEY=tuclavesecretaf0f4caa6cf63b88e8d3e7
>ALGORITHM=HS256


###Build & Run docker-compose
En el root directory del proyecto
```
sudo docker-compose build
sudo docker-compose up
```
####Listo!
Puedes ir a la documentacion interactiva en tu localhost: [http://localhost:8000/docs](http://localhost:8000/docs)
