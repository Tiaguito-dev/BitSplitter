import tkinter as tk
import customtkinter as ctk  # Importar customtkinter para widgets personalizados
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from BACKEND import constantes  # Importar las constantes desde el módulo de constantes
from DATABASE import registros  # Para importar la ventana


# -- CONFIGURACIÓN DE LA VENTANA PRINCIPAL --
ventana = registros.ventana  # Utilizar la ventana principal definida en registros.py
ventana.geometry("800x500")  # Definir el tamaño de la ventana (ancho x alto)
ventana.resizable(False, False)  # Deshabilitar el cambio de tamaño de la ventana
# Esto evita que el usuario pueda cambiar el tamaño de la ventana y mantiene un diseño fijo.
ventana.configure(bg=constantes.color_fondo)  # Definir el color de fondo de la ventana
ventana.title("BitSplitter")  # Definir el título de la ventana

# -- CONFIGURACIÓN DE WIDGETS --

# Frame con borde redondeado para el título
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
# Etiqueta del título dentro del frame
titulo = tk.Label(
    frame_titulo,
    text="BitSplitter: Shannon-Fano Encoder",
    font=constantes.fuente_titulo,
    bg=constantes.color_fondo_titulo,
    fg=constantes.color_texto
)
titulo.pack(expand=True)


# -- Frame de la carga de archivos --
frame_input = tk.Frame(ventana, bg=constantes.color_fondo)  # Crear un frame para la carga de archivos
frame_input.place(
    rely=0.09, 
    relheight=0.25, 
    relwidth=1
)
# Titulo de la sección carga de archivos
tk.Label(
    frame_input, 
    text="Input Text", 
    font=constantes.fuente_seccion,
    bg=constantes.color_fondo,
    fg=constantes.color_texto  # ← color del texto
).grid(row=0, column=0, padx=20, pady=15, sticky="w")
entrada_titulo = ctk.CTkEntry(
    frame_input,
    font=constantes.fuente_general,  # Fuente y tamaño del texto
    width=400,
    corner_radius=5,
    border_width=1,
    border_color=constantes.color_borde
)
entrada_titulo.grid(row=1, column=0, padx=20, sticky="nw")
# Botón redondeado con customtkinter
boton_cargar = ctk.CTkButton(
    frame_input,
    text="Cargar archivo",
    font=("Arial", 16),
    fg_color=constantes.color_boton,          # color de fondo
    text_color=constantes.color_texto,          # color del texto
    corner_radius=5,            # radio del borde redondeado
    border_width=1,  # Ancho del borde
    border_color=constantes.color_borde,  # Color del borde
    command=lambda: print("¡Archivo cargado!")
)
boton_cargar.grid(row=1, column=1, padx=20, sticky="w")


# -- Frame de codificación y decodificación --
frame_code = tk.Frame(ventana, bg=constantes.color_fondo)
frame_code.place(
    rely=0.30,  # Posición vertical relativa (comienza abajo de la etiqueta)
    relheight=0.4,
    relwidth=1
)
# Configuración de la columna para que se expanda
frame_code.grid_columnconfigure(0, weight=1)  # Permitir que la columna 1 se expanda
frame_code.grid_rowconfigure(1, weight=1)  # Permitir que la fila 2 se expanda
# Titulo de la sección codificación y decodificación
tk.Label(
    frame_code, 
    text="Encoded Message", 
    font=constantes.fuente_seccion,
    bg=constantes.color_fondo,
    fg=constantes.color_texto
).grid(row=0, column=0, padx=20, pady=10, sticky="w")
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
# Botones de codificación y decodificación
frame_botones = tk.Frame(
    frame_code,
    bg=constantes.color_fondo
    )
frame_botones.grid(row=1, column=1,sticky="w")
# Botón "Encode"
codigo = registros.codigo  # Aquí se vincula la variable codigo para actualizarla con el código generado
encode = ctk.CTkButton(
    frame_botones,
    text="Encode",
    font=("Arial", 14),
    fg_color= constantes.color_boton,          # color de fondo
    text_color=constantes.color_texto,          # color del texto
    corner_radius=5,            # radio del borde redondeado
    width=100,
    border_width=1,  # Ancho del borde
    border_color=constantes.color_borde,  # Color del borde
    # Cuando aprieta el botón tiene que guardar el texto en la BD
    command = lambda: (
        registros.guardar_palabra(entrada_titulo.get()),
        campo_texto.configure(state="normal"),
        campo_texto.delete("1.0", "end"),
        campo_texto.insert("1.0", codigo.get()),
        campo_texto.configure(state="disabled")
    ) # Aquí se llama a la función que guarda el texto ingresado en la entrada de texto
# TO DO # Implementar la función de codificación aquí


)
encode.grid(
    row=0, column=0, padx=10, pady=7,sticky="w"
)
# Botón "Decode"
decode = ctk.CTkButton(
    frame_botones,
    text="Decode",
    font=("Arial", 14),
    fg_color= constantes.color_boton,          # color de fondo
    text_color=constantes.color_texto,          # color del texto
    corner_radius=5,            # radio del borde redondeado
    width=100,
    border_width=1,  # Ancho del borde
    border_color=constantes.color_borde,  # Color del borde
    command=lambda: print("¡Archivo decodificado!")
)
decode.grid(
    row=1, column=0, padx=10, pady=7, sticky="w"
)


# -- Frame de resultados --
frame_output = tk.Frame(ventana, bg=constantes.color_fondo)
frame_output.place(
    rely=0.7,  # Posición vertical relativa (comienza abajo de la etiqueta)
    relheight=0.3,  # Altura relativa del contenedor
    relwidth=1,  # Ancho relativo del contenedor
)  # posicionamos el "div" completo
frame_output.grid_columnconfigure(0, weight=1)  # Permitir que la fila 2 se expanda
# Titulo de la sección resultados
tk.Label(
    frame_output, 
    text="Comparison Results", 
    font=constantes.fuente_seccion,
    bg=constantes.color_fondo,
    fg=constantes.color_texto
).grid(row=0, column=0, padx=20, pady=10, sticky="w")  # Título de la sección
frame_resultados = ctk.CTkFrame(frame_output, border_width=1, border_color=constantes.color_borde, fg_color="transparent")  # Crear un frame personalizado con customtkinter
frame_resultados.grid(row=1, column=0, padx=20, sticky="nsew")  # Contenedor para los resultados
tk.Label(
    frame_resultados,
    text="Compresion ratio:",
    bg=constantes.color_fondo,
    font=("Arial", 12)
).grid(row=0, column=0, sticky="w", padx=2, pady=1)  # Etiqueta para mostrar resultados
tk.Label(
    frame_resultados,
    text="Compresion ratio:",
    bg=constantes.color_fondo,
    font=("Arial", 12)
).grid(row=1, column=0, sticky="w", padx=2, pady=1)  # Etiqueta para mostrar resultados
tk.Label(
    frame_resultados,
    text="Compresion ratio:",
    bg=constantes.color_fondo,
    font=("Arial", 12),
).grid(row=2, column=0, sticky="w", padx=2, pady=1)  # Etiqueta para mostrar resultados


# -- Iniciar la aplicación --


ventana.mainloop()  # Iniciar el bucle principal de la aplicación