from distutils.log import debug
from tkinter.ttk import Style
from click import style
from flask import Flask, render_template


app = Flask(__name__) #instancia python.

@app.get("/")  #funcion decoradora crea una ruta.
def index():    
    return render_template("index.html")

@app.get("/contacto")
def contacto():
    return render_template("contacto/index.html")

@app.get("/contacto/<contactoId>/edit")
def editarcontacto(contactoId):
    suma = 2+2
    return render_template("contacto/editar.html",
                           contactoId = contactoId, 
                           suma = suma)
    

@app.get("/contacto/<int:edadP>/edad")
def edadpersona(edadP):
    
    return render_template("contacto/edad.html",
                           edadP = edadP) 

app.run(debug=True)

