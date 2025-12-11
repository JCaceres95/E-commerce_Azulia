def agregar_al_carrito(catalogo, carrito):
    """
    Agrega un producto al carrito:
    - Pide ID del producto.
    - Pide cantidad (> 0).
    - Valida los datos sin usar try/except.
    """
    id_texto = input("Ingrese el ID de la joya que desea agregar: ")

    # Validar que el ID sea número
    if not id_texto.isdigit():
        print("ID inválido. Debe ser un número entero.")
        return

    id_producto = int(id_texto)

    if id_producto not in catalogo:
        print("El producto no existe en el catálogo.")
        return

    cantidad_texto = input("Ingrese la cantidad (> 0): ")

    # Validar que la cantidad sea número
    if not cantidad_texto.isdigit():
        print("Cantidad inválida. Debe ser un número entero.")
        return

    cantidad = int(cantidad_texto)

    if cantidad <= 0:
        print("La cantidad debe ser mayor que 0.")
        return

    producto = catalogo[id_producto]

    item_carrito = {
        "id": id_producto,
        "nombre": producto["nombre"],
        "precio": producto["precio"],
        "cantidad": cantidad
    }

    carrito.append(item_carrito)
    print("Joya agregada al carrito correctamente.")


def calcular_total(carrito):
    """
    Calcula y devuelve el total a pagar del carrito.
    Esta función recibe un parámetro y RETORNA un valor (float/int).
    """
    total = 0.0
    for item in carrito:
        subtotal = item["precio"] * item["cantidad"]
        total = total + subtotal
    return total


def mostrar_carrito_y_total(carrito):
    """Muestra los ítems del carrito y el total a pagar."""
    if len(carrito) == 0:
        print("\nEl carrito está vacío.")
        return

    print("\n--- CARRITO DE COMPRAS (JOYERÍA) ---")

    for item in carrito:
        subtotal = item["precio"] * item["cantidad"]
        print(
            "ID:", item["id"],
            "| Nombre:", item["nombre"],
            "| Cantidad:", item["cantidad"],
            "| Precio unitario: $", item["precio"],
            "| Subtotal: $", subtotal
        )

    total = calcular_total(carrito)
    print("\nTOTAL A PAGAR: $", total)


def vaciar_carrito(carrito):
    """Vacía todos los productos del carrito."""
    carrito.clear()
    print("El carrito ha sido vaciado correctamente.")
