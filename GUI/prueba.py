# Acá tiene que ir lo de tk inter
import tkinter as tk


app = tk.Tk() #creo la ventana principal
#app es un objeto de la clase Tk, que es la ventana principal de la aplicación
app.geometry("800x600") #defino el tamaño de la ventana altura por anchura
#color de fondo
app.configure(bg="#f0f0f0") #defino el color de fondo de la ventana
app.title("BitSplitter") #defino el título de la ventana

# Crea una variable de tipo cadena vinculada a la interfaz (app), útil para actualizar textos dinámicamente (como entradas o etiquetas)
palabra = tk.StringVar(app)
palabra.set("¡Hola, mundo!") #establezco un valor inicial para la variable
palabra.set("¡Hola!") #actualizo el valor de la variable y los widgets vinculados a ella se actualizarán automáticamente
# StringVar es una clase de tkinter que permite crear variables de tipo cadena que se pueden vincular a widgets de la interfaz gráfica

entrada = tk.StringVar(app)

#-- AGREGO WIDGETS A LA VENTANA --
#un widget es un elemento de la interfaz gráfica, como un botón, una etiqueta, etc.
def saludar():
    print("¡Hola, mundo!") #función que se ejecutará al hacer clic en el botón
    print("¡Hola, mundo versión 2!") #otra función que se ejecutará al hacer clic en el botón

contador = [0]

def actualizar_palabra():
    #esta función se ejecuta al hacer clic en el botón
    #actualiza el valor de la variable palabra con el texto ingresado en la entrada de texto
    palabra.set("hola" + str(contador[0])) #actualiza la variable palabra con el texto ingresado en la entrada de texto
    contador[0] += 1 #incrementa el contador en 1 cada vez que se hace clic en el botón

tk.Button(
    #donde queremos incrustar el botón, va en casi todos los widgets
    app,
    text="Cargar archivo", #el texto que queremos que tenga el botón
    font=("Arial", 14), #tipo de letra y tamaño
    fg="#ffffff", #color del texto
    bg="#4CAF50", #color de fondo del botón
    #para hacer que el botón haga algo al hacer clic, se usa el parámetro command
    #command=saludar, command recibe una función que se ejecutará al hacer clic en el botón
    #también se puede usar lambda para pasar objetos o parámetros a la función, si no usáramos esto se ejecutaría al momento de crear el botón
    command=lambda: (print("¡Hola, mundo versión 2!" + entrada.get()), actualizar_palabra())#esto es una función anónima que imprime un mensaje al hacer clic
    #lambda solo acepta un parámetro, si queremos pasar más de uno, usamos una función normal como antes
).pack(
    fill=tk.BOTH, #para que el botón ocupe todo el ancho de la ventana
    expand=True, #para que se expanda si hay un cambio de tamaño de la ventana
) #el método pack() indica cómo se va a colocar el widget en la ventana, también se puede usar grid() o place()

# Agrego una entrada de texto para que el usuario pueda escribir algo
tk.Entry(
    #nos permite escribir texto en la ventana
    app,
    font=("Arial", 14), #tipo de letra y tamaño
    fg="#333333", #color del texto
    bg="#ffffff", #color de fondo de la entrada de texto
    justify=tk.LEFT, #alineación del texto dentro de la entrada
    #justify puede ser LEFT, CENTER o RIGHT
    textvariable=entrada, #vincula la entrada de texto a la variable palabra, así se actualiza automáticamente
).pack(
    fill=tk.BOTH, #para que la entrada ocupe todo el ancho de la ventana
    # como hay dos BOTH se van a repartir el espacio entre el botón y la entrada de texto
    #si hubiera más widgets, se repartiría el espacio entre todos
    expand=True, #para que se expanda si hay un cambio de tamaño de la ventana
    padx=10, #margen horizontal interno de 10 píxeles
)

tk.Label(
    app,
    font=("Arial", 14), #tipo de letra y tamaño
    fg="#A30808", #color del texto
    textvariable=palabra, #vincula la etiqueta a la variable palabra, así se actualiza automáticamente
).pack(
    fill=tk.BOTH, #para que la etiqueta ocupe todo el ancho de la ventana
    expand=True, #para que se expanda si hay un cambio de tamaño de la ventana
    padx=10, #margen horizontal interno de 10 píxeles
)

#siempre al final de todo se pone el mainloop, que es el bucle principal de la aplicación
#es el que mantiene la ventana abierta y espera a que el usuario interactúe con ella
app.mainloop() #la muestro y la mantengo abierta hasta que el usuario la cierre