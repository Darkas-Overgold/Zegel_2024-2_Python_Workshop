# Gestor de iniciales por región Pokémon
pokemon_iniciales = {
    "Kanto": ["Bulbasaur", "Charmander", "Squirtle"],
    "Johto": ["Chikorita", "Cyndaquil", "Totodile"],
    "Hoenn": ["Treecko", "Torchic", "Mudkip"],
    "Sinnoh": ["Turtwig", "Chimchar", "Piplup"],
    "Unova": ["Snivy", "Tepig", "Oshawott"],
    "Kalos": ["Chespin", "Fennekin", "Froakie"],
    "Alola": ["Rowlet", "Litten", "Popplio"],
    "Galar": ["Grookey", "Scorbunny", "Sobble"],
    "Paldea": ["Sprigatito", "Fuecoco", "Quaxly"]
}

def mostrar_regiones():
    """Muestra las regiones disponibles."""
    print("\nRegiones disponibles:")
    for region in pokemon_iniciales.keys():
        print(f"- {region}")

def mostrar_iniciales(region):
    """Muestra los iniciales de la región seleccionada."""
    print(f"\nIniciales de {region}:")
    for inicial in pokemon_iniciales[region]:
        print(f"- {inicial}")

def gestor_pokemon():
    """Función principal del gestor de iniciales Pokémon."""
    while True:
        print("\n" + "=" * 40)
        print("Gestor de Iniciales Pokémon".center(40))
        print("=" * 40)
        print("1. Mostrar regiones disponibles")
        print("2. Mostrar iniciales de una región")
        print("3. Salir")
        print("=" * 40)

        opcion = input("Selecciona una opción: ")

        try:
            if opcion == "1":
                mostrar_regiones()
            elif opcion == "2":
                region = input("Introduce el nombre de la región: ")
                if region in pokemon_iniciales:
                    mostrar_iniciales(region)
                else:
                    print("Error: La región no es válida. Intenta nuevamente.")
            elif opcion == "3":
                print("¡Hasta luego, Entrenador Pokémon!")
                break
            else:
                print("Opción no válida. Intenta nuevamente.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

# Ejecutar el programa
gestor_pokemon()