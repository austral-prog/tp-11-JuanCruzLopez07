def read_file_to_dict(filename):
    """Lee un archivo de ventas donde cada venta es producto:valor_de_venta;... y agrupa los valores por producto en una lista.

    :param filename: str - nombre del archivo a leer.
    :return: dict - diccionario con listas de montos por producto.
    :raises: FileNotFoundError - si el archivo no existe.
    """
    ventas_por_producto = {}

    with open(filename, 'r') as file:
        linea = file.readline().strip()
        ventas = linea.split(';')

        for venta in ventas:
            if venta:  # Evita procesar cadenas vacías por el último ;
                try:
                    producto, valor = venta.split(':')
                    valor = float(valor)
                    if producto in ventas_por_producto:
                        ventas_por_producto[producto].append(valor)
                    else:
                        ventas_por_producto[producto] = [valor]
                except ValueError:
                    print(f"Advertencia: formato inválido en venta '{venta}' (ignorada).")

    return ventas_por_producto


def process_dict(data):
    """Para cada producto, imprime el total de ventas y el promedio, en el orden natural del diccionario.

    :param data: dict - diccionario a procesar.
    :return: None
    """
    for producto, montos in data.items():
        total = sum(montos)
        promedio = total / len(montos) if montos else 0
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
