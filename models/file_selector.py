import os
import tkinter as tk
from tkinter import filedialog


class File_selector:
    ruta_proyecto = os.getcwd()
    ruta_completa = os.path.join(ruta_proyecto, "worlds")

    @staticmethod
    def select():
        # Crear una ventana de tkinter para el selector de archivos
        root = tk.Tk()
        root.withdraw()  # Ocultar la ventana principal de tkinter

        # Abrir el cuadro de diálogo para seleccionar un archivo
        archivo = filedialog.askopenfilename(
            initialdir=File_selector.ruta_completa)

        # Cerrar la ventana de tkinter
        root.destroy()

        # Devolver la ubicación absoluta del archivo seleccionado
        return archivo
