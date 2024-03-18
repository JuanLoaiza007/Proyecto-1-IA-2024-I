from models.agente import agente


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
            if self.debug:
                print("agente_reflejo_simply.py: Estoy en la meta, no me movere")
            return False
        if accion == 'esperar':
            if self.debug:
                print("agente_reflejo_simply.py: No encuentro que hacer, no me movere")
            return False
        else:
            if self.debug:
                print("agente_reflejo_simply.py: Me moveré a ", accion)
            self.set_coordenadas(getattr(self, accion)())

            return True

    def iniciar_viaje(self):

        en_viaje = True
        resultado = "Estoy perdido"

        while (en_viaje):
            en_viaje = self.tomar_decision()

            for elemento in self.pasos[:-1]:
                if elemento == self.coordenadas:
                    if self.debug:
                        print("agente_reflejo_simply.py: Pensé ir a ",
                              self.coordenadas, " pero  ya estuve en ", elemento)
                    resultado = "Ya paśe por aqui, algo anda mal :("
                    en_viaje = False

        if self.meta_alcanzada():
            resultado = "Encontré a grogu"

        return self.pasos, resultado
