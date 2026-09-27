Documentación Técnica del Proyecto: Catálogo de Piezas Coleccionables (CLI)
1. Resumen Ejecutivo y Visión General
El proyecto Vinyl Catalog CLI / Catálogo de Coleccionables es una herramienta de línea de comandos (CLI) desarrollada en Python orientada a cumplir con los requerimientos del Reto Python Nivel I: Catálogo Básico de Coleccionables. Su propósito principal es permitir la gestión digital de un inventario de 10 piezas coleccionables, aplicando validaciones estrictas de datos, filtros avanzados por estados y precios, operadores lógicos para reglas de negocio, manipulación de cadenas de texto y una presentación visual inmersiva de estilo neón/synthwave.

2. Objetivos Académicos y del Proyecto
Eficiencia en CLI: Proveer una interfaz de comandos fluida, intuitiva y estructurada por consola que cubra los tres niveles de exigencia del reto (registro, operadores/filtros y menú interactivo/métricas).

Filosofía de Código Limpio (Clean Code): Aplicar buenas prácticas de desarrollo estrictas, destacando la ausencia deliberada de estructuras de bifurcación condicional anidada (no-else return) para mejorar la legibilidad y reducir la complejidad ciclomática.

Gestión de Reglas de Negocio: Implementar validaciones de integridad de datos (precios numéricos positivos, estados restringidos y palabras clave obligatorias como usada o certificada en las descripciones).

3. Arquitectura y Decisiones de Diseño (Los "Porqués")
¿Por qué Python para la lógica de la CLI?
Tipado dinámico y versatilidad: Permite gestionar estructuras complejas (como la lista principal catalog con diccionarios y conjuntos set para categorías únicas) de forma nativa, limpia y rápida.

Ecosistema robusto: Facilita la implementación de funciones de orden superior (filter, map), manipulación avanzada de strings y control de flujos iterativos.

¿Por qué el principio "No-Else"?
Reducción de indentación: Al eliminar las sentencias else mediante la técnica de guard clauses (validaciones tempranas y errores anticipados), el flujo de ejecución se lee de manera lineal de arriba a abajo.

Mantenibilidad y Robustez: Facilita la validación de entradas de usuario (Nivel III) sin anidamientos excesivos, simplificando la depuración de errores (debugging).

4. Guía de Implementación por Niveles (Funcionamiento del Sistema)
NIVEL I – Registro de piezas y estructuras base
Partes 1 a 3 (Inicialización y Captura): El programa inicia mostrando un mensaje de bienvenida al sistema de coleccionables. Acto seguido, ejecuta un flujo de captura por terminal para registrar exactamente 10 piezas coleccionables. Cada una almacena su identificador (id), nombre, categoría, precio decimal, estado y una descripción validada. Todo se almacena en la estructura principal catalog.

Partes 4 y 5 (Categorías y Visualización): Se procesa un conjunto (set) para extraer las categorías únicas de forma automatizada, eliminando duplicados y midiendo la variedad de la colección. Finalmente, se recorre el catálogo mostrando la información tabular de cada pieza junto con las métricas generales.

NIVEL II – Filtros, operadores y strings
Partes 6 y 7 (Filtros por Estado y Precio): El sistema permite filtrar dinámicamente las piezas según su estado actual (disponible, reservada, vendida) y aplicar consultas de precio mínimo introducido por el usuario mediante validación numérica.

Parte 8 (Operadores Lógicos y Reglas de Negocio):

Regla de publicación: Evalúa si el precio es mayor a cero y su estado es disponible.

Regla de revisión: Identifica si la pieza está reservada o vendida.

Filtro de no vendidas: Extrae los elementos que no posean el estado de venta final.

Parte 9 (Manipulación de Strings): Se realizan operaciones avanzadas de cadenas: concatenación, interpolación, separación de etiquetas introducidas por comas (retro,anime,limited), reemplazo de la palabra usada por certificada, normalización de nombres de usuario (eliminación de espacios, minúsculas, mayúsculas y formato título) y normalización de los títulos de las piezas.

