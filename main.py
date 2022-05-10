from fastapi import FastAPI

app = FastAPI()
#operations get. traeme la informacion, 
# post te envio la informacion put actualizo lainformacion
#delete borro la informacion
@app.get("/")
def home():
    return {"Hello": "World"}

@app.post("/person")
def datos_personales():
    pass

#path parameter--una variable dentro de un path es obligatorio 
# pasarlo se define con llaves. parametro que yo puedo enviar 
# de manera obligatoria a cuaquier endpoint de mi api

#query Parameters: un parametro opcional estops parametros
#se ponen despues de ? y &. ? simbolo que permite saber donde
#  comieza el query parameter.

