# [estructura_datos.py]

class Accion:
    def __init__(self, nombre, dx, dy):
        self.nombre = nombre
        self.dx = dx  # Cambio en y
        self.dy = dy  # Cambio en x


class Celda:
    def __init__(self, tipo):
        self.tipo = tipo


class Estado:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Problema:
    def __init__(self, estado_inicial, estado_objetivo, cuadricula):
        self.estado_inicial = estado_inicial
        self.estado_objetivo = estado_objetivo
        self.cuadricula = cuadricula

    def es_valido(self, estado):
        enMatriz = 0 <= estado.x < 10 and 0 <= estado.y < 10
        enPared = self.cuadricula[estado.x][estado.y] != "pared"
        return enMatriz and enPared

    def es_objetivo(self, estado):
        return estado in self.estado_objetivo

    def acciones_validas(self, estado):
        acciones = []
        for dx, dy, accion_nombre in [(0, -1, 'arriba'), (0, 1, 'abajo'), (-1, 0, 'izquierda'), (1, 0, 'derecha')]:
            nuevo_estado = Estado(estado.x + dx, estado.y + dy)
            if self.es_valido(nuevo_estado):
                acciones.append(Accion(accion_nombre, dx, dy))
        return acciones

    def resultado(self, estado, accion):
        nuevo_estado = Estado(estado.x + accion.dx, estado.y + accion.dy)
        if self.es_valido(nuevo_estado):
            return nuevo_estado
        else:
            return None


if __name__ == '__main__':
    print("Hola mundo")
