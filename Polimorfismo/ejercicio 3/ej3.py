class Empleado:
    def __init__(self, nombre, sueldo_mes, horas_extra=0, sueldo_hora=0, propina=0, cargo=""):
        self.nombre = nombre
        self.sueldo_mes = sueldo_mes
        self.horas_extra = horas_extra
        self.sueldo_hora = sueldo_hora
        self.propina = propina
        self.cargo = cargo

    def sueldo_total(self):
        return self.sueldo_mes + (self.horas_extra * self.sueldo_hora) + self.propina

    def mostrar(self):
        print(f"{self.cargo}: {self.nombre}, Sueldo Total: Bs{self.sueldo_total()}")

def mostrar_empleados(sueldo_mes, empleados):
    print(f"\nEmpleados con sueldo mensual de {sueldo_mes}:")
    for empleado in empleados:
        if empleado.sueldo_mes == sueldo_mes:
            print(f"- {empleado.nombre} ({empleado.cargo})")

cocinero = Empleado("Felipe", 2500, 10, 15, 0, "Cocinero")
mesero1 = Empleado("Marco", 1500, 5, 10, 200, "Mesero")
mesero2 = Empleado("Maria", 1500, 8, 10, 250, "Mesero")
admin1 = Empleado("Britney", 3400, 0, 0, 0, "Administrativo")
admin2 = Empleado("Alan", 3400, 5, 20, 0, "Administrativo")

empleados = [cocinero, mesero1, mesero2, admin1, admin2]

for empleado in empleados:
    empleado.mostrar()

mostrar_empleados(1500, empleados)