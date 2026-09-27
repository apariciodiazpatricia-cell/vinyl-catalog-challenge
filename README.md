<div align="center">

<!-- Banner dinámico limpio solo con el título principal -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:ff007f,50:7928ca,100:00ffcc&height=180&section=header&text=VINYL%20CATALOG%20CHALLENGE&fontSize=38&fontColor=ffffff&fontAlign=50&animation=fadeIn" width="100%" />

<p>
  <img src="https://img.shields.io/badge/PYTHON-3.x_--_GROOVE_ON-ff007f?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/STATUS-EN_LA_PISTA_💃-00ffcc?style=for-the-badge&logoColor=black" alt="Status">
  <img src="https://img.shields.io/badge/GIT-COMMITS_AL_RITMO_🎵-ffb800?style=for-the-badge&logo=git&logoColor=black" alt="Git">
</p>
<div align="center">

  <!-- Banda deslizante de vinilos animados reales -->
  <marquee width="100%" behavior="alternate" scrollamount="6">
    <h1>💿 🎧 🎵 🎶 🎸 🪩 🔊 💿</h1>
  </marquee>

  <br>

  <!-- Tarjeta central de estilo tocadiscos neón -->
  <table border="0" cellspacing="0" cellpadding="15" style="background: rgba(255,0,127,0.05); border-radius: 15px;">
    <tr>
      <td align="center">
        <h2><font color="#ff007f">🎧 ZONA DE MEZCLAS - TOCADISCOS ACTIVE 🎧</font></h2>
        <p><em><font color="#00ffcc">⚡ "Cargando el amplificador... ¡Lógica impecable, código limpio y el mejor ritmo en cada surco!" ⚡</font></em></p>
      </td>
    </tr>
  </table>

  <br>

  <!-- Ecualizador inferior con movimiento -->
  <img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%" alt="Ondas de ritmo" />

</div>

</div>



## 🎯 Objetivo del Programa
Desarrollar una herramienta de línea de comandos (CLI) avanzada en Python estructurada bajo un modelo de **arquitectura modular**. Su propósito es la gestión integral de un inventario de piezas coleccionables (vinilos) aplicando validaciones estrictas de datos mediante funciones atómicas, manejo profesional de excepciones (`try-except` y `raise`), filtrados avanzados por estados y precios, métricas estadísticas y un menú interactivo robusto del 1 al 8 que garantiza la estabilidad absoluta del sistema.
---

## 📂 Contexto del Catálogo
El proyecto cumple estrictamente con el principio de separación de responsabilidades, desacoplando el código fuente en tres módulos independientes:

```text
catalogo_coleccionables/
├── catalog.py        -> Lógica de negocio, gestión de inventario, búsquedas, filtros y métricas.
├── validations.py    -> Módulo de validaciones atómicas con responsabilidad única (raise / ValueError).
├── main.py           -> Interfaz de usuario por consola, bucles de control y menú interactivo (1-8).
└── README.md         -> Documentación técnica completa del proyecto.

---
Cada pieza recopila su identificador único (id), nombre del álbum/artista (name), categoría musical (category), precio de referencia (price), estado operativo (status - disponible, reservada, vendida) y una descripción detallada (description) validada mediante palabras clave obligatorias ('usada' o 'certificada').
```
## 🚀 Funcionalidades Implementadas
Arquitectura Modular (Partes 1 - 11): Funciones optimizadas con parámetros y retorno, sin duplicación de lógica y con validaciones centralizadas en módulos externos.

Manejo de Errores con raise y ValueError (Parte 11): Funciones de validación tempranas (validate_price, validate_status, validate_description, validate_not_empty) que interceptan anomalías y previenen caídas del sistema (exit code 1).

Gestión Dinámica de Categorías y Resúmenes: Extracción automatizada mediante Sets y contadores analíticos agrupados por categorías.

Filtrado Avanzado y Precios Mínimos: Aislamiento de piezas por estado operativo estricto y consultas dinámicas superiores a umbrales numéricos.

Métricas y Estadísticas del Catálogo: Cálculo automatizado del precio promedio protegido contra división por cero y listados consecutivos mediante enumerate().

Menú Interactivo CLI Ampliado (Parte 12): Interfaz de navegación continua basada en bucles while y bloques try-except conectada de forma transparente con el backend (opciones 1 a 8).

---

🔍 Auditoría de Comprobaciones y Verificación al 100%
Durante la fase de auditoría técnica en la rama feature/level-2, se han verificado los siguientes puntos críticos:

Sanitización de Entradas: Introducir datos no numéricos en los precios activa correctamente el control de excepciones sin romper la aplicación.

Restricción de Estados y Keywords: Bloqueo inmediato de estados no permitidos y exigencia estricta de las palabras usada o certificada en las descripciones.

Estabilidad del Menú (1-8): Comprobación completa de adición, resúmenes, filtrados, promedios, verificación de existencia por ID y eliminación segura.

## 💻 Ejemplo de Interacción con el Programa

```text
==================================================
¡Bienvenido al catálogo de vinilos coleccionables!
==================================================

--- Registro de Vinilo 1 de 10 ---
Introduce el identificador del vinilo (ej. V01): V80
Introduce el nombre del álbum/artista: The Dark Side of the Moon
Introduce la categoría (ej. Rock, Pop): Rock Clásico
Introduce el precio (ej. 45.0): 45.0
Introduce el estado (disponible/reservada/vendida): disponible
Introduce la descripción (debe incluir 'usada' o 'certificada'): Edición original usada en buen estado
¡Vinilo guardado con éxito en el catálogo!

        PARTE 11: MÉTRICAS DEL CATÁLOGO      
=============================================
1. Cantidad de piezas disponibles: 6
2. Cantidad de piezas reservadas: 2
3. Cantidad de piezas vendidas: 2
4. Cantidad total de piezas: 10
5. Suma total de los precios: 457.00€
6. Precio promedio del catálogo: 45.70€

--- Listado Consecutivo de Álbumes ---
1. The Dark Side of the Moon
2. Thriller
3. Back in Black
...

=============================================
        PARTE 10: MENÚ INTERACTIVO           
=============================================
--- MENÚ DE CATÁLOGO DE VINILOS ---
1. Mostrar todas las piezas
2. Mostrar solo las piezas disponibles
3. Mostrar el precio promedio
4. Salir
Elige una opción (1-4): 4

¡Gracias por utilizar el gestor de vinilos! Saliendo del programa...

🛠️ Tecnologías Utilizadas
Lenguaje: Python 3.x

Control de versiones: Git & GitHub (Historial estructurado bajo los estándares de Conventional Commits).

==================================================
¡Bienvenido al sistema de gestión de catálogo!
==================================================
1. Agregar una pieza
2. Resumen del catálogo (por categoría)
3. Mostrar piezas por categoría
4. Mostrar piezas disponibles
5. Mostrar el precio promedio
6. Verificar si una pieza existe por ID
7. Eliminar una pieza por ID
8. Salir
Elige una opción (1-8): 1

--- AGREGAR NUEVA PIEZA ---
ID de la pieza: V01
Nombre: The Dark Side of the Moon
Categoría: Rock Clásico
Introduce el precio (ej. 45.0): 45.0
Introduce el estado (disponible / reservada / vendida): disponible
Introduce la descripción (debe incluir 'usada' o 'certificada'): Edición original usada en excelente estado

¡Éxito! Pieza agregada correctamente al catálogo.



```
🛠️ Tecnologías Utilizadas
Lenguaje: Python 3.10+

Control de versiones: Git & GitHub (Historial limpio estructurado bajo los estándares de Conventional Commits en inglés).

Entorno de Trabajo: PyCharm /soporte para entornos virtuales (.venv).

## ⚙️ Cómo Ejecutar el Programa

Clona este repositorio en tu equipo local:

```bash
git clone [https://github.com/apariciodiazpatricia-cell/vinyl-catalog-challenge.git](https://github.com/apariciodiazpatricia-cell/vinyl-catalog-challenge.git)
```
Accede al directorio del proyecto:

```bash
cd vinyl-catalog-challenge
```

Ejecuta el programa principal desde tu terminal:

```bash
python main.py
```

---

---
## 🧪 Pruebas Automatizadas con PyTest

