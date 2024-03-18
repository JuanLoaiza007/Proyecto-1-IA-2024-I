import os
import subprocess


# Hace automaticamente: pyuic5 vista.ui -o vista.py
# para todos los archivos en la misma carpeta
def ui_to_py():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    ui_files = [file for file in os.listdir(
        current_dir) if file.endswith('.ui')]

    for ui_file in ui_files:
        py_file = os.path.splitext(ui_file)[0] + '.py'
        ui_path = os.path.join(current_dir, ui_file)
        py_path = os.path.join(current_dir, py_file)
        command = ['pyuic5', '-x', ui_path, '-o', py_path]
        subprocess.run(command)


if __name__ == "__main__":
    ui_to_py()
