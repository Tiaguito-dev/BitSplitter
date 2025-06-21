import sys # Importar sys para manipular el path
import os # Importar os para manipular rutas de archivos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from BACKEND import shannon  # Importar las constantes desde el módulo de constantes
import tkinter as tk

# -- CREACIÓN DE LA VENTANA PRINCIPAL --
ventana = tk.Tk() # Creo la ventana principal aquí para evitar importaciones circulares y errores de referencia

# -- MANEJO DEL STRINGVAR --
# Crea una variable de tipo cadena vinculada a la interfaz, útil para actualizar textos dinámicamente
palabra = tk.StringVar(ventana) # Esta es la palabra que ingresará el usuario
codigo = tk.StringVar(ventana) # Esta es la variable que contendrá el código generado por el algoritmo de Shannon

def guardar_palabra(entrada):
    # TO DO Validar la entrada del usuario antes de guardarla
    # A mi me gustaría que se validara la entrada acá en vez de en el backend para tratarlo directamente, pero hay que migrar el código de shannon.py a un módulo separado para evitar circular imports.

    # Esta función se ejecuta al hacer clic en el botón
    # Actualiza el valor de la variable palabra con el texto ingresado en la entrada de texto
    palabra.set(entrada)  # Actualiza la variable palabra con el texto ingresado en la entrada de texto
    print("Palabra guardada:", palabra.get())  # Imprime la palabra guardada en la consola

    #TO DO Pasar los parámetros y agregar la lógica para los strngVar y el botón de guardar
    codigo.set(shannon.main(palabra.get()))  # Actualiza la variable codigo con el código generado por el algoritmo de Shannon
    print("Código generado:", codigo.get())  # Imprime el código generado en la consola