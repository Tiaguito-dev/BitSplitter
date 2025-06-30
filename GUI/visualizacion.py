import tkinter as tk
from tkinter import Toplevel
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def abrir_ventana_grafico(ventana, eficiencia_shannon,eficiencia_huffman):
    # Crear ventana secundaria
    ventana_grafico = Toplevel(ventana)
    ventana_grafico.title("Gráfico de Barras")
    ventana_grafico.geometry("600x400")

    # Ejemplo de datos
    categorias = ["shannon", "huffman"]
    valores = [eficiencia_shannon, eficiencia_huffman]

    # Crear figura de matplotlib
    figura = Figure(figsize=(5, 3), dpi=100)
    ax = figura.add_subplot(111)
    ax.bar(categorias, valores)
    ax.set_title("Comparación de algoritmos")
    ax.set_xlabel("BitSplitter")
    ax.set_ylabel("Eficiencia")

    # Incrustar gráfico en la ventana secundaria
    canvas = FigureCanvasTkAgg(figura, master=ventana_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # No afecta a la ventana principal: cuando cierres esta ventana,
    # la principal sigue funcionando.

