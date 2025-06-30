import sys # Importar sys para manipular el path
import os # Importar os para manipular rutas de archivos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DATABASE import registros  # Importar las constantes desde el módulo de constantes
from BACKEND import shannon # Importar el módulo de codificación Shannon-Fano
from BACKEND import huffman # Importar el módulo de codificación Huffman
import tkinter as tk
import string # ofrece listas útiles como string.printable, que usamos para filtrar caracteres válidos.

from collections import Counter #Usamos funcion Counter de la libreria collection para contar fácilmente cuántas veces aparece cada carácter en el texto.
import math #se usa para calcular logaritmos (para la entropía).

# -- MÓDULO DE MANEJO DE ENTRADAS Y CODIFICACIÓN --
texto = registros.palabra  # Rescato la variable palabra del módulo de registros
codigo = registros.codigo  # Rescato la variable codigo del módulo de registros
entropia = registros.entropia
longitud_promedio = registros.longitud_promedio
eficiencia_shannon= registros.eficiencia_shannon
eficiencia_huffman = registros.eficiencia_huffman

def limpiar_texto(texto, permitidos=None): #Permite evitar contar caracteres invisibles (como \n, \x00, etc.) que pueden distorsionar las frecuencias.
    if permitidos is None: #Filtra el texto para contar solo caracteres permitidos. Por defecto permite todos los caracteres imprimibles.
        permitidos = set(string.printable)  
    return ''.join(c for c in texto if c in permitidos)

def guardar_entrada(entrada):
    entrada_limpia = limpiar_texto(entrada)  # Limpia la entrada de caracteres no imprimibles

    if not entrada_limpia:  # Si la entrada está vacía después de limpiar, se cancela la operación.
        print("La entrada está vacía o contiene solo caracteres no imprimibles.")
        return False  # Termina el programa si no hay texto válido para codificar.
        # TODO NO TIENE QUE TERMINAR EN REALIDAD, DEBERÍA DAR UN MENSAJE AL USUARIO Y VOLVER A PEDIR LA ENTRADA.

    # Guarda en la BD
    texto.set(entrada_limpia.upper())
    print(entrada_limpia.upper())

# -- PROGRAMA PRINCIPAL PARA CODIFICAR --
def activar_shannon(entrada):

    guardar_entrada(entrada)  # Limpia y guarda la entrada en la BD

    if not texto.get():
        return False
    else:
        # Calcula en el main de shannon
        shannon.codificar(texto.get())
        
        # Guarda el resto de parámetros en la BD
        codigo.set(shannon.getTextoCodificado())
        entropia.set(round(shannon.getEntropia(), 4))                   # 4 decimales para entropia
        longitud_promedio.set(round(shannon.getLongitud_promedio(), 4)) # 4 decimales para longitud promeido
        eficiencia_shannon.set(round(shannon.getEficiencia(), 2))       # 2 decimales para eficiencia

        print("\n=== BIENVENIDO A SHANNON ===")
        print("Palabra para codificar:", texto.get())  # Imprime la entrada a codificar en la consola
        print("Código generado:", codigo.get())  # Imprime el código generado en la consola
        print("Entropia:", entropia.get())  # Imprime la entrada a codificar en la consola
        print("Longitud Promedio:", longitud_promedio.get())  # Imprime el código generado en la consola
        print("Eficiencia:", eficiencia_shannon.get(), "%")  # Imprime el código generado en la consola

        return codigo.get()  # Devuelve el código generado para su uso posterior

def activar_huffman(entrada):
    
    print("\n=== BIENVENIDO A HUFFMAN ===")
    # Imprime todo en el algoritmo
    guardar_entrada(entrada)
    huffman.main(texto.get())

    # Guarda el resto de parámetros en la BD
    codigo.set(huffman.getTextoCodificado())
    entropia.set(round(huffman.getEntropia(), 4))                   # 4 decimales para entropia
    longitud_promedio.set(round(huffman.getLongitudPromedio(), 4)) # 4 decimales para longitud promeido
    eficiencia_huffman.set(round(huffman.getEficiencia(), 2))       # 2 decimales para eficiencia

    """
    print("Palabra para codificar:", texto.get())  # Imprime la entrada a codificar en la consola
    print("Código generado:", codigo.get())  # Imprime el código generado en la consola
    print("Entropia:", entropia.get())  # Imprime la entrada a codificar en la consola
    print("Longitud Promedio:", longitud_promedio.get())  # Imprime el código generado en la consola
    print("Eficiencia:", eficiencia_huffman.get(), "%")  # Imprime el código generado en la consola
    
    """

    return codigo.get()