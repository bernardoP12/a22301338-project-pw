import zipfile
import os

def unzip_images(zip_path, output_folder):
    # Verifica se a pasta de saída existe, se não, cria
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Extensões de arquivos de imagem comumente utilizadas, incluindo .svg
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.tif', '.webp', '.svg')

    # Abre o arquivo ZIP
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Itera sobre os arquivos no ZIP
        for file_info in zip_ref.infolist():
            # Verifica se o arquivo é uma imagem
            if file_info.filename.lower().endswith(image_extensions):
                # Extrai o arquivo para a pasta de saída
                zip_ref.extract(file_info, output_folder)
