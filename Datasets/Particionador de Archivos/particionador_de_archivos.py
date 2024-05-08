def split_file(file_path, num_parts=5):
    import os

    # Leer el contenido del archivo
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # La primera línea contiene los nombres de las columnas
    header = lines[0]
    data_lines = lines[1:]

    # Calcular el número de líneas por archivo
    lines_per_part = len(data_lines) // num_parts

    # Obtener el nombre base del archivo original sin la extensión
    base_name = os.path.splitext(os.path.basename(file_path))[0]

    # Crear directorio para archivos divididos si no existe
    output_dir = os.path.join(os.path.dirname(file_path), f'particiones_{base_name}')
    os.makedirs(output_dir, exist_ok=True)

    # Escribir cada parte en un archivo separado
    for i in range(num_parts):
        part_file_path = os.path.join(output_dir, f'{base_name}_parte_{i + 1}.txt')
        start_index = i * lines_per_part
        # Asegurarse de incluir todas las líneas en la última parte
        end_index = (i + 1) * lines_per_part if i != num_parts - 1 else None

        with open(part_file_path, 'w', encoding='utf-8') as part_file:
            part_file.write(header)  # Escribir los nombres de las columnas
            part_file.writelines(data_lines[start_index:end_index])

    print(f'Archivo dividido en {num_parts} partes en la carpeta {output_dir}')


# Usar la función
split_file('/Users/tars/Desktop/UNIVERSITY/7mo Semestre/Procesamiento de Datos a Gran Escala/Parcial 2/Parcial2-Procesamiento-de-Datos-a-Gran-Escala/Datasets/Post-Pandemia/Año 2023/2023-2/SB11_20232.txt')
