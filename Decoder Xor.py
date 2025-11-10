# ======================================================
# Autor: Arath Reyes González
# Universidad Autónoma de Baja California
# Práctica: Desencriptado XOR
# ======================================================

# Tramas en hexadecimal
tramas = [
    "5041434f3a012d2f2d",
    "5041434f3a0a2d2e23"
]

# Llave XOR
key = 0x42

# Función para convertir hex -> bytes -> aplicar XOR
def xor_decode(hex_data, key):
    data = bytes.fromhex(hex_data)
    result = bytes([b ^ key for b in data])
    return result

# Procesar cada trama
for i, trama in enumerate(tramas, 1):
    decodificada = xor_decode(trama, key)
    print(f"Trama {i}: {trama}")
    print(" Resultado XOR:", decodificada)
    # Filtrar bytes imprimibles (ASCII)
    texto_legible = ''.join(chr(b) for b in decodificada if 32 <= b <= 126)
    print(" Texto legible:", texto_legible)
    print("-" * 40)
