# Gestor de marcas de motos en Perú
marcas_motos = {
    "Honda": ["CB190R", "XR150L", "Wave 110"],
    "Yamaha": ["FZ FI", "XTZ 150", "R15 V4"],
    "Suzuki": ["Gixxer SF 250", "GN125", "Hayabusa"],
    "Kawasaki": ["Ninja 400", "Versys 300", "Z900"],
    "Bajaj": ["Pulsar NS200", "Dominar 400", "Discover 125"],
    "KTM": ["Duke 200", "RC 390", "Adventure 390"],
    "Royal_Enfield": ["Classic 350", "Himalayan", "Interceptor 650"],
    "Harley-Davidson": ["Iron 883", "Street Glide", "Fat Boy"]
}

def mostrar_marcas():
    """Muestra las marcas disponibles."""
    print("\nMarcas de motos disponibles en Perú:")
    for marca in marcas_motos.keys():
        print(f"- {marca}")

def mostrar_modelos(marca):
    """Muestra los modelos de la marca seleccionada."""
    print(f"\nModelos de {marca}:")
    for modelo in marcas_motos[marca]:
        print(f"- {modelo}")

def gestor_motos():
    """Función principal del gestor de marcas de motos."""
    while True:
        print("\n" + "=" * 40)
        print("Gestor de Marcas de Motos en Perú".center(40))
        print("=" * 40)
        print("1. Mostrar marcas disponibles")
        print("2. Mostrar modelos de una marca")
        print("3. Salir")
        print("=" * 40)

        opcion = input("Selecciona una opción: ")

        try:
            if opcion == "1":
                mostrar_marcas()
            elif opcion == "2":
                marca = input("Introduce el nombre de la marca: ")
                if marca in marcas_motos:
                    mostrar_modelos(marca)
                else:
                    print("Error: La marca no es válida. Intenta nuevamente.")
            elif opcion == "3":
                print("¡Gracias por usar el gestor! Hasta pronto.")
                break
            else:
                print("Opción no válida. Intenta nuevamente.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

# Ejecutar el programa
gestor_motos()
