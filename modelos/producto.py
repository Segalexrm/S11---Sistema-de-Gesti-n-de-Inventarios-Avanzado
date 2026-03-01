class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters
    @property
    def id(self): return self.__id

    @property
    def nombre(self): return self.__nombre

    @property
    def cantidad(self): return self.__cantidad

    @property
    def precio(self): return self.__precio

    # Setters
    @nombre.setter
    def nombre(self, valor): self.__nombre = valor

    @cantidad.setter
    def cantidad(self, valor): self.__cantidad = valor

    @precio.setter
    def precio(self, valor): self.__precio = valor

    def __str__(self):
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Stock: {self.__cantidad} | Precio: ${self.__precio:.2f}"

    def a_diccionario(self):
        """Facilita la serialización para el archivo."""
        return f"{self.__id},{self.__nombre},{self.__cantidad},{self.__precio}"