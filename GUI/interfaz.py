import tkinter as tk
import customtkinter as ctk  # Importar customtkinter para widgets personalizados
from tkinter import filedialog
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from BACKEND import constantes, handler  # Importar las constantes desde el módulo de constantes
from DATABASE import registros  # Para importar la ventana
import visualizacion


"""
TODO 
REVISAR COMENTARIOS
REVISAR EL RESTO DE TO-DO
IMPRESIÓN DE MENSAJE DE ERROR
"""


# ---------- FUNCIONES PRINCIPALES ----------
# Esta función la va a llamar el handler cuando tenga haya procesado todos los resultados
def mostrar_resultados(eficiencia_shannon, entropia, longitud_promedio):

    resultado1= f"Eficiencia: {eficiencia_shannon}%"
    resultado2= f"Entropia: {entropia} bits/símbolo"
    resultado3= f"Longitud Promedio: {longitud_promedio} bits/símbolo"

    etiqueta_eficiencia.config(text=resultado1)
    etiqueta_entropia.config(text=resultado2)
    etiqueta_longitud_promedio.config(text=resultado3)

# Esta funcion muestra el codigo generado en el campo_texto
def mostrar_codigo(codigo):
    # Como el campo está bloqueado, primero lo desbloqueamos
    campo_texto.configure(state="normal")
    campo_texto.delete("1.0", "end")  # Borramos cualquier contenido previo
    campo_texto.insert("1.0", codigo)  # Ponemos el código generado ahí
    campo_texto.configure(state="disabled")  # Volvemos a bloquear para que no se edite


# Esta función se dispara cuando el usuario hace click en "Shannon"
def ejecutar_shannon(input):
    # Llama a tu handler que codifica el texto ingresado en shannon
    codigo = handler.activar_shannon(input)
    mostrar_codigo(codigo)
    mostrar_resultados(registros.eficiencia_shannon.get(), registros.entropia.get(), registros.longitud_promedio.get())

# Esta función se dispara cuando el usuario hace click en "Huffman"
def ejecutar_huffman(input):
    # Llama a tu handler que codifica el texto ingresado en huffman
    codigo = handler.activar_huffman(input)
    mostrar_codigo(codigo)
    mostrar_resultados(registros.eficiencia_huffman.get(), registros.entropia.get(), registros.longitud_promedio.get())
    

# Esta función limpia el campo donde se muestra el mensaje codificado
def limpiar_campo_texto():
    campo_texto.configure(state="normal")  # Lo desbloqueamos para poder borrar
    campo_texto.delete("1.0", "end")      # Borramos todo el contenido
    campo_texto.configure(state="disabled") # Lo bloqueamos otra vez para evitar cambios

def limpiar_input():
    texto_entrada.delete(0, tk.END)     # Limpiamos el campo de entrada

# Función para abrir el explorador y cargar un archivo de texto
def seleccionar_archivo():
    ruta_archivo = filedialog.askopenfilename(
        title="Selecciona un archivo",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    if ruta_archivo:
        print(f"Archivo seleccionado: {ruta_archivo}")
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
        print("Contenido del archivo:")
        print(contenido)
        limpiar_input()                         # Se limpia el espacio para ingresar texto
        texto_entrada.insert(0, contenido)     # Pegamos el texto que cargamos
        limpiar_campo_texto()                   # También limpiamos el campo que muestra código generado
    else:
        print("No se seleccionó ningún archivo.")

# Esta función se activa cuando se presiona al botón ejecutar
def ejecutar_grafica():
    handler.activar_huffman(texto_entrada.get())
    handler.activar_shannon(texto_entrada.get())
    eficiencia_shannon=registros.eficiencia_shannon.get()
    eficiencia_huffman=registros.eficiencia_huffman.get()
    visualizacion.abrir_ventana_grafico(ventana, eficiencia_shannon,eficiencia_huffman)

def imprimir_error():
    #acá deberia imprimir error
    print("Sexooo")



# ========== VENTANA PRINCIPAL ==========
ventana = registros.ventana  # Traemos la ventana que definida en registros.py
ventana.geometry("800x500")  # Le ponemos un tamaño fijo
ventana.resizable(False, False)
ventana.configure(bg=constantes.color_fondo)
ventana.title("BitSplitter")  # Título que va a salir en la barra


# ---------- FRAME DEL TÍTULO ----------
frame_titulo = ctk.CTkFrame(
    ventana,
    fg_color=constantes.color_fondo_titulo,
    border_width=1,
    border_color=constantes.color_borde,
)
frame_titulo.place(
    relx=0.5,
    rely=0.04,
    relheight=0.1,
    relwidth=1.01,
    anchor=tk.CENTER
)

# Acá va la etiqueta que muestra el título, adentro del frame
titulo = tk.Label(
    frame_titulo,
    text="Codificador Shannon-Fano & Huffman",
    font=constantes.fuente_titulo,
    bg=constantes.color_fondo_titulo,
    fg=constantes.color_texto
)
titulo.pack(expand=True)


# ---------- FRAME DE ENTRADA DE TEXTO ----------
frame_input = tk.Frame(ventana, bg=constantes.color_fondo)
frame_input.place(rely=0.09, relheight=0.25, relwidth=1)

# Label que dice “Input Text”
tk.Label(
    frame_input,
    text="Texto de entrada",
    font=constantes.fuente_seccion,
    bg=constantes.color_fondo,
    fg=constantes.color_texto
).grid(row=0, column=0, padx=20, pady=15, sticky="w")

# Campo donde el usuario escribe o pega el texto a codificar
texto_entrada = ctk.CTkEntry(
    frame_input,
    font=constantes.fuente_general,
    width=400,
    corner_radius=5,
    border_width=1,
    border_color=constantes.color_borde
)
texto_entrada.grid(row=1, column=0, padx=20, sticky="nw")

# Botón para cargar archivo, que llama a la función anterior
boton_cargar = ctk.CTkButton(
    frame_input,
    text="Cargar archivo",
    font=("Arial", 16),
    fg_color=constantes.color_boton,
    text_color=constantes.color_texto,
    corner_radius=5,
    border_width=1,
    border_color=constantes.color_borde,
    command= seleccionar_archivo
)
boton_cargar.grid(row=1, column=1, padx=20, sticky="w")

# Botón para limpiar entrada
boton_limpiar = ctk.CTkButton(
    frame_input,
    text="Limpiar entrada",
    font=("Arial", 16),
    fg_color=constantes.color_boton,
    text_color=constantes.color_texto,
    corner_radius=5,
    border_width=1,
    border_color=constantes.color_borde,
    command= limpiar_input
)
boton_limpiar.grid(row=1, column=2, sticky="w")


# ---------- FRAME DE CODIFICACIÓN ----------
frame_code = tk.Frame(ventana, bg=constantes.color_fondo)
frame_code.place(rely=0.30, relheight=0.4, relwidth=1)

# Esto para que el campo de texto se expanda y quede bien
frame_code.grid_columnconfigure(0, weight=1)
frame_code.grid_rowconfigure(1, weight=1)

# Label que dice “Encoded Message”
tk.Label(
    frame_code,
    text="Texto codificado",
    font=constantes.fuente_seccion,
    bg=constantes.color_fondo,
    fg=constantes.color_texto
).grid(row=0, column=0, padx=20, pady=10, sticky="w")

# Aquí mostramos el resultado del código generado (con el campo de texto bloqueado para que no editen)
campo_texto = ctk.CTkTextbox(
    frame_code,
    font=("Arial", 12),
    wrap="word",
    corner_radius=5,
    border_width=1,
    border_color=constantes.color_borde
)
campo_texto.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0,10))
campo_texto.configure(state="disabled")


