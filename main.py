import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

if __name__ == "__main__":
    longitud =int(input("Ingresa la longitud de la contrasena: "))
    contrasena = generar_contrasena(longitud)
    print("Contrasena generada: ", contrasena) 