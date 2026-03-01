# modelos/producto.py

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id = id_producto  # Atributo privado
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters y Setters (Encapsulamiento)
    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, valor):
        if valor >= 0:
            self.__cantidad = valor

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        if valor >= 0:
            self.__precio = valor

    def __str__(self):
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"