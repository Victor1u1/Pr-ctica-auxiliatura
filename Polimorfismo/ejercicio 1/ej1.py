class Videojuego:
    def __init__(self, nombre, plataforma, cantidad_jugadores):
        self.nombre, self.plataforma, self.cantidad_jugadores = nombre, plataforma, cantidad_jugadores
        
    def mostrar(self):
        print(f"{self.nombre} - {self.plataforma} - jugadores: {self.cantidad_jugadores}")
        
    def agregar_jugadores(self, cantidad=1):
        self.cantidad_jugadores += cantidad
        
juego1 = Videojuego("Minecraft", "PC", 5)
juego2 = Videojuego("Watchdogs", "XBOX ONE", 1)
    
juego1.mostrar()
juego2.mostrar()

juego1.agregar_jugadores(3)
juego1.mostrar()