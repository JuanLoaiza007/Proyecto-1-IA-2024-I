# [Costo_uniforme.py]

from models.shared.Estructuras_datos import *
import time
from queue import PriorityQueue

class Costo_uniforme:
    def busqueda_por_costo_uniforme(problema: Problema):
        nodos_expandidos = 0
        profundidad = 0
        reporte = "Generando..."   
        
        tiempo_inicio = time.time()
        cola_prioridad = PriorityQueue()
        cola_prioridad.put(Nodo.get_costo_acumulado, Nodo(problema))
        
        while not cola_prioridad.empty():
            nodo: Nodo = cola_prioridad.get()  # Saca un nodo de la cola        
