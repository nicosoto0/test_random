class car:
    def __init__(self, ruedas, km):
        self.ruedas = ruedas
        self.km = km
        self.last_oil = 1000

    def avanzar(self, km):
        self.km += km

    def need_change(self):
        if (self.last_oil+10000 < self.km):
            return True
        return False


a1 = car(4, 1000)

if a1.need_change():
    print("cambiar aceite")
else:
    print("Seguir andando")
