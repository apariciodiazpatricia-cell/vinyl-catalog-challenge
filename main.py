# Main file for the vinyl catalog system
catalogName = "Vinyl Catalog Challenge"
welcomeMessage = "¡Bienvenido al catálogo de vinilos coleccionables!"


print(welcomeMessage)




print("\n--- Registro de Nuevo Vinilo ---")



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


catalogCategories = {vinylCategory}

print("\n--- Información de Categorías ---")
print(f"Categorías únicas en el catálogo: {catalogCategories}")
print(f"Cantidad de categorías diferentes: {len(catalogCategories)}")



catalog = []

#Modificado para integrar la lógica de la parte 12

for i in range(10):
    print(f"\n--- Registro de Vinilo {i + 1} de 10 ---")

    vinylId = input("Introduce el identificador del vinilo (ej. V01): ")


    vinylName = ""
    while not vinylName.strip():
        vinylName = input("Introduce el nombre del álbum/artista: ")
        if not vinylName.strip():
            print("Error: El nombre no puede estar vacío.")

    vinylCategory = input("Introduce la categoría (ej. Rock, Pop): ")


    vinylPrice = None
    while vinylPrice is None:
        try:
            precio_temp = float(input("Introduce el precio (ej. 45.0): "))
            if precio_temp > 0:
                vinylPrice = precio_temp
            if precio_temp <= 0:
                print("Error: El precio debe ser mayor que cero.")
        except ValueError:
            print("Error: Debes introducir un valor numérico válido.")


    estados_permitidos = ["disponible", "reservada", "vendida"]
    vinylStatus = ""
    while vinylStatus not in estados_permitidos:
        vinylStatus = input("Introduce el estado (disponible/reservada/vendida): ").strip().lower()
        if vinylStatus not in estados_permitidos:
            print("Error: Estado no válido. Debe ser 'disponible', 'reservada' o 'vendida'.")

    vinylDescription = ""
    while not ("usada" in vinylDescription.lower() or "certificada" in vinylDescription.lower()):
        vinylDescription = input("Introduce la descripción (debe incluir 'usada' o 'certificada'): ")
        if not ("usada" in vinylDescription.lower() or "certificada" in vinylDescription.lower()):
            print("Error: La descripción debe contener 'usada' o 'certificada'.")



    vinylItem = {
        "id": vinylId,
        "name": vinylName,
        "category": vinylCategory,
        "price": vinylPrice,
        "status": vinylStatus,
        "description": vinylDescription
    }


    catalog.append(vinylItem)
    print("¡Vinilo guardado con éxito en el catálogo!")





print("       CATÁLOGO COMPLETO DE VINILOS COLECCIONABLES")


for vinyl in catalog:
    print(
        f"ID: {vinyl['id']} | Álbum: {vinyl['name']} | Categoría: {vinyl['category']} | Precio: {vinyl['price']}€ | Estado: {vinyl['status']}")



catalogCategories = {vinyl['category'] for vinyl in catalog}

print("\n--- Resumen de Categorías ---")

print(f"Categorías únicas en el catálogo: {catalogCategories}")
print(f"Cantidad de categorías diferentes: {len(catalogCategories)}")
print(f"Cantidad total de piezas en el catálogo: {len(catalog)}")





print("             FILTRADO POR ESTADOS                 ")



print("\n--- Piezas en estado: DISPONIBLE ---")
disponibles = [vinyl for vinyl in catalog if vinyl['status'].lower() == 'disponible']

if disponibles:
    for vinyl in disponibles:
        print(f"ID: {vinyl['id']} | Álbum: {vinyl['name']} | Precio: {vinyl['price']}€")

if not disponibles:
    print("No hay piezas disponibles en este momento.")


print("\n--- Piezas en estado: RESERVADA ---")
reservadas = [vinyl for vinyl in catalog if vinyl['status'].lower() == 'reservada']

if reservadas:
    for vinyl in reservadas:
        print(f"ID: {vinyl['id']} | Álbum: {vinyl['name']} | Precio: {vinyl['price']}€")

if not reservadas:
    print("No hay piezas reservadas en este momento.")


print("\n--- Piezas en estado: VENDIDA ---")
vendidas = [vinyl for vinyl in catalog if vinyl['status'].lower() == 'vendida']

if vendidas:
    for vinyl in vendidas:
        print(f"ID: {vinyl['id']} | Álbum: {vinyl['name']} | Precio: {vinyl['price']}€")

if not vendidas:
    print("No hay piezas vendidas en este momento.")


print("\n=== FILTRADO DE VINILOS POR PRECIO MÍNIMO ===")

min_price = None
while min_price is None:
    try:
        min_price = float(input("Introduce el precio mínimo deseado (€): "))
    except ValueError:
        print("Error: Debes introducir un valor numérico válido (ej. 15.50).")

vinilos_filtrados = [vinyl for vinyl in catalog if vinyl["price"] > min_price]

if vinilos_filtrados:
    print(f"\nVinilos con un precio superior a {min_price}€:")
    for vinyl in vinilos_filtrados:
        print(
            f"ID: {vinyl['id']} | Álbum: {vinyl['name']} | Categoría: {vinyl['category']} | Precio: {vinyl['price']}€ | Estado: {vinyl['status']}")

