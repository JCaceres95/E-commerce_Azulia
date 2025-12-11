def listar_productos(catalogo):
    """Muestra todos los productos del catálogo."""
    print("\n--- CATÁLOGO DE JOYAS ---")
    for id_prod, datos in catalogo.items():
        print(
            "ID:", id_prod,
            "| Nombre:", datos["nombre"],
            "| Categoría:", datos["categoria"],
            "| Precio: $", datos["precio"]
        )
