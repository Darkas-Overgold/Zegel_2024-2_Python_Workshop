# Fundamentos de programación
import random
import string

def generate_password():
    # Diccionario que contiene los diferentes tipos de caracteres
    char_types = {
        "lowercase": string.ascii_lowercase,
        "uppercase": string.ascii_uppercase,
        "digits": string.digits,
        "symbols": string.punctuation
    }

    while True:
        # Solicitar al usuario la longitud de la contraseña
        length = input("Digita la longitud de tu contraseña (mínimo 8): ")

        if length.isdigit():  # Verificar si la entrada es un número
            length = int(length)
            if length >= 8:
                break
            else:
                print("La longitud debe ser al menos de 8 caracteres. Intenta nuevamente.")
        else:
            print("Debes ingresar un número válido. Intenta nuevamente.")

    # Crear una lista de tuplas con el nombre y los caracteres de cada tipo
    char_pool = [(name, chars) for name, chars in char_types.items()]

    # Construir la contraseña asegurando que al menos un carácter de cada tipo esté presente
    password = []
    for name, chars in char_pool:
        password.append(random.choice(chars))

    # Rellenar el resto de la contraseña con caracteres aleatorios de cualquier tipo
    all_chars = ''.join([chars for _, chars in char_pool])
    for _ in range(length - len(password)):
        password.append(random.choice(all_chars))

    # Mezclar los caracteres para que la contraseña sea menos predecible
    random.shuffle(password)

    # Convertir la lista en una cadena y devolverla
    return ''.join(password)

if __name__ == "__main__":
    print("Generador de contraseñas seguras:")
    password = generate_password()
    print(f"Tu contraseña es: {password}")
