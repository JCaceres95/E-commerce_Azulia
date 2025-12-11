"""
Proyecto final Módulo 3 Ecommerce Azulia
Joyería en consola.
Alumna: Jeimy Caceres
"""

from menu import mostrar_menu
from listar import listar_productos
from buscar import buscar_productos
from carrito import (
    agregar_al_carrito,
    mostrar_carrito_y_total,
    vaciar_carrito,
)


def main():
    # Catálogo de joyas: id -> datos del producto
    catalogo = {
        1: {"nombre": "Anillo plata luna", "categoria": "anillos", "precio": 15990.0},
        2: {"nombre": "Collar cuarzo rosa", "categoria": "collares", "precio": 18990.0},
        3: {"nombre": "Aros acero minimal", "categoria": "aros", "precio": 9990.0},
        4: {"nombre": "Pulsera ojo de tigre", "categoria": "pulseras", "precio": 12990.0},
        5: {"nombre": "Anillo compromiso oro", "categoria": "anillos", "precio": 45990.0},
    }

    # Carrito: lista vacía al comenzar
    carrito = []

    opcion = ""

    # Menú principal con while
    while opcion != "0":
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            listar_productos(catalogo)

        elif opcion == "2":
            buscar_productos(catalogo)

        elif opcion == "3":
            agregar_al_carrito(catalogo, carrito)

        elif opcion == "4":
            mostrar_carrito_y_total(carrito)

        elif opcion == "5":
            vaciar_carrito(carrito)

        elif opcion == "0":
            print("Gracias por visitar la Joyería CLI. ¡Hasta luego!")

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