El proyecto cuenta con una suite completa de **40 pruebas unitarias y funcionales** implementadas con `pytest`, garantizando la integridad de las operaciones, la robustez de las validaciones de entrada y el correcto funcionamiento de la lógica de negocio del catálogo[cite: 7].

### 📋 Cobertura de las Pruebas

| Archivo de Prueba | Tests | ¿Qué verifica? | Herramientas clave |
| :--- | :---: | :--- | :--- |
| **`test/test_validations.py`** | 25 | • **Campos no vacíos** (`validate_not_empty`): rechazo de cadenas vacías, espacios, `None` y tipos no string.<br>• **Precios válidos** (`validate_price`): números positivos, rechazo de $\le 0$, booleanos y tipos no numéricos.<br>• **Estados permitidos** (`validate_status`): normalización (`strip`, `lower`) y rechazo de estados inválidos.<br>• **Descripciones** (`validate_description`): presencia obligatoria de "usada" o "certificada". | `@pytest.mark.parametrize`, `pytest.raises` |
| **`test/test_catalog.py`** | 15 | • **Adición de piezas** con datos limpios y detección estricta de IDs duplicados.<br>• **Búsqueda** por ID existente e inexistente (`None`).<br>• **Eliminación** de piezas y retorno de estado booleano.<br>• **Cálculo de precio promedio** (`get_average_price`) y manejo seguro de catálogos vacíos. | `@pytest.fixture`, `pytest.raises` |

---

### ⚡ Comandos para Ejecutar las Pruebas

Para ejecutar la suite de pruebas desde la terminal integrada de PyCharm con el entorno virtual activo:

```bash
# Ejecutar toda la suite de pruebas detallada
$env:PYTHONPATH="."; pytest -v

# Ejecutar un módulo de pruebas específico
$env:PYTHONPATH="."; pytest test/test_catalog.py -v
$env:PYTHONPATH="."; pytest test/test_validations.py -v
```
🔄 Flujo de Datos y Arquitectura
El sistema está diseñado bajo una arquitectura modular y desacoplada, garantizando una separación clara de responsabilidades entre la interfaz de usuario, las reglas de negocio y los validadores de datos:
```
👤 Usuario
          │
          ▼
┌───────────────────┐
│     main.py       │ ← Menú interactivo de consola + manejadores (handlers)
└─────────┬─────────┘
          │
          ├────────────────────────────────┬────────────────────────────────┐
          ▼                                ▼                                ▼
  add_piece()                      list_pieces()                    filter_by_status()
  find_piece_by_id()               remove_piece()                   get_average_price()
  update_piece()                   get_catalog_summary()            filter_by_min_price()
          │                                │                                │
          └────────────────────────────────┼────────────────────────────────┘
                                           │
                                           ▼
                           ┌───────────────────────────────┐
                           │       validations.py          │ ← Guardián de datos y saneamiento
                           └───────────────┬───────────────┘
                                           │
                                           ▼
                           ┌───────────────────────────────┐
                           │      catalog: list of dicts   │ ← [{"id": "...", "name": "...", ...}]
                           └───────────────────────────────┘

```
                        
## 📬 Contacto y Redes

<div align="center">

<img src="https://github.com/apariciodiazpatricia-cell.png" alt="Patricia Aparicio Díaz" width="140" style="border-radius: 50%; border: 2px solid #ff007f;" />

### ¡Conecta conmigo!

[![GitHub](https://img.shields.io/badge/GitHub-apariciodiazpatricia--cell-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/apariciodiazpatricia-cell)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Patricia_Aparicio-0a66c2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/patriciaapariciodiaz/)
[![Portafolio](https://img.shields.io/badge/Portafolio-Web_Personal-ff007f?style=for-the-badge&logo=vercel&logoColor=white)](https://patricia-aparicio-dev.vercel.app/)
[![Linktree](https://img.shields.io/badge/Linktree-Mis_Enlaces-00ffcc?style=for-the-badge&logo=linktree&logoColor=black)](https://linktree-woad-tau.vercel.app/)

</div>

---

<div align="center">
  <sub>Desarrollado con 🎸, código limpio y mucho ritmo por Patricia Aparicio Díaz</sub>
</div>

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:ff007f,50:7928ca,100:00ffcc&height=150&section=footer&animation=fadeIn" width="100%" />
</div>