if not vinilos_filtrados:
    print(f"No se encontraron piezas con un precio superior a {min_price}€.")


    print("          PARTE 8: OPERADORES LÓGICOS        ")


    for vinyl in catalog:
        # Regla de publicación: precio > 0 y estado disponible
        puede_publicarse = (vinyl["price"] > 0) and (vinyl["status"].lower() == "disponible")

        # Regla de revisión: estado reservada o vendida
        requiere_revision = (vinyl["status"].lower() == "reservada") or (vinyl["status"].lower() == "vendida")

        # Regla de piezas no vendidas: estado diferente de vendida
        no_vendida = vinyl["status"].lower() != "vendida"

        print(f"Álbum: {vinyl['name']} | Estado: {vinyl['status']}")
        print(f"  -> ¿Puede publicarse?: {puede_publicarse}")
        print(f"  -> ¿Requiere revisión?: {requiere_revision}")
        print(f"  -> ¿No está vendida?: {no_vendida}")
        print("-" * 45)


print("         PARTE 9: MANIPULACIÓN DE STRINGS    ")



if catalog:

    print("1. Concatenación:", "Álbum: " + catalog[0]["name"] + " | Categoría: " + catalog[0]["category"])


    print(
        f"2. Interpolación: Álbum: {catalog[0]['name']} | Precio: {catalog[0]['price']}€ | Estado: {catalog[0]['status']}")


    descripcion_original = catalog[0]["description"]
    descripcion_modificada = descripcion_original.replace("usada", "certificada")
    print(f"5. Descripción modificada: {descripcion_modificada}")


    nombre_normalizado = catalog[0]["name"].strip().title()
    print(f"8. Nombre de pieza normalizado: {nombre_normalizado}")


tags_input = input("Introduce etiquetas separadas por comas (ej. retro,anime,limited): ")
lista_tags = [tag.strip() for tag in tags_input.split(",")]
print(f"4. Elementos separados (lista de etiquetas): {lista_tags}")


username = input("Introduce un nombre de usuario para formatear: ")
print(f"  - Sin espacios (strip): '{username.strip()}'")
print(f"  - En minúsculas (lower): {username.lower()}")
print(f"  - En mayúsculas (upper): {username.upper()}")
print(f"  - En formato título (title): {username.title()}")


# Por sentido común (parte 11 por delante de la 10)

print("        PARTE 11: MÉTRICAS DEL CATÁLOGO      ")


cantidad_disponibles = len([vinyl for vinyl in catalog if vinyl["status"].lower() == "disponible"])
cantidad_reservadas = len([vinyl for vinyl in catalog if vinyl["status"].lower() == "reservada"])
cantidad_vendidas = len([vinyl for vinyl in catalog if vinyl["status"].lower() == "vendida"])


cantidad_total = len(catalog)


suma_precios = 0.0
promedio_precios = 0.0

if catalog:
    suma_precios = sum(vinyl["price"] for vinyl in catalog)
    promedio_precios = suma_precios / len(catalog)


print(f"1. Cantidad de piezas disponibles: {cantidad_disponibles}")
print(f"2. Cantidad de piezas reservadas: {cantidad_reservadas}")
print(f"3. Cantidad de piezas vendidas: {cantidad_vendidas}")
print(f"4. Cantidad total de piezas: {cantidad_total}")
print(f"5. Suma total de los precios: {suma_precios:.2f}€")
print(f"6. Precio promedio del catálogo: {promedio_precios:.2f}€")


print("\n--- Listado Consecutivo de Álbumes ---")
for indice, vinyl in enumerate(catalog, start=1):
    print(f"{indice}. {vinyl['name']}")


print("        PARTE 10: MENÚ INTERACTIVO           ")

opcion = ""
while opcion != "4":
    print("\n--- MENÚ DE CATÁLOGO DE VINILOS ---")
    print("1. Mostrar todas las piezas")
    print("2. Mostrar solo las piezas disponibles")
    print("3. Mostrar el precio promedio")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")


    if opcion == "1":
        print("\n--- Catálogo Completo ---")
        for vinyl in catalog:
            print(
                f"ID: {vinyl['id']} | Álbum: {vinyl['name']} | Categoría: {vinyl['category']} | Precio: {vinyl['price']}€ | Estado: {vinyl['status']}")


    if opcion == "2":
        print("\n--- Piezas Disponibles ---")
        for vinyl in catalog:
            if vinyl["status"].lower() == "disponible":
                print(f"ID: {vinyl['id']} | Álbum: {vinyl['name']} | Precio: {vinyl['price']}€")


    if opcion == "3":
        if catalog:
            suma_precios = sum(vinyl["price"] for vinyl in catalog)
            promedio = suma_precios / len(catalog)
            print(f"\nPrecio promedio del catálogo: {promedio:.2f}€")
        if not catalog:
            print("\nEl catálogo está vacío, no se puede calcular el promedio.")


    if opcion == "4":
        print("\n¡Gracias por utilizar el gestor de vinilos! Saliendo del programa...")


    if opcion not in ["1", "2", "3", "4"]:
        print("\nError: Opción no válida. Por favor, introduce un número entre 1 y 4.")