# ---------- FRAME BOTONES SHANNON Y HUFFMAN ----------
frame_botones = tk.Frame(frame_code, bg=constantes.color_fondo)
frame_botones.grid(row=1, column=1, sticky="w")

# Botón que ejecuta el codificador Shannon
encode = ctk.CTkButton(
    frame_botones,
    text="Shannon",
    font=("Arial", 14),
    fg_color=constantes.color_boton,
    text_color=constantes.color_texto,
    corner_radius=5,
    width=100,
    border_width=1,
    border_color=constantes.color_borde,
    command=lambda: ejecutar_shannon(texto_entrada.get())
)
encode.grid(row=0, column=0, padx=10, pady=7, sticky="w")

# Botón que ejecuta el codificador Huffman
decode = ctk.CTkButton(
    frame_botones,
    text="Huffman",
    font=("Arial", 14),
    fg_color=constantes.color_boton,
    text_color=constantes.color_texto,
    corner_radius=5,
    width=100,
    border_width=1,
    border_color=constantes.color_borde,
    command=lambda:ejecutar_huffman(texto_entrada.get())
)
decode.grid(row=1, column=0, padx=10, pady=7, sticky="w")


# ---------- FRAME DE RESULTADOS ----------
frame_output = tk.Frame(ventana, bg=constantes.color_fondo)
frame_output.place(rely=0.7, relheight=0.3, relwidth=1)

frame_output.grid_columnconfigure(0, weight=1)

# Título de la sección resultados
tk.Label(
    frame_output,
    text="Parámetros de la codificación",
    font=constantes.fuente_seccion,
    bg=constantes.color_fondo,
    fg=constantes.color_texto
).grid(row=0, column=0, padx=20, pady=10, sticky="w")

# Contenedor para los resultados con borde
frame_resultados = ctk.CTkFrame(
    frame_output,
    border_width=1,
    border_color=constantes.color_borde,
    fg_color="transparent"
)
frame_resultados.grid(row=1, column=0, padx=20, sticky="nsew")

# Etiquetas para mostrar los indices de los resultados. Es decir, indice: valor
etiqueta_eficiencia=tk.Label(
    frame_resultados,
    text="Eficiencia:",
    bg=constantes.color_fondo,
    font=("Arial", 12)
)
etiqueta_eficiencia.grid(row=0, column=0, sticky="w", padx=2, pady=1)

etiqueta_entropia=tk.Label(
    frame_resultados,
    text="Entropia:",
    bg=constantes.color_fondo,
    font=("Arial", 12)
)
etiqueta_entropia.grid(row=1, column=0, sticky="w", padx=2, pady=1)

etiqueta_longitud_promedio=tk.Label(
    frame_resultados,
    text="Longitud:",
    bg=constantes.color_fondo,
    font=("Arial", 12),
)
etiqueta_longitud_promedio.grid(row=2, column=0, sticky="w", padx=2, pady=1)

graficar = ctk.CTkButton(
    frame_botones,
    text="Comparar",
    font=("Arial", 14),
    fg_color=constantes.color_boton,
    text_color=constantes.color_texto,
    corner_radius=5,
    width=100,
    border_width=1,
    border_color=constantes.color_borde,
    command= ejecutar_grafica
)
graficar.grid(row=2, column=0, padx=10, pady=7, sticky="w")

# ---------- INICIAR APLICACIÓN ----------
ventana.mainloop()  # Arrancamos el loop para que la app corra y responda