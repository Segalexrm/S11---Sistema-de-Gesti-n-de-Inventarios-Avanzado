# main.py
from modelos.producto import Producto
from servicios.inventario import Inventario


def menu():
    # Al instanciar, automáticamente cargará lo que esté en inventario.txt
    sistema = Inventario()

    while True:
        print("\n= GESTIÓN DE INVENTARIO PERSISTENTE =")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Listar inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                id_p = input("ID único: ").strip()
                if not id_p: raise ValueError("El ID no puede estar vacio.")
                nom = input("Nombre: ")
                cant = int(input("Cantidad: "))
                pre = float(input("Precio: "))
                nuevo = Producto(id_p, nom, cant, pre)
                sistema.añadir_producto(nuevo)

            elif opcion == "2":
                id_p = input("ID del producto a eliminar: ")
                sistema.eliminar_producto(id_p)

            elif opcion == "3":
                id_p = input("ID del producto a actualizar: ")
                c_input = input("Nueva cantidad (Enter para omitir): ")
                p_input = input("Nuevo precio (Enter para omitir): ")

                cant = int(c_input) if c_input else None
                pre = float(p_input) if p_input else None
                sistema.actualizar_producto(id_p, cant, pre)

            elif opcion == "4":
                nom = input("Nombre a buscar: ")
                encontrados = sistema.buscar_por_nombre(nom)
                if encontrados:
                    for e in encontrados: print(e)
                else:
                    print("No se encontraron coincidencias.")

            elif opcion == "5":
                sistema.mostrar_inventario()

            elif opcion == "6":
                print("Hasta luego!")
                break
            else:
                print("Opción no válida.")

        except ValueError as e:
            print(f"Error de entrada: {e}. Asegúrese de usar números donde corresponda.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    menu()