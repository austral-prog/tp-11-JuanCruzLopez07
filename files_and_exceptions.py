def read_file_to_dict(str):
    """Lee un archivo de ventas donde cada venta es producto:valor_de_venta;... y agrupa los valores por producto en una lista.

    :param filename: str - nombre del archivo a leer.
    :return: dict - diccionario con listas de montos por producto.
    :raises: FileNotFoundError - si el archivo no existe.
    """
    ventas_por_producto = {}

    try:
        with open(str, 'r') as file:
            linea = file.readline().strip()
            ventas = linea.split(';')

            for venta in ventas:
                if venta:  # Evita procesar cadenas vacías por el último ;
                    try:
                        producto, valor = venta.split(':')
                        valor = float(valor)
                        if producto in dict:
                            dict[producto].append(valor)
                        else:
                            dict[producto] = [valor]
                    except ValueError:
                        print(f"Advertencia: formato inválido en venta '{venta}' (ignorada).")

        return dict

    except FileNotFoundError:
        print(f"Error: El archivo '{str}' no existe.")
        return {}

def process_dict(dict):
    """Para cada producto, imprime el total de ventas y el promedio, en el orden natural del diccionario.

    :param data: dict - diccionario a procesar.
    :return: None
    """
    for producto, montos in dict.items():
        total = sum(montos)
        promedio = total / len(montos) if montos else 0
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
