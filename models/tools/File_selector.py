import os
import tkinter as tk
from tkinter import filedialog


class File_selector:
    @staticmethod
    def select(initial_folder=None):
        if initial_folder is None:
            # Si no se proporciona una carpeta inicial, se usará el directorio actual
            initial_folder = os.getcwd()
        else:
            initial_folder = os.path.abspath(initial_folder)

        # Crear una ventana de tkinter para el selector de archivos
        root = tk.Tk()
        root.withdraw()  # Ocultar la ventana principal de tkinter

        # Abrir el cuadro de diálogo para seleccionar un archivo
        archivo = filedialog.askopenfilename(initialdir=initial_folder)

        # Cerrar la ventana de tkinter
        root.destroy()

        # Devolver la ubicación absoluta del archivo seleccionado
        return archivo
