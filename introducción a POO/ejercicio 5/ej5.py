class Estudiante:
    def __init__(self, nombre, nota_1, nota_2):
        self.nombre = nombre
        self.nota_1 = nota_1
        self.nota_2 = nota_2
        
    def promedio(self):
        return (self.nota_1 + self.nota_2) / 2
        
    def aprobo(self):
        return self.promedio() >=6
        
    def __str__(self):
        return f"{self.nombre} - Promedio: {self.promedio()} - Aprobo: {self.aprobo()}"
        
estudiante1 = Estudiante("Marcelo", 9, 10)
estudiante2 = Estudiante("Wilmer", 5, 10)
estudiante3 = Estudiante("Gabriel", 2, 3)

print(estudiante1)
print(estudiante2)
print(estudiante3)