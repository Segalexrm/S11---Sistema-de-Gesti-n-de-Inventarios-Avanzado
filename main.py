from modelos.producto import Producto
from servicios.inventario import Inventario


def mostrar_menu():
    print("\n--- SISTEMA AVANZADO DE INVENTARIO (Semana 12) ---")
    print("1. Añadir Producto")
    print("2. Eliminar Producto")
    print("3. Actualizar Producto")
    print("4. Buscar Producto por Nombre")
    print("5. Mostrar Inventario Completo")
    print("6. Salir")


def ejecutar():
    inv = Inventario()
    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ")

        if opcion == "1":
            id_p = input("ID: ")
            nom = input("Nombre: ")
            cant = int(input("Cantidad: "))
            pre = float(input("Precio: "))
            inv.añadir_producto(Producto(id_p, nom, cant, pre))

        elif opcion == "2":
            id_p = input("Ingrese ID a eliminar: ")
            inv.eliminar_producto(id_p)

        elif opcion == "3":
            id_p = input("ID del producto: ")
            c = input("Nueva cantidad (Enter para omitir): ")
            p = input("Nuevo precio (Enter para omitir): ")
            inv.actualizar_producto(id_p, int(c) if c else None, float(p) if p else None)

        elif opcion == "4":
            nom = input("Nombre a buscar: ")
            resultados = inv.buscar_por_nombre(nom)
            for r in resultados: print(r)

        elif opcion == "5":
            inv.mostrar_todos()

        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    ejecutar()