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
    vinylPrice = None
    while vinylPrice is None:
        try:
            vinylPrice = float(input("Introduce el precio (ej. 45.0): "))
        except ValueError:
            print("Error: Debes introducir un valor numérico válido para el precio.")
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


    # --- Parte 7: Filtrar piezas por precio mínimo con validación numérica ---
print("\n=== FILTRADO DE VINILOS POR PRECIO MÍNIMO ===")

# Validamos que el valor introducido sea numérico sin usar 'else'
min_price = None
while min_price is None:
    try:
        min_price = float(input("Introduce el precio mínimo deseado (€): "))
    except ValueError:
        print("Error: Debes introducir un valor numérico válido (ej. 15.50).")

# Filtramos los vinilos cuyo precio sea estrictamente superior al introducido
vinilos_filtrados = [vinyl for vinyl in catalog if vinyl["price"] > min_price]

if vinilos_filtrados:
    print(f"\nVinilos con un precio superior a {min_price}€:")
    for vinyl in vinilos_filtrados:
        print(
            f"ID: {vinyl['id']} | Álbum: {vinyl['name']} | Categoría: {vinyl['category']} | Precio: {vinyl['price']}€ | Estado: {vinyl['status']}")

if not vinilos_filtrados:
    print(f"No se encontraron piezas con un precio superior a {min_price}€.")



print("\n=============================================")
print("          PARTE 8: OPERADORES LÓGICOS        ")
print("=============================================")

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

    # --- Parte 9: Manipulación de strings ---
    print("\n=============================================")
    print("         PARTE 9: MANIPULACIÓN DE STRINGS    ")
    print("=============================================")

    # Evaluamos de forma segura si el catálogo tiene elementos sin usar 'else'
    if catalog:
        # 1. Mostrar la información de una pieza utilizando concatenación (+)
        print("1. Concatenación:", "Álbum: " + catalog[0]["name"] + " | Categoría: " + catalog[0]["category"])

        # 2. Mostrar la información de una pieza utilizando interpolación (f-strings)
        print(
            f"2. Interpolación: Álbum: {catalog[0]['name']} | Precio: {catalog[0]['price']}€ | Estado: {catalog[0]['status']}")

        # 5. Reemplazar la palabra 'usada' por 'certificada' en una descripción
        descripcion_original = catalog[0]["description"]
        descripcion_modificada = descripcion_original.replace("usada", "certificada")
        print(f"5. Descripción modificada: {descripcion_modificada}")

        # 8. Normalizar el nombre de una pieza antes de mostrarlo (quitando espacios y aplicando formato título)
        nombre_normalizado = catalog[0]["name"].strip().title()
        print(f"8. Nombre de pieza normalizado: {nombre_normalizado}")

    # 3 y 4. Solicitar cadena de etiquetas separadas por comas y convertirlas en lista
    tags_input = input("Introduce etiquetas separadas por comas (ej. retro,anime,limited): ")
    lista_tags = [tag.strip() for tag in tags_input.split(",")]
    print(f"4. Elementos separados (lista de etiquetas): {lista_tags}")

    # 6 y 7. Solicitar un nombre de usuario y mostrarlo con distintos formatos de string
    username = input("Introduce un nombre de usuario para formatear: ")
    print(f"  - Sin espacios (strip): '{username.strip()}'")
    print(f"  - En minúsculas (lower): {username.lower()}")
    print(f"  - En mayúsculas (upper): {username.upper()}")
    print(f"  - En formato título (title): {username.title()}")

