import subprocess
import os

def get_current_dir():
    current_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Source\\')
    return current_dir

def get_images():
    images = os.listdir(get_current_dir())
    return images

def resize_images():
    if os.path.exists('Result') == False:
        os.makedirs('Result')
    convert_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'convert.exe')
    for image in get_images():
        args = [convert_path, os.path.join(get_current_dir(), image), '-resize', '200',
                os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Result',
                             image.replace('.jpg', '_resized.jpg'))
                ]
        subprocess.call(args)

resize_images()