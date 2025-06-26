import sys # Importar sys para manipular el path
import os # Importar os para manipular rutas de archivos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DATABASE import registros  # Importar las constantes desde el módulo de constantes
from BACKEND import shannon # Importar el módulo de codificación Shannon-Fano
import tkinter as tk
import string # ofrece listas útiles como string.printable, que usamos para filtrar caracteres válidos.

from collections import Counter #Usamos funcion Counter de la libreria collection para contar fácilmente cuántas veces aparece cada carácter en el texto.
import math #se usa para calcular logaritmos (para la entropía).

# -- MÓDULO DE MANEJO DE ENTRADAS Y CODIFICACIÓN --
palabra = registros.palabra  # Rescato la variable palabra del módulo de registros
codigo = registros.codigo  # Rescato la variable codigo del módulo de registros

# Esta función se encarga de limpiar el texto de caracteres no imprimibles o invisibles.
def limpiar_texto(texto, permitidos=None): #Permite evitar contar caracteres invisibles (como \n, \x00, etc.) que pueden distorsionar las frecuencias.
    if permitidos is None: #Filtra el texto para contar solo caracteres permitidos. Por defecto permite todos los caracteres imprimibles.
        permitidos = set(string.printable)  
    return ''.join(c for c in texto if c in permitidos)

# -- PROGRAMA PRINCIPAL PARA CODIFICAR --
def activar_shannon(entrada):
    # Antes de guardar la entrada, se limpia el texto para evitar errores de codificación con caracteres raros.
    entrada_limpia = limpiar_texto(entrada)  # Limpia la entrada de caracteres no imprimibles

    if not entrada_limpia:  # Si la entrada está vacía después de limpiar, se cancela la operación.
        print("La entrada está vacía o contiene solo caracteres no imprimibles.")
        exit()  # Termina el programa si no hay texto válido para codificar.
        # TODO NO TIENE QUE TERMINAR EN REALIDAD, DEBERÍA DAR UN MENSAJE AL USUARIO Y VOLVER A PEDIR LA ENTRADA.

    # Guarda la entrada limpia y el código generado en las variables de la BD
    palabra.set(entrada_limpia)  # Guarda la entrada en la BD
    codigo.set(shannon.codificar(palabra.get()))  # Codifica la palabra usando el algoritmo de Shannon-Fano y guarda el resultado en la BD

    # Obtengo el resto de las estadísticas del código generado
    # Impresión de estadísticas en la consola
    print("Palabra para codificar:", palabra.get())  # Imprime la palabra a codificar en la consola
    print("Código generado:", codigo.get())  # Imprime el código generado en la consola
    entropia = shannon.getEntropia()
    print(f"\nEntropía H(X): {entropia:.4f} bits")
    longitud_promedio = shannon.getLongitudPromedio()
    print(f"Longitud promedio del código: {longitud_promedio:.4f} bits/símbolo")
    eficiencia = shannon.getEficiencia()
    print(f"Eficiencia del código: {eficiencia:.2f} %")

    # TODO Hay que ver cómo le paso esto a mariano
    frecuencias = shannon.getFrecuencias()
    probabilidades = shannon.getProbabilidades()
    diccionario_codigos = shannon.getDiccionario_codigos()

    for char in sorted(probabilidades, key=probabilidades.get, reverse=True):
        print(f"{repr(char):^8} | {frecuencias[char]:^10} | {probabilidades[char]:^12.4f} | {diccionario_codigos[char]:^19}")


    return codigo.get()  # Devuelve el código generado para su uso posterior