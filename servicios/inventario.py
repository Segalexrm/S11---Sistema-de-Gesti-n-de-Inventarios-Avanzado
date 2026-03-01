# servicios/inventario.py
import os
from modelos.producto import Producto


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Carga los productos desde el archivo al iniciar el programa."""
        try:
            if not os.path.exists(self.archivo):
                # Si el archivo no existe, lo creamos vacío
                with open(self.archivo, 'w', encoding='utf-8') as f:
                    pass
                return

            with open(self.archivo, 'r', encoding='utf-8') as f:
                for linea in f:
                    # Suponemos formato: ID,Nombre,Cantidad,Precio
                    datos = linea.strip().split(',')
                    if len(datos) == 4:
                        id_p, nom, cant, pre = datos
                        nuevo_p = Producto(id_p, nom, int(cant), float(pre))
                        self.productos.append(nuevo_p)
        except FileNotFoundError:
            print(f"Aviso: El archivo {self.archivo} no fue encontrado. Se creará uno nuevo.")
        except PermissionError:
            print(f"Error: No tienes permisos para leer el archivo {self.archivo}.")
        except Exception as e:
            print(f"Error inesperado al cargar datos: {e}")

    def guardar_en_archivo(self):
        """Sobrescribe el archivo con la lista actual de productos (Persistencia)."""
        try:
            with open(self.archivo, 'w', encoding='utf-8') as f:
                for p in self.productos:
                    # Guardamos en formato CSV simple
                    f.write(f"{p.id},{p.nombre},{p.cantidad},{p.precio}\n")
        except PermissionError:
            print(f"Error crítico: No se pudo guardar en {self.archivo} por falta de permisos.")
        except Exception as e:
            print(f"Error al intentar escribir en el archivo: {e}")

    def añadir_producto(self, producto):
        if any(p.id == producto.id for p in self.productos):
            print(f"Error: El ID {producto.id} ya existe.")
            return False

        self.productos.append(producto)
        self.guardar_en_archivo()  # Sincronizar con archivo
        print(f"Producto '{producto.nombre}' añadido y guardado exitosamente.")
        return True

    def eliminar_producto(self, id_buscar):
        for p in self.productos:
            if p.id == id_buscar:
                self.productos.remove(p)
                self.guardar_en_archivo()  # Sincronizar con archivo
                print(f"Producto ID {id_buscar} eliminado del archivo.")
                return True
        print("Error: Producto no encontrado.")
        return False

    def actualizar_producto(self, id_buscar, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.id == id_buscar:
                if nueva_cantidad is not None: p.cantidad = nueva_cantidad
                if nuevo_precio is not None: p.precio = nuevo_precio
                self.guardar_en_archivo()  # Sincronizar con archivo
                print("Producto actualizado en el archivo.")
                return True
        print("Error: Producto no encontrado.")
        return False

    def buscar_por_nombre(self, nombre_parcial):
        return [p for p in self.productos if nombre_parcial.lower() in p.nombre.lower()]

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        for p in self.productos:
            print(p)