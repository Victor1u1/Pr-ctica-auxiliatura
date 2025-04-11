class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def saludo(self):
        return f"Hola, soy {self.nombre} de {self.ciudad}"

    def es_mayor_de_edad(self):
        return self.edad >= 18  

persona1 = Persona("Luis", 20, "La Paz")
persona2 = Persona("Melani", 21, "La Paz")
persona3 = Persona("Yadira", 23, "Cochabamba")

print(persona1.saludo())
print(persona2.saludo())
print(persona3.saludo())

print(f"{persona1.nombre} es mayor de edad: {persona1.es_mayor_de_edad()}")
print(f"{persona2.nombre} es mayor de edad: {persona2.es_mayor_de_edad()}")
print(f"{persona3.nombre} es mayor de edad: {persona3.es_mayor_de_edad()}")