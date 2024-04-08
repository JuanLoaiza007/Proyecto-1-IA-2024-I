# [Costo_uniforme.py]

# from models.shared.Estructuras_datos import *
import time
from queue import PriorityQueue

class Costo_uniforme:
    def busqueda_por_costo_uniforme():
        nodos_expandidos = 0
        profundidad = 0
        reporte = "Generando..."   
        
        tiempo_inicio = time.time()
        # insert into queue 
        
        q = PriorityQueue()         
        
        q.put((2, 'g')) 
        q.put((3, 'e')) 
        q.put((4, 'k')) 
        q.put((5, 's')) 
        q.put((1, 'e')) 
        q.put((1, 't'))        
        
        # remove and return  
        # lowest priority item 
        
        # check queue size 
        print('Items in queue :', q.qsize()) 
        
        # check if queue is empty 
        print('Is queue empty :', q.empty()) 
        
        # check if queue is full 
        print('Is queue full :', q.full()) 
        
        while q.empty() == False:
            print(q.get())                                 
        
        print("Cola vacia")
        
        return None
    
Costo_uniforme.busqueda_por_costo_uniforme()    