NIVEL III – Bucles, menú y métricas
Partes 10 a 12 (Menú Interactivo, Métricas y Validaciones):

Menú Interactivo: Maneja un bucle de ejecución continua con opciones para mostrar el catálogo completo, filtrar piezas disponibles, calcular el precio promedio y salir de forma controlada, manejando opciones no válidas sin romper la ejecución.

Métricas y Enumeración: Calcula de forma automatizada la cantidad de piezas por estado, la suma total de precios, el promedio general y lista los elementos con una posición consecutiva enumerada (ej. 1. Figura Dragon Red).

Validaciones Robustas: Aplica filtros estrictos para asegurar que los precios sean mayores a cero, los nombres no estén vacíos, los estados pertenezcan al conjunto permitido y las descripciones incluyan obligatoriamente las palabras clave usada o certificada.

5. Stack Tecnológico y Justificación Detallada
5.1. Núcleo de Desarrollo
Python (Versión 3.x): Elegido por su sintaxis clara, agilidad en la gestión de entradas/salidas por consola y potencia nativa en el manejo de colecciones de datos.

5.2. Arquitectura y Buenas Prácticas
Paradigma Clean Code y Guard Clauses ("No-Else"): Vital para asegurar un código legible, mantenible y con baja complejidad ciclomática al validar restricciones de negocio complejas.

5.3. Control de Versiones e Integración
Git, GitHub y Conventional Commits: Control de versiones distribuido con un historial estructurado en 15 commits profesionales, asegurando la trazabilidad de cada fase del desarrollo.

Presentación Visual Synthwave / Cyberpunk: Uso de un README.md optimizado con insignias, tablas y marquesinas fluidas que garantizan una experiencia visual atractiva y sin fallos de renderizado en GitHub.

6. Conclusiones
El desarrollo del Vinyl Catalog CLI demuestra cómo una aplicación basada en consola puede estructurarse de manera profesional y robusta cumpliendo estrictamente con todas las especificaciones de negocio, control de errores y principios de ingeniería de software limpia. El proyecto se presenta en un formato de repositorio optimizado e listo para su evaluación académica.

📋 Documentación Técnica del Proyecto: Catálogo de Piezas Coleccionables (Nivel 2)
1. Resumen Ejecutivo y Visión General
El proyecto Catálogo de Piezas Coleccionables (Vinyl Catalog Challenge) es una aplicación de línea de comandos (CLI) desarrollada en Python bajo una arquitectura modular y limpia. Su objetivo es la gestión integral de un inventario de piezas aplicando validaciones estrictas de datos mediante funciones atómicas, manejo profesional de excepciones (try-except y raise), filtrados avanzados por estados y precios, métricas estadísticas y un menú interactivo robusto que garantiza la estabilidad absoluta del sistema.

2. Objetivos Académicos y del Proyecto
Arquitectura Modular y Separación de Responsabilidades: Desacoplar la lógica en tres módulos (main.py, catalog.py y validations.py) para evitar la duplicación de código y asegurar la mantenibilidad.

Manejo Robusto de Errores (raise y ValueError): Interceptar entradas incorrectas mediante validaciones tempranas y excepciones descriptivas que evitan la caída del programa (exit code 1).

Control de Versiones Profesional: Mantener un historial de commits limpio y estandarizado en inglés mediante el estándar de Conventional Commits.

3. Arquitectura y Decisiones de Diseño
Diseño Multimodular:

validations.py: Funciones de validación puras de responsabilidad única.

catalog.py: Lógica de negocio (inserción, búsquedas por ID, eliminaciones seguras, resúmenes por categorías y filtros).

main.py: Orquesta la interfaz de consola, los bucles de control y el menú interactivo (opciones 1 a 8).

Flujo Controlado con Bucles y Excepciones: Las entradas por consola están encapsuladas en bucles while combinados con bloques try-except, obligando al usuario a introducir datos válidos sin interrumpir la ejecución.

4. Auditoría, Comprobaciones y Verificación al 100%
Durante la fase de pruebas y despliegue del proyecto en la rama feature/level-2, se han verificado y auditado sistemáticamente los siguientes puntos críticos, garantizando un funcionamiento impecable:

