from agente import agente


class agente_reflejo_simple(agente):
    def __init__(self):
        super().__init__()

        self.tabla_percepcion_accion = [
            #  Esta libre
            # left    up    right  down     action
            ((True, True, True, True, False), 'arriba'),
            ((True, True, True, False, False), 'arriba'),
            ((True, True, False, True, False), 'arriba'),
            ((True, True, False, False, False), 'arriba'),
            ((True, False, True, True, False), 'izquierda'),
            ((True, False, True, False, False), 'derecha'),
            ((True, False, False, True, False), 'izquierda'),
            ((True, False, False, False, False), 'izquierda'),
            ((False, True, True, True, False), 'arriba'),
            ((False, True, True, False, False), 'derecha'),
            ((False, True, False, True, False), 'abajo'),
            ((False, True, False, False, False), 'arriba'),
            ((False, False, True, True, False), 'derecha'),
            ((False, False, True, False, False), 'derecha'),
            ((False, False, False, True, False), 'abajo'),
            ((False, False, False, False, False), 'esperar')
        ]

    def determinar_accion(self, percepcion_actual):
        if percepcion_actual[-1]:
            return 'alegrarse'
        for percepcion, accion in self.tabla_percepcion_accion:
            if percepcion_actual == percepcion:
                return accion
        return 'esperar'

    def tomar_decision(self):
        percepciones = (
            self.libre_izquierda(),
            self.libre_arriba(),
            self.libre_derecha(),
            self.libre_abajo(),
            self.meta_alcanzada()
        )

        accion = self.determinar_accion(percepciones)

        if accion == 'alegrarse':
            print("Lo logré :D")
            return False
        if accion == 'esperar':
            print("Ayuda :(")
            return False
        else:
            self.set_coordenadas(getattr(self, accion)())
            return True
