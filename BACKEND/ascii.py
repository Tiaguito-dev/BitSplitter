from collections import Counter #Usamos funcion Counter de la libreria collection para contar fácilmente cuántas veces aparece cada carácter en el texto.
import math #se usa para calcular logaritmos (para la entropía).

def calcular_frecuencias(texto):
    return Counter(texto)

# Calcula la probabilidad de cada carácter
def calcular_probabilidades(frecuencias):
    total = sum(frecuencias.values())
    return {char: freq / total for char, freq in frecuencias.items()}

# Calcula la entropía
def calcular_entropia(probabilidades):
    return -sum(p * math.log2(p) for p in probabilidades.values())

# Calcula la eficiencia del código
def calcular_eficiencia(entropia):
    return (entropia / 8) * 100

def codificar(texto):
    frecuencias = calcular_frecuencias(texto)
    probabilidades = calcular_probabilidades(frecuencias)
    entropia = calcular_entropia(probabilidades)
    eficiencia = round(calcular_eficiencia(entropia))

    print("\n === BIENVENIDO A ASCII ===")
    print("\n Eficiencia", eficiencia, "%")

    return eficiencia
