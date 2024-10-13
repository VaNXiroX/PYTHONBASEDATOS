# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 18:18:06 2024

@author: VaNXiroX
"""

import tkinter as tk
from tkinter import messagebox
import re
import csv
import mysql.connector

def insertarRegistro(nombres, apellidos, edad, estatura, telefono, genero):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            port=3306,  # Cambiado a entero
            user="root",
            password="1234",
            database="new_schema1"
        )
        cursor = conexion.cursor()

        query = "INSERT INTO REGISTROS (nombres, apellidos, edad, estatura, telefono, genero) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (nombres, apellidos, edad, estatura, telefono, genero)
        
        cursor.execute(query, valores)
        conexion.commit()
        messagebox.showinfo("informacion", "Datos guardados en la base de datos con éxito")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al insertar los datos: {err}")
        print(f"Error MySQL: {err}")  # Agrega más detalles al mensaje de error

    except Exception as e:
        messagebox.showerror("Error", f"Error inesperado: {e}")
        print(f"Error inesperado: {e}")  # Captura otros posibles errores inesperados

    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

def limpiar_campos():
    tbNombre.delete(0, tk.END)
    tbApellidos.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    var_genero.set(0)  

def borrar_fun():
    limpiar_campos()

def validar_telefono(valor):
    return valor.isdigit() and len(valor) == 10

def validar_texto(valor):
    return bool(re.match("^[a-zA-Z\s]+$", valor))

def validar_altura(valor):
    try:
        return 0.5 <= float(valor) <= 2.5
    except ValueError:
        return False

def validar_edad(valor):
    return valor.isdigit() and 1 <= int(valor) <= 120 



def guardar_valores():
   
    nombres = tbNombre.get()
    apellidos = tbApellidos.get()
    edad = tbEdad.get()
    estatura = tbEstatura.get()
    telefono = tbTelefono.get()
   

    
    genero = ""
    if var_genero.get() ==" 1":
        genero = "Hombre"
    elif var_genero.get() == "2":
        genero = "Mujer"
    elif var_genero.get()== "3":
        genero = "Helicoptero_apache"
        
    if (validar_edad(edad) and validar_altura(estatura) and validar_telefono(telefono) and validar_texto(nombres) and validar_texto(apellidos) ):
    
       datos = f"Nombres: {nombres}\nEdad: {edad} años\nEstatura: {estatura}\nTeléfono: {telefono}\nGénero: {genero}\n"
              
    nombre_archivo = "Datos_Registro.csv"
    with open(nombre_archivo, mode="a", newline='') as archivo_csv:
      escritor_csv = csv.writer(archivo_csv)    
      insertarRegistro(nombres, apellidos, edad, estatura, telefono, genero)
      escritor_csv.writerow([nombres, apellidos, edad, estatura, telefono, genero])

    
    with open("302024Datos.txt", "a") as archivo:
        archivo.write(datos + "\n\n")
    messagebox.showinfo("Información", "Datos guardados con éxito: \n\n" + datos)
    
    limpiar_campos()


ventana = tk.Tk()
ventana.geometry("520x500")
ventana.title("Formulario Vr.01")


var_genero = tk.IntVar()


lbNombre = tk.Label(ventana, text="Nombres:")
lbNombre.pack()
tbNombre = tk.Entry(ventana)
tbNombre.pack()

lbApellidos = tk.Label(ventana, text="Apellidos:")
lbApellidos.pack()
tbApellidos = tk.Entry(ventana)
tbApellidos.pack()

lbTelefono = tk.Label(ventana, text="Teléfono:")
lbTelefono.pack()
tbTelefono = tk.Entry(ventana)
tbTelefono.pack()

lbEdad = tk.Label(ventana, text="Edad:")
lbEdad.pack()
tbEdad = tk.Entry(ventana)
tbEdad.pack()

lbEstatura = tk.Label(ventana, text="Estatura:")
lbEstatura.pack()
tbEstatura = tk.Entry(ventana)
tbEstatura.pack()

lbGenero = tk.Label(ventana, text="Género")
lbGenero.pack()

rbHombre = tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value=1)
rbHombre.pack()

rbMujer = tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value=2)
rbMujer.pack()

rbHelicoptero_apache = tk.Radiobutton(ventana, text="Helicoptero Apache", variable=var_genero, value=3)
rbHelicoptero_apache.pack()

btnBorrar = tk.Button(ventana, text="Borrar valores", command=borrar_fun)
btnBorrar.pack()

btnGuardar = tk.Button(ventana, text="Guardar", command=guardar_valores)
btnGuardar.pack()


ventana.mainloop()




