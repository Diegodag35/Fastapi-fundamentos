#python
from typing import Optional
#typing opcional para tipado estático
#pydantic
from pydantic import BaseModel 
#clase BaseModel me ayuda a crear modelos
#fastapi
from fastapi import FastAPI, Query
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

#validaciones query parameters

@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(None, min_length=1, max_length=50),
    age: Optional[int] = Query(...)
):

    return {name: age}


@app.post("/mas/pendulo")
def periodo(pendulo: Pendulo = Body(...)):
    return pendulo

@app.get("/mas/pendulo/periodo/details")
def periodo_pendulo(
    longitud: Optional[float] = Query(
        ...,
        gt=0,
        lt=100,
        title="Longitud para determinar el periodo de un pendulo",
        description="longitud de la cuerda"
        ),
    masa: Optional[float] =Query(
        None,
        )
    
):
    return {longitud: masa}

#path parameter--una variable dentro de un path es obligatorio 
# pasarlo se define con llaves. parametro que yo puedo enviar 
# de manera obligatoria a cuaquier endpoint de mi api

#query Parameters: un parametro opcional estops parametros
#se ponen despues de ? y &. ? simbolo que permite saber donde
#  comieza el query parameter.
#_________________________________________________
#Modelos: representación de una entidad de manera descriptiva
# un request body es un parametro de la path operation function