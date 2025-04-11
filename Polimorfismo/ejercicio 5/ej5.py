class Ambiente:
    def __init__(self, nombre, capacidad, nro_sillas=0, nro_escritorios=0, nro_estanterias=0, nro_pupitres=0, nro_mesas=0):
        self.nombre = nombre
        self.capacidad = capacidad
        self.nro_sillas = nro_sillas
        self.nro_escritorios = nro_escritorios
        self.nro_estanterias = nro_estanterias
        self.nro_pupitres = nro_pupitres
        self.nro_mesas = nro_mesas

    def mostrar(self):
        print(f"{self.nombre}: Capacidad {self.capacidad}, Muebles Totales: {self.cantidad_muebles()}")

    def cantidad_muebles(self):
        return self.nro_sillas + self.nro_escritorios + self.nro_estanterias + self.nro_pupitres + self.nro_mesas

oficina1 = Ambiente("Oficina 1", 5, nro_sillas=3, nro_escritorios=2, nro_estanterias=1)
oficina2 = Ambiente("Oficina 2", 4, nro_sillas=4, nro_escritorios=2, nro_estanterias=2)
aula1 = Ambiente("Aula C", 30, nro_pupitres=32, nro_sillas=32)
aula2 = Ambiente("Aula D", 25, nro_pupitres=28, nro_sillas=28)
laboratorio = Ambiente("Lab Computación", 20, nro_mesas=13, nro_sillas=20)

ambientes = [oficina1, oficina2, aula1, aula2, laboratorio]

for ambiente in ambientes:
    ambiente.mostrar()