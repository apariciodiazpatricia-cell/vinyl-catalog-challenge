📚 Documentación Técnica Completa: Catálogo de Piezas Coleccionables (Vinyl Catalog CLI)
1. Resumen Ejecutivo y Visión General
El proyecto Vinyl Catalog CLI (vinyl-catalog-challenge) es una aplicación avanzada de línea de comandos (CLI) desarrollada en Python. Su objetivo es la gestión digital integral de un inventario de piezas coleccionables (vinilos), aplicando un estándar de calidad profesional basado en Clean Code, validaciones estrictas de datos, manejo de excepciones, filtrados dinámicos, métricas estadísticas y una robusta suite de pruebas automatizadas.

El proyecto se ha construido en dos grandes fases evolutivas:

Reto 1: Enfoque centralizado e interactivo en consola mediante un script principal (main.py).

Reto 2: Evolución hacia una arquitectura modular, refactorización de código, validaciones atómicas mediante bloques de control de excepciones (raise / try-except), especificación de comportamiento en Gherkin y pruebas unitarias con PyTest.

2. Objetivos Académicos y de Ingeniería
Arquitectura Modular (Clean Architecture): Desacoplar gradualmente el código para separar la interfaz de usuario, la lógica de negocio y los validadores de datos.

Filosofía de Código Limpio: Aplicar buenas prácticas como el uso de funciones atómicas, nombres descriptivos y la reducción de complejidad mediante validaciones tempranas (Guard Clauses).

Robustez y Manejo de Errores: Interceptar entradas de usuario incorrectas mediante excepciones descriptivas (ValueError), previniendo caídas imprevistas del programa (crash).

Calidad y Verificación (Testing): Garantizar la inmunidad del código ante fallos mediante una suite de pruebas automatizadas y especificaciones formales de comportamiento.

3. Arquitectura y Decisiones de Diseño (Los "Porqués")
💡 ¿Por qué Python para la lógica de la CLI?
Tipado dinámico y versatilidad: Permite gestionar estructuras complejas de datos nativas (como listas de diccionarios para el catálogo o conjuntos set para extraer categorías únicas sin duplicados).

Ecosistema y control de flujos: Facilita la manipulación avanzada de cadenas de texto (strings) y la implementación de operaciones iterativas eficientes.

💡 Evolución de la Estructura (Del Reto 1 al Reto 2)
Reto 1 (main.py monolítico): Todo el flujo de registro, captura de datos mediante input(), bucles de control while y estructuras de bifurcación condicional (if-elif-else) se concentraron inicialmente en un único archivo ejecutable para validar la lógica base de la CLI.

Reto 2 (Refactorización Modular): El código evolucionó hacia un diseño desacoplado en tres módulos independientes para cumplir con el principio de responsabilidad única:

main.py: Orquestador de la interfaz de consola, bucles y menú interactivo (opciones 1 a 8).

catalog.py: Núcleo de la lógica de negocio (inserciones, búsquedas por ID, eliminaciones seguras, resúmenes por categorías y filtros avanzados).

validations.py: El guardián de datos, encargado de las funciones atómicas de saneamiento y restricciones mediante raise.

4. Guía de Implementación por Fases
🚀 FASE 1: RETO 1 – Lógica Inicial y Menú en Consola (main.py)
Captura y Registro: Inicialización de un catálogo estructurado para almacenar coleccionables, exigiendo identificador (id), nombre, categoría, precio decimal, estado y descripción validada.

Estructuras de Control y Menú: Uso de bucles continuos combinados con menús interactivos por consola para añadir piezas, consultar listados, extraer categorías mediante sets y mostrar métricas generales.

Manipulación de Cadenas: Aplicación de operaciones sobre textos (concatenación, interpolación con f-strings, normalización de mayúsculas/minúsculas y reemplazos de términos).

⚙️ FASE 2: RETO 2 – Refactorización, Validaciones y Testing
Sanitización de Entradas: Bloqueo de precios no numéricos o menores/iguales a cero mediante bloques try-except.

Restricción de Estados: Limitación exclusiva de los estados operativos a los valores permitidos (disponible, reservada, vendida).

Control de Palabras Clave: Exigencia obligatoria de los términos "usada" o "certificada" en la descripción de cada pieza.

5. Especificación de Comportamiento (Gherkin / BDD)
Para documentar formalmente las reglas de validación y la lógica del sistema incorporadas en el Reto 2, se definen los siguientes escenarios bajo la metodología Gherkin:

A. Módulo de Validaciones Atómicas (validations.py)
Característica: Validación estricta de entradas en el catálogo
  Como sistema, quiero verificar cada dato introducido por el usuario
  Para evitar registros incorrectos o fallos de ejecución.

  Escenario: Rechazo de campos vacíos o nulos
    Dado que el usuario introduce un campo de texto obligatorio vacío o con espacios en blanco
    Cuando el sistema ejecuta la función de validación de texto
    Entonces se interrumpe la ejecución lanzando un ValueError.

  Escenario: Restricción y validación de precios
    Dado que el usuario introduce un precio de referencia
    Cuando el sistema comprueba la regla numérica
    Entonces se acepta únicamente si es un número mayor estricto que cero, rechazando tipos booleanos, ceros o negativos.

  Escenario: Normalización de estados operativos
    Dado que el usuario introduce un estado para el vinilo
    Cuando el sistema procesa el estado
    Entonces se normalizan las minúsculas y espacios, rechazando cualquier valor ajeno a ("disponible", "reservada", "vendida").

  Escenario: Obligatoriedad de palabras clave en descripciones
    Dado que el usuario escribe la descripción del artículo
    Cuando el sistema valida el contenido
    Entonces se exige obligatoriamente la presencia de las palabras "usada" o "certificada".
    
## 6. Suite de Pruebas Automatizadas (`PyTest`)

El proyecto implementa una potente suite de pruebas unitarias para certificar la estabilidad absoluta del sistema:

| Módulo de Pruebas | Nivel de Cobertura | Aspectos Clave Verificados | Herramientas Principales |
| :--- | :---: | :--- | :--- |
| **`test/test_validations.py`** | 25 Tests | • Control estricto de nulos, cadenas vacías y tipos incorrectos.<br>• Validación de rangos numéricos y rechazo de booleanos.<br>• Normalización de estados y control de palabras clave obligatorias. | `@pytest.mark.parametrize`, `pytest.raises` |
| **`test/test_catalog.py`** | 15 Tests | • Inserción de piezas y bloqueo estricto de IDs duplicados.<br>• Búsquedas exitosas y nulas por identificador único.<br>• Eliminación lógica y cálculo robusto de promedios financieros. | `@pytest.fixture`, `pytest.raises` |

### ⚡ Instrucciones de Ejecución de las Pruebas
Para ejecutar la suite completa de pruebas desde la terminal con el entorno virtual activo y asegurando la ruta raíz del proyecto:
```bash
$env:PYTHONPATH="."; pytest -v
```
7. Stack Tecnológico
Lenguaje: Python 3.10+

Control de Versiones: Git & GitHub (Historial estricto bajo los estándares de Conventional Commits).

Entorno de Trabajo: PyCharm / Visual Studio Code con soporte para entorno virtual (.venv).

Framework de Testing: PyTest.

8. Glosario Técnico del Proyecto
Arquitectura Modular: Diseño de software basado en la división de responsabilidades en archivos independientes (catalog.py, validations.py, main.py).

BDD (Behavior-Driven Development): Desarrollo guiado por el comportamiento mediante especificaciones legibles en lenguaje natural (Gherkin).

CLI (Command Line Interface): Interfaz basada en terminal de comandos para la interacción directa con el usuario.

Concatenación: Acción de unir cadenas de texto utilizando el operador de suma (+).

Excepción (ValueError): Mecanismo de control de errores que interrumpe la ejecución anómala ante datos incorrectos.

Fixture: Función auxiliar de PyTest para inicializar un entorno limpio de datos antes de testear.

Gherkin: Lenguaje estructurado en texto plano basado en palabras clave (Given, When, Then).

Interpolación (f-strings): Inserción limpia de variables dentro de plantillas de texto usando llaves {}.

PYTHONPATH: Variable de entorno empleada para indicar a Python las rutas de importación de módulos en proyectos estructurados.

Raise: Instrucción utilizada para disparar una excepción de forma explícita ante un fallo de validación.

Scope (Ámbito): Contexto del código donde una variable o función es visible y accesible.    

