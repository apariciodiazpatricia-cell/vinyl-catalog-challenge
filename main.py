# Main file for the vinyl catalog system
catalogName = "Vinyl Catalog Challenge"
welcomeMessage = "¡Bienvenido al catálogo de vinilos coleccionables!"

print("==================================================")
print(welcomeMessage)
print("==================================================")



print("\n--- Registro de Nuevo Vinilo ---")

vinylId = input("Introduce el identificador del vinilo (ej. V01): ")
vinylName = input("Introduce el nombre del álbum/artista: ")
vinylCategory = input("Introduce la categoría (ej. Rock, Pop): ")

vinylPrice = float(input("Introduce el precio (ej. 45.0): "))
vinylStatus = input("Introduce el estado (disponible / reservada / vendida): ")
vinylDescription = input("Introduce la descripción (debe incluir 'usada' o 'certificada'): ")

vinylItem = {
    "id": vinylId,
    "name": vinylName,
    "category": vinylCategory,
    "price": vinylPrice,
    "status": vinylStatus,
    "description": vinylDescription
}
catalog = []
catalog.append(vinylItem)
print("\n¡Vinilo guardado con éxito en el catálogo!")
print(catalog)

# Parte 4: Crear un set con las categorías únicas del catálogo
catalogCategories = {vinylCategory}

print("\n--- Información de Categorías ---")
print(f"Categorías únicas en el catálogo: {catalogCategories}")
print(f"Cantidad de categorías diferentes: {len(catalogCategories)}")


# Lista vacía donde iremos acumulando los 10 vinilos
catalog = []

# Bucle para repetir el proceso 10 veces (del 0 al 9)

for i in range(10):
    print(f"\n--- Registro de Vinilo {i + 1} de 10 ---")

    vinylId = input("Introduce el identificador del vinilo (ej. V01): ")
    vinylName = input("Introduce el nombre del álbum/artista: ")
    vinylCategory = input("Introduce la categoría (ej. Rock, Pop): ")
    vinylPrice = float(input("Introduce el precio (ej. 45.0): "))
    vinylStatus = input("Introduce el estado (disponible / reservada / vendida): ")
    vinylDescription = input("Introduce la descripción (debe incluir 'usada' o 'certificada'): ")

    # Creamos el objeto (diccionario) para este vinilo

    vinylItem = {
        "id": vinylId,
        "name": vinylName,
        "category": vinylCategory,
        "price": vinylPrice,
        "status": vinylStatus,
        "description": vinylDescription
    }

    # Añadimos el vinilo a nuestra lista del catálogo

    catalog.append(vinylItem)
    print("¡Vinilo guardado con éxito en el catálogo!")


    # Mostramos el catálogo completo al terminar el bucle

print("\n==================================================")
print("       CATÁLOGO COMPLETO DE VINILOS COLECCIONABLES")
print("==================================================")

for vinyl in catalog:
    print(
        f"ID: {vinyl['id']} | Álbum: {vinyl['name']} | Categoría: {vinyl['category']} | Precio: {vinyl['price']}€ | Estado: {vinyl['status']}")



catalogCategories = {vinyl['category'] for vinyl in catalog}

print("\n--- Resumen de Categorías ---")

print(f"Categorías únicas en el catálogo: {catalogCategories}")
print(f"Cantidad de categorías diferentes: {len(catalogCategories)}")
print(f"Cantidad total de piezas en el catálogo: {len(catalog)}")