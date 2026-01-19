from PIL import Image
import os
from concurrent.futures import ThreadPoolExecutor

folder = os.path.dirname(os.path.realpath(__file__))

webp_files = [
    file_name for file_name in os.listdir(folder)
    if file_name.lower().endswith('.webp')
]

def convert_to_png(file_name, folder):
    file_path = os.path.join(folder, file_name)

    with Image.open(file_path) as img:
        png_path = os.path.splitext(file_path)[0] + '.png'
        img.save(png_path, 'PNG')
        print(f'{file_name} converted to {png_path}')

    os.remove(file_path)
    print(f'{file_name} has been deleted after conversion.')

def convert_images_in_parallel(webp_files, folder):
    with ThreadPoolExecutor() as executor:
        for file_name in webp_files:
            executor.submit(convert_to_png, file_name, folder)

        print("Conversion der Dateien gestartet...")

convert_images_in_parallel(webp_files, folder)
