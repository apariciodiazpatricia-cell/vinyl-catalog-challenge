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