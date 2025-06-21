from collections import Counter #Usamos funcion Counter de la libreria collection para contar fácilmente cuántas veces aparece cada carácter en el texto.
import math #se usa para calcular logaritmos (para la entropía).
import string # ofrece listas útiles como string.printable, que usamos para filtrar caracteres válidos.

def limpiar_texto(texto, permitidos=None): #Permite evitar contar caracteres invisibles (como \n, \x00, etc.) que pueden distorsionar las frecuencias.
    if permitidos is None: #Filtra el texto para contar solo caracteres permitidos. Por defecto permite todos los caracteres imprimibles.
        permitidos = set(string.printable)  
    return ''.join(c for c in texto if c in permitidos)

def calcular_probabilidades(texto):
    frecuencias = Counter(texto) #Cuenta cada carácter del texto
    total = sum(frecuencias.values()) #Total de caracteres
    probabilidades = {char: freq / total for char, freq in frecuencias.items()}
    return probabilidades, frecuencias #Retorna dos estructuras: probabilidades: diccionario {carácter: probabilidad} y frecuencias: diccionario {carácter: frecuencia absoluta} 

def shannon_fano(probabilidades):
    simbolos_ordenados = sorted(probabilidades.items(), key=lambda x: x[1], reverse=True) #Ordena los símbolos por probabilidad descendente.
    return codificar_recursivo(simbolos_ordenados) #Codificacion recursiva

def codificar_recursivo(simbolos):
    if len(simbolos) == 1:
        return {simbolos[0][0]: ''} #Caso base: un solo símbolo, código vacío
    total = sum(prob for _, prob in simbolos) #Cuando queda un solo símbolo, no necesita codificación (profundidad cero).
    acumulado = 0
    min_diff = float('inf')
    index = 0

    for i in range(len(simbolos)): #Inicializa acumulador para dividir la lista en dos subconjuntos con suma de probabilidades lo más cercana posible a 0.5.
        acumulado += simbolos[i][1]
        diff = abs(acumulado - (total - acumulado))
        if diff < min_diff:
            min_diff = diff
            index = i
        else:
            break #Encuentra el punto donde la diferencia entre los dos subconjuntos es mínima.

    #Divide la lista en dos partes
    grupo1 = simbolos[:index+1]
    grupo2 = simbolos[index+1:]
    codigos = {}

    codigos1 = codificar_recursivo(grupo1)
    for char in codigos1:
        codigos[char] = '0' + codigos1[char] #Llama recursivamente a la mitad superior y agrega '0' a todos sus códigos.

    codigos2 = codificar_recursivo(grupo2)
    for char in codigos2:
        codigos[char] = '1' + codigos2[char] #Llama recursivamente a la otra mitad y agrega '1' a todos sus códigos.

    return codigos #Devuelve el diccionario con todos los códigos.

def codificar_texto(texto, codigos): #Reemplaza cada carácter del texto original con su código Shannon-Fano
    return ''.join(codigos[char] for char in texto)

def calcular_entropia(probabilidades): #Fórmula de entropía de Shannon: mide la cantidad mínima de bits necesarios para codificar el mensaje.
    return -sum(p * math.log2(p) for p in probabilidades.values())

def calcular_longitud_promedio(probabilidades, codigos): #Promedio ponderado de la longitud de los códigos (se espera que se acerque a la entropía si el código es eficiente)
    return sum(probabilidades[char] * len(codigos[char]) for char in codigos)

def calcular_eficiencia(entropia, longitud_promedio): #Evalúa qué tan cercano está el código real a la entropía maxima (100%).
    return (entropia / longitud_promedio) * 100 if longitud_promedio > 0 else 0

#Programa Principal

def main(palabra):
    # Validación básica de entrada
    print("Bienvenido al codificador Shannon-Fano") #Mensaje de bienvenida
    texto = limpiar_texto(palabra) #Pide al usuario el texto y lo limpia para evitar errores de codificación con caracteres raros.
    if not texto:
        print("El texto no contiene caracteres válidos para codificar.")
        exit() #Si después de limpiar no queda texto útil, se cancela.

    # Calcula las probabilidades y frecuencias de los caracteres
    # y genera los códigos Shannon-Fano
    probabilidades, frecuencias = calcular_probabilidades(texto)
    codigos = shannon_fano(probabilidades) #Se calculan las probabilidades y se generan los códigos Shannon-Fano.
    
    #Codifica el mensaje
    texto_codificado = codificar_texto(texto, codigos)
    
    # Calcula la entropía, longitud promedio y eficiencia del código
    entropia = calcular_entropia(probabilidades) 
    longitud_promedio = calcular_longitud_promedio(probabilidades, codigos)
    eficiencia = calcular_eficiencia(entropia, longitud_promedio)

    # -- IMPRESIÓN DE RESULTADOS --
    # Lo dejo comentado para que puedas descomentar si quieres ver los resultados en la consola.
    """
    print("\n--- Resultados de la codificación Shannon-Fano ---")
    # Imprime la tabla de frecuencias, probabilidades y códigos
    print("\nCaracter | Frecuencia | Probabilidad | Código Shannon-Fano") #Tabla que imprime cada carácter con su frecuencia, probabilidad y código asignado.
    print("---------|------------|--------------|---------------------")
    for char in sorted(probabilidades, key=probabilidades.get, reverse=True):
        print(f"{repr(char):^8} | {frecuencias[char]:^10} | {probabilidades[char]:^12.4f} | {codigos[char]:^19}")
    
    # Imprime el texto original y el texto codificado
    print("\nTexto codificado:")
    print(texto_codificado)
    
    # Imprime la entropía, longitud promedio y eficiencia del código
    print(f"\nEntropía H(X): {entropia:.4f} bits") #Entropía: cuánta información tiene el texto.
    print(f"Longitud promedio del código: {longitud_promedio:.4f} bits/símbolo") #Longitud promedio: cuánto ocupa realmente.
    print(f"Eficiencia del código: {eficiencia:.2f} %") #ficiencia: cuán cerca está de Hmax (100%)
    """
    return texto_codificado  # Devuelve el texto codificado para usarlo en la interfaz gráfica o donde sea necesario.