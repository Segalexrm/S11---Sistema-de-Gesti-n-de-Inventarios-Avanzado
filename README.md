# Sistema Avanzado de Gestión de Inventario (Semana 12)

Este proyecto es un sistema de gestión de inventario desarrollado en **Python** aplicando los fundamentos de la **Programación Orientada a Objetos (POO)**. En esta versión avanzada, se han implementado colecciones de datos eficientes y persistencia mediante archivos de texto.

## Características Principales

- **POO Completa:** Uso de clases, encapsulamiento (atributos privados), getters y setters.
- **Colecciones Eficientes:** Uso de **Diccionarios** (`dict`) para optimizar la búsqueda, eliminación y actualización de productos mediante su ID único ($O(1)$).
- **Persistencia de Datos:** Carga y guardado automático en un archivo `inventario.txt`.
- **Manejo de Excepciones:** Validación de entradas de usuario y control de errores en la manipulación de archivos.
- **Modularización:** Separación clara entre modelos de datos, lógica de servicio y la interfaz de usuario.

---

## Estructura del Proyecto

```text
mi_proyecto/
│
├── modelos/
│   └── producto.py      # Clase Producto con sus atributos y métodos.
├── servicios/
│   └── inventario.py    # Lógica de gestión usando Diccionarios y Archivos.
├── main.py              # Interfaz de consola y menú interactivo.
└── inventario.txt       # Archivo de almacenamiento persistente (auto-generado).
