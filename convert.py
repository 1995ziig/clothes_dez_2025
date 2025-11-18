from PIL import Image
import os
from concurrent.futures import ThreadPoolExecutor

folder = os.path.dirname(os.path.realpath(__file__))

png_files = [file_name for file_name in os.listdir(folder) if file_name.endswith('.png')]

def convert_to_webp(file_name, folder):
    file_path = os.path.join(folder, file_name)
    
    with Image.open(file_path) as img:
        webp_path = os.path.splitext(file_path)[0] + '.webp'
        img.save(webp_path, 'WEBP', quality=75)
        print(f'{file_name} converted to {webp_path}')
    
    os.remove(file_path)
    print(f'{file_name} has been deleted after conversion.')

def convert_images_in_parallel(png_files, folder):
    with ThreadPoolExecutor() as executor:
        for index, file_name in enumerate(png_files, start=1):
            executor.submit(convert_to_webp, file_name, folder)
            
        print("Conversion des fichiers lancée...")


convert_images_in_parallel(png_files, folder)
