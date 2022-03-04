
from sqlite3 import Cursor
from flask import Flask, render_template, request, redirect, url_for

import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user="root",
    password="",
    database="producto",
    port="3306"
)
db.autocommit = True





app = Flask(__name__) #instancia python.

@app.get("/crear")
def crearProducto():
    return render_template("crear.html")

@app.post("/crear")
def crearProductoPost():
    nombre = request.form.get('nombre')
    precio = request.form.get('precio')
    
    cursor = db.cursor()
    cursor.execute("INSERT INTO producto(nombre,precio) VALUES (%s,%s)",(
        nombre,
        precio
    ))
    
    cursor.close()
    return redirect(url_for("index"))


@app.get("/")  #funcion decoradora crea una ruta.
def index():    
    
    #abrir cursos para hacer una conexion y llamar base de datos, dictionary para poder leer los datos
    cursor=db.cursor(dictionary=True)
    cursor.execute("select * from producto")
    
    
    productos=cursor.fetchall() # optener todos los productos
    
    #producto = cursor.fetchone() optine el primer producti
    
    # print(productos[0]["nombre"]) mostrar datos en consola
    cursor.close()
    return render_template("index.html",productos=productos)


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

