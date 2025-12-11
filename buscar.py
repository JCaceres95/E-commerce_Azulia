def buscar_productos(catalogo):
    """
    Busca productos por nombre o categoría.
    El texto ingresado se compara con ambas cosas.
    """
    texto = input("\nIngrese texto a buscar (nombre o categoría): ").lower()
    encontrados = False  # bool para saber si hubo resultados

    print("\n--- RESULTADOS DE BÚSQUEDA ---")
    for id_prod, datos in catalogo.items():
        nombre = datos["nombre"].lower()
        categoria = datos["categoria"].lower()

        if texto in nombre or texto in categoria:
            print(
                "ID:", id_prod,
                "| Nombre:", datos["nombre"],
                "| Categoría:", datos["categoria"],
                "| Precio: $", datos["precio"]
            )
            encontrados = True

    if not encontrados:
        print("No se encontraron joyas con ese criterio.")