Gestión de Errores de Entrada (Sanitización):

Comprobado que introducir precios no numéricos (ej. "treinta", "hbjh") activa correctamente el bloque try-except de validate_price, mostrando el mensaje de error descriptivo sin romper la aplicación.

Validación estricta de que los precios introducidos sean estrictamente mayores a cero.

Restricción de Estados:

Verificado que estados no permitidos (ej. "no se") sean rechazados de inmediato por validate_status, restringiendo los valores exclusivamente al conjunto permitido: disponible, reservada, vendida.

Control de Palabras Clave Obligatorias:

Comprobado que la función validate_description rechaza descripciones que no incluyan obligatoriamente los términos clave usada o certificada.

Navegación e Integridad del Menú Interactivo:

Auditoría completa de las opciones del menú (1 a 8): adición de piezas, cálculo correcto de resúmenes por categoría, filtrados dinámicos por estado, obtención del precio promedio con protección contra división por cero, verificación de existencia y eliminación segura de registros por ID.

Trazabilidad del Código (Git & Conventional Commits):

Historial de versiones estructurado mediante commits limpios y detallados en inglés para la gestión de importaciones, corrección de errores de flujo, incorporación de validaciones y refactorización del menú.

5. Stack Tecnológico
Lenguaje: Python 3.10+

Control de Versiones: Git y GitHub (Conventional Commits en inglés).

Entorno de Trabajo: PyCharm / Visual Studio Code con soporte para entorno virtual (.venv).

6. Instrucciones de Ejecución
Clona el repositorio y sitúate en la rama de trabajo (feature/level-2).

Abre la terminal integrada en la raíz del proyecto y activa el entorno virtual (.venv).

Ejecuta el programa principal con el comando:

Bash
python main.py
Interactúa con el menú por consola introduciendo las opciones numéricas del 1 al 8 para administrar el catálogo de vinilos.

## 🧪 8. Arquitectura de Pruebas Automatizadas (Testing Suite)

El proyecto incluye una robusta suite de **40 pruebas unitarias y funcionales** implementadas con **PyTest**, asegurando la cobertura total, la estabilidad del negocio y la integridad de las entradas de datos.

### 📋 Estructura de Módulos de Prueba
- **`test/test_validations.py` (25 tests)**:
  - Valida la restricción de campos no vacíos (`validate_not_empty`) controlando nulos, espacios y tipos incorrectos.
  - Comprueba precios válidos (`validate_price`) rechazando valores negativos, ceros, booleanos y cadenas no numéricas.
  - Verifica los estados permitidos (`validate_status`) con normalización automática de mayúsculas y espacios.
  - Somete a prueba las descripciones (`validate_description`) exigiendo la presencia obligatoria de las palabras clave *"usada"* o *"certificada"*.
  - Utiliza decoradores avanzados como `@pytest.mark.parametrize` y el control de excepciones `pytest.raises`.

- **`test/test_catalog.py` (15 tests)**:
  - Comprueba la correcta inserción de piezas con limpieza de espacios mediante `add_piece`.
  - Incorpora una validación estricta para evitar y detectar IDs duplicados (lanzando `ValueError`).
  - Evalúa la búsqueda exitosa y nula por identificador (`find_piece_by_id`).
  - Valida la eliminación lógica de elementos (`remove_piece`) y el cálculo seguro del precio promedio (`get_average_price`) con protección contra catálogos vacíos.
  - Utiliza fixtures de PyTest (`@pytest.fixture`) para inicializar catálogos limpios de prueba.

### ⚡ Ejecución de la Suite
Para ejecutar el entorno de pruebas completo o módulos específicos desde la terminal con el entorno virtual activo:
```bash
# Ejecutar todas las pruebas con detalle (verbose)
$env:PYTHONPATH="."; pytest -v

# Ejecutar únicamente las pruebas del catálogo
$env:PYTHONPATH="."; pytest test/test_catalog.py -v

# Ejecutar únicamente las pruebas de validaciones
$env:PYTHONPATH="."; pytest test/test_validations.py -v