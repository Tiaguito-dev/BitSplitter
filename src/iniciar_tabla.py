# TABLA DE ASCII
for i in range(256):
    char = chr(i)
    # Mostrar carácter imprimible; si no, mostrar código hexadecimal
    if 32 <= i <= 126:
        display_char = char
    else:
        display_char = f"\\x{i:02x}"
    bin_code = format(i, '08b')
    print(f"{display_char:<5} | {bin_code}")

# ESTA ES LA TABLA
tabla_codigos = {
    'A': 0.38,
    'B': 0.17,
    'C': 0.15,
    'D': 0.15,
    'E': 0.12,
}

print(tabla_codigos["B"])