<div align="center">

<!-- Banner dinámico limpio solo con el título principal -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:ff007f,50:7928ca,100:00ffcc&height=180&section=header&text=VINYL%20CATALOG%20CHALLENGE&fontSize=38&fontColor=ffffff&fontAlign=50&animation=fadeIn" width="100%" />

<p>
  <img src="https://img.shields.io/badge/PYTHON-3.x_--_GROOVE_ON-ff007f?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/STATUS-EN_LA_PISTA_💃-00ffcc?style=for-the-badge&logoColor=black" alt="Status">
  <img src="https://img.shields.io/badge/CLEAN_CODE-NO_ELSE_🕺-7928ca?style=for-the-badge" alt="Clean Code">
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
Construir una herramienta de línea de comandos (CLI) eficiente y con una marcada identidad retro para gestionar un catálogo básico de discos de vinilo coleccionables. El sistema integra filtros avanzados, cálculo de métricas financieras, manipulación de cadenas de texto y un control estricto de validación de entradas de usuario, cumpliendo estrictamente con buenas prácticas de desarrollo y **sin utilizar ni una sola sentencia `else`**.

---

## 📂 Contexto del Catálogo
El programa administra un inventario inspirado en la época dorada de la música analógica, estructurado en memoria bajo la colección principal llamada `catalog`. Cada pieza recopila su identificador único (`id`), nombre del álbum/artista (`name`), categoría musical (`category`), precio de referencia (`price`), estado operativo (`status` - *disponible*, *reservada*, *vendida*) y una descripción detallada (`description`) que certifica su autenticidad mediante palabras clave obligatorias (*'usada'* o *'certificada'*).

---

## 🚀 Funcionalidades Implementadas

* **Registro con Validación Robusta (Partes 1 - 3 & 12):** Captura de 10 piezas coleccionables asegurando que no existan nombres vacíos, aplicando control de excepciones (`try-except`) para precios numéricos estrictamente mayores a cero, y filtrando estados y palabras clave obligatorias en las descripciones.
* **Gestión Dinámica de Categorías (Parte 4):** Extracción automatizada de categorías mediante *Sets* para eliminar duplicados y contabilizar la variedad musical del inventario.
* **Filtrado Avanzado (Partes 6 & 7):** Consultas personalizadas para aislar piezas según su estado operativo y filtrado dinámico por umbrales de precio mínimo ingresados por el usuario.
* **Evaluación Lógica (Parte 8):** Reglas de negocio automatizadas para determinar la elegibilidad de publicación de piezas, necesidades de revisión y control de inventario no vendido.
* **Manipulación de Strings (Parte 9):** Normalización de texto, formato de títulos, concatenación segura, interpolación con f-strings y procesamiento de listas de etiquetas separadas por comas.
* **Métricas y Enumeración Consecutiva (Parte 11):** Conteo automatizado por estados, cálculo de la suma total de precios, obtención del precio promedio y generación de listas ordenadas mediante `enumerate()`.
* **Menú Interactivo CLI (Parte 10):** Interfaz de navegación continua basada en bucles `while` con control de opciones inválidas y salida segura.

---

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

¡Gracias por utilizar el gestor de vinilos! Saliendo del programa...inyl-catalog-challenge

🛠️ Tecnologías Utilizadas
Lenguaje: Python 3.x

Control de versiones: Git & GitHub (Historial estructurado bajo los estándares de Conventional Commits).

Entorno de ejecución: Terminal CLI / Visual Studio Code.

```
## ⚙️ Cómo Ejecutar el Programa

Clona este repositorio en tu equipo local:

```bash
git clone [https://github.com/tu-usuario/vinyl-catalog-challenge.git](https://github.com/tu-usuario/vinyl-catalog-challenge.git)
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

