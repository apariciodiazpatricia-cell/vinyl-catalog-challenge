# Main file for the vinyl catalog system
catalogName = "Vinyl Catalog Challenge"
welcomeMessage = "¡Bienvenido al catálogo de vinilos coleccionables!"

print("==================================================")
print(welcomeMessage)
print("==================================================")



print("\n--- Registro de Nuevo Vinilo ---")

# --- CAPTURA DE PIEZAS (Versión final interactiva) ---

vinylId = input("Introduce el identificador del vinilo (ej. V01): ")
vinylName = input("Introduce el nombre del álbum/artista: ")
vinylCategory = input("Introduce la categoría (ej. Rock, Pop): ")
vinylPrice = float(input("Introduce el precio (ej. 45.0): "))
vinylStatus = input("Introduce el estado (disponible/reservada/vendida): ")
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
    vinylStatus = input("Introduce el estado (disponible/reservada/vendida): ")
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


# --- PARTE 6: FILTRAR PIEZAS POR ESTADO (Sin usar else) ---

print("\n==================================================")
print("             FILTRADO POR ESTADOS                 ")
print("==================================================")

# 1. Filtrar por 'disponible'
print("\n--- Piezas en estado: DISPONIBLE ---")
disponibles = [vinyl for vinyl in catalog if vinyl['status'].lower() == 'disponible']

if disponibles:
    for vinyl in disponibles:
        print(f"ID: {vinyl['id']} | Álbum: {vinyl['name']} | Precio: {vinyl['price']}€")

if not disponibles:
    print("No hay piezas disponibles en este momento.")


# 2. Filtrar por 'reservada'
print("\n--- Piezas en estado: RESERVADA ---")
reservadas = [vinyl for vinyl in catalog if vinyl['status'].lower() == 'reservada']

if reservadas:
    for vinyl in reservadas:
        print(f"ID: {vinyl['id']} | Álbum: {vinyl['name']} | Precio: {vinyl['price']}€")

if not reservadas:
    print("No hay piezas reservadas en este momento.")


# 3. Filtrar por 'vendida'
print("\n--- Piezas en estado: VENDIDA ---")
vendidas = [vinyl for vinyl in catalog if vinyl['status'].lower() == 'vendida']

if vendidas:
    for vinyl in vendidas:
        print(f"ID: {vinyl['id']} | Álbum: {vinyl['name']} | Precio: {vinyl['price']}€")

if not vendidas:
    print("No hay piezas vendidas en este momento.")