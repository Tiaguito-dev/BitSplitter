import heapq
from collections import Counter
import math

# Clase para representar cada nodo del árbol de Huffman
class NodoHuffman:
    def __init__(self, caracter=None, frecuencia=0):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):  # Para que los nodos se comparen por frecuencia al usar heapq
        return self.frecuencia < otro.frecuencia

# Cuenta las frecuencias de los caracteres
def calcular_frecuencias(texto):
    return Counter(texto)

# Calcula la probabilidad de cada carácter
def calcular_probabilidades(frecuencias):
    total = sum(frecuencias.values())
    return {char: freq / total for char, freq in frecuencias.items()}

# Construye el árbol de Huffman usando un heap (cola de prioridad)
def construir_arbol(frecuencias):
    heap = []
    for caracter, freq in frecuencias.items():
        nodo = NodoHuffman(caracter, freq)
        heapq.heappush(heap, nodo)

    while len(heap) > 1:
        nodo1 = heapq.heappop(heap)
        nodo2 = heapq.heappop(heap)
        nodo_padre = NodoHuffman(frecuencia=nodo1.frecuencia + nodo2.frecuencia)
        nodo_padre.izquierda = nodo1
        nodo_padre.derecha = nodo2
        heapq.heappush(heap, nodo_padre)

    return heap[0] if heap else None

# Asigna códigos a cada carácter recorriendo el árbol
def generar_codigos(nodo, codigo_actual="", codigos=None):
    if codigos is None:
        codigos = {}

    if nodo is None:
        return codigos

    if nodo.caracter is not None:
        codigos[nodo.caracter] = codigo_actual
        return codigos

    generar_codigos(nodo.izquierda, codigo_actual + "0", codigos)
    generar_codigos(nodo.derecha, codigo_actual + "1", codigos)

    return codigos

# Codifica el texto original usando los códigos binarios
def codificar_texto(texto, codigos):
    return ''.join(codigos[char] for char in texto)

# Decodifica el texto codificado usando el árbol de Huffman
def decodificar_texto(texto_codificado, arbol_huffman):
    resultado = []
    nodo = arbol_huffman
    for bit in texto_codificado:
        nodo = nodo.izquierda if bit == '0' else nodo.derecha
        if nodo.caracter is not None:
            resultado.append(nodo.caracter)
            nodo = arbol_huffman
    return ''.join(resultado)

# Calcula la entropía
def calcular_entropia(probabilidades):
    return -sum(p * math.log2(p) for p in probabilidades.values())

# Calcula la longitud promedio del código
def calcular_longitud_promedio(probabilidades, codigos):
    return sum(probabilidades[char] * len(codigos[char]) for char in codigos)

# Calcula la eficiencia del código
def calcular_eficiencia(entropia, longitud_promedio):
    return (entropia / longitud_promedio) * 100 if longitud_promedio > 0 else 0

# Imprime el árbol de Huffman
def imprimir_arbol(nodo, nivel=0, camino=''):
    if nodo is None:
        return

    if nodo.caracter is not None:
        print(f"{'   ' * nivel}➡️  Código: {camino} → Símbolo: '{nodo.caracter}'")
    else:
        print(f"{'   ' * nivel}🔽 Nivel {nivel}")
        print(f"{'   ' * nivel}   Si bit = '0':")
        imprimir_arbol(nodo.izquierda, nivel + 1, camino + '0')
        print(f"{'   ' * nivel}   Si bit = '1':")
        imprimir_arbol(nodo.derecha, nivel + 1, camino + '1')

# Genera una tabla de información siguiendo el recorrido del árbol
def obtener_tabla_desde_arbol(nodo, camino='', tabla=None, frecuencias=None, probabilidades=None):
    if tabla is None:
        tabla = []
    if nodo is None:
        return tabla
    if nodo.caracter is not None:
        tabla.append({
            'caracter': nodo.caracter,
            'codigo': camino,
            'frecuencia': frecuencias[nodo.caracter],
            'probabilidad': probabilidades[nodo.caracter]
        })
    else:
        obtener_tabla_desde_arbol(nodo.izquierda, camino + '0', tabla, frecuencias, probabilidades)
        obtener_tabla_desde_arbol(nodo.derecha, camino + '1', tabla, frecuencias, probabilidades)
    return tabla

# Función principal de compresión
def comprimir(texto):
    frecuencias = calcular_frecuencias(texto)
    probabilidades = calcular_probabilidades(frecuencias)
    arbol = construir_arbol(frecuencias)
    codigos = generar_codigos(arbol)
    texto_codificado = codificar_texto(texto, codigos)
    entropia = calcular_entropia(probabilidades)
    longitud_promedio = calcular_longitud_promedio(probabilidades, codigos)
    eficiencia = calcular_eficiencia(entropia, longitud_promedio)
    return texto_codificado, codigos, arbol, frecuencias, probabilidades, entropia, longitud_promedio, eficiencia

# Bloque principal
if __name__ == "__main__":
    texto = input("Ingrese el texto a codificar: ").strip()

    if not texto:
        print("Texto vacío. No hay nada para codificar.")
        exit()

    texto_codificado, codigos, arbol, frecuencias, probabilidades, entropia, longitud_promedio, eficiencia = comprimir(texto)

    print("\nCaracter | Frecuencia | Probabilidad | Código Huffman (orden del árbol)")
    print("---------|------------|--------------|-----------------------------")
    tabla_huffman = obtener_tabla_desde_arbol(arbol, '', [], frecuencias, probabilidades)
    for entrada in tabla_huffman:
        char = repr(entrada['caracter'])
        print(f"{char:^8} | {entrada['frecuencia']:^10} | {entrada['probabilidad']:^12.4f} | {entrada['codigo']:^27}")

    print("\nTexto codificado:")
    print(texto_codificado)

    print("\nÁrbol de Huffman:")
    imprimir_arbol(arbol)

    print("\nTexto decodificado:")
    print(decodificar_texto(texto_codificado, arbol))

    print(f"\nEntropía: {entropia:.4f} bits")
    print(f"Longitud promedio del código: {longitud_promedio:.4f} bits/símbolo")
    print(f"Eficiencia del código: {eficiencia:.2f} %")
