import os

# Generar una clave secreta aleatoria
clave_secreta = os.urandom(32)

# Convertir la clave secreta en una cadena hexadecimal
clave_secreta_hex = clave_secreta.hex()

print("Clave secreta generada:", clave_secreta_hex)
