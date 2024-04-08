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
            
            if nodo.es_meta():
                camino = Costo_uniforme.reconstruir_camino(nodo)
                reporte = Costo_uniforme.generar_reporte(
                    nodos_expandidos, profundidad, tiempo_inicio, nodo)

                return camino, 'Encontré a grogu', reporte 
            
            # Expande el nodo y obtiene sus hijos
            hijos: "list[Nodo]" = nodo.expandir()

            # Actualiza cantidad de nodos expandidos
            nodos_expandidos += 1      
            
            cola_prioridad.get()            
            
            for hijo in hijos:

                # Actualiza profundidad
                if profundidad < hijo.get_profundidad():
                    profundidad = hijo.get_profundidad()

                if evitar_devolverse and Costo_uniforme.se_ha_devuelto(hijo):
                    print_debug("paso, queria ir a {} pero hace dos pasos estuve en {}".format(
                        str(hijo.get_estado()), str(nodo.get_padre().get_estado())))
                    continue

                if evitar_ciclo and Costo_uniforme.cayo_en_ciclo(hijo):
                    print_debug("paso, hace un tiempo estuve en {}, evitare entrar en ciclo".format(
                        str(hijo.get_estado())))
                    continue
                                
                cola_prioridad.put(hijo)  # Agrega los hijos a la cola                       
