import os
from modelos.producto import Producto

class Inventario:
    def __init__(self, nombre_archivo="inventario.txt"):
        # Usamos un DICCIONARIO para búsqueda rápida por ID {id: objeto_producto}
        self.productos = {}
        self.archivo = nombre_archivo
        self.cargar_datos()

    def añadir_producto(self, producto):
        if producto.id in self.productos:
            print("Error: Ya existe un producto con ese ID.")
            return
        self.productos[producto.id] = producto
        self.guardar_datos()
        print("Producto añadido exitosamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_datos()
            print("Producto eliminado.")
        else:
            print("Error: No se encontró el ID.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None: self.productos[id_producto].cantidad = cantidad
            if precio is not None: self.productos[id_producto].precio = precio
            self.guardar_datos()
            print("Producto actualizado.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        # Usamos una lista por comprensión para filtrar coincidencias parciales
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        return encontrados

    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío.")
        for p in self.productos.values():
            print(p)

    # --- Persistencia de Datos ---
    def guardar_datos(self):
        try:
            with open(self.archivo, 'w', encoding='utf-8') as f:
                for p in self.productos.values():
                    f.write(p.a_diccionario() + "\n")
        except PermissionError:
            print("Error: No hay permisos para escribir el archivo.")

    def cargar_datos(self):
        if not os.path.exists(self.archivo): return
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                for linea in f:
                    id_p, nom, cant, pre = linea.strip().split(',')
                    self.productos[id_p] = Producto(id_p, nom, int(cant), float(pre))
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")