#python
from typing import Optional
#typing opcional para tipado estático
#pydantic
from pydantic import BaseModel 
#clase BaseModel me ayuda a crear modelos
#fastapi
from fastapi import FastAPI
from fastapi import Body




app = FastAPI()
#operations get. traeme la informacion, 
# post te envio la informacion put actualizo lainformacion
#delete borro la informacion

#Models
#class <nombre del modelo>(<herencia. Basemodel>):
    #característicvas o atributos: <tipo de dato>

class Person(BaseModel):
    first_name: str
    last__name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None

class Pendulo(BaseModel):
    longitud_cuerda: float
    planeta: Optional[str] = None
    gravedad_planeta:float
    masa: Optional[int] = None
    amplitud: Optional[int] = None

@app.get("/")
def home():
    return {"Hello": "World"}

#request and response body

@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person

@app.post("/mas/pendulo")
def periodo(pendulo: Pendulo = Body(...)):
    return pendulo

"""@app.get("/mas/pendulo/periodo/?longitud=2")
def periodo_pendulo():
    periodo = longitud * 2
    return {"periodo": "periodo"}"""
#path parameter--una variable dentro de un path es obligatorio 
# pasarlo se define con llaves. parametro que yo puedo enviar 
# de manera obligatoria a cuaquier endpoint de mi api

#query Parameters: un parametro opcional estops parametros
#se ponen despues de ? y &. ? simbolo que permite saber donde
#  comieza el query parameter.
#_________________________________________________
#Modelos: representación de una entidad de manera descriptiva
# un request body es un parametro de la path operation function