import tkinter as tk

# -- CREACIÓN DE LA VENTANA PRINCIPAL --
ventana = tk.Tk() # Creo la ventana principal aquí para evitar importaciones circulares y errores de referencia

# -- MANEJO DEL STRINGVAR --
# Crea una variable de tipo cadena vinculada a la interfaz, útil para actualizar textos dinámicamente
palabra = tk.StringVar(ventana) # Esta es la palabra que ingresará el usuario
codigo = tk.StringVar(ventana) # Esta es la variable que contendrá el código generado por el algoritmo de Shannon
entropia = tk.DoubleVar(ventana)
longitud_promedio = tk.DoubleVar(ventana)
eficiencia_shannon = tk.DoubleVar(ventana)
eficiencia_huffman = tk.DoubleVar(ventana)