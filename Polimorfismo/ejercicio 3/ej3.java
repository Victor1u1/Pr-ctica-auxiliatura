class Empleado {
    String nombre;
    int sueldoMes;
    int horasExtra;
    float sueldoHora;
    float propina;
    String cargo;

    public Empleado(String nombre, int sueldoMes, int horasExtra, float sueldoHora, float propina, String cargo) {
        this.nombre = nombre;
        this.sueldoMes = sueldoMes;
        this.horasExtra = horasExtra;
        this.sueldoHora = sueldoHora;
        this.propina = propina;
        this.cargo = cargo;
    }

    public float sueldoTotal() {
        return sueldoMes + (horasExtra * sueldoHora) + propina;
    }

    public void mostrar() {
        System.out.println(cargo + ": " + nombre + ", Sueldo Total: Bs" + sueldoTotal());
    }

    public static void mostrarEmpleados(int sueldoMes, Empleado[] empleados) {
        System.out.println("\nEmpleados con sueldo mensual de " + sueldoMes + ":");
        for (Empleado empleado : empleados) {
            if (empleado.sueldoMes == sueldoMes) {
                System.out.println("- " + empleado.nombre + " (" + empleado.cargo + ")");
            }
        }
    }
}

public class Restaurante {
    public static void main(String[] args) {

        Empleado cocinero = new Empleado("Felipe", 2500, 10, 15, 0, "Cocinero");
        Empleado mesero1 = new Empleado("Marco", 1500, 5, 10, 200, "Mesero");
        Empleado mesero2 = new Empleado("Maria", 1500, 8, 10, 250, "Mesero");
        Empleado admin1 = new Empleado("Britney", 3400, 0, 0, 0, "Administrativo");
        Empleado admin2 = new Empleado("Alan", 3400, 5, 20, 0, "Administrativo");

        Empleado[] empleados = {cocinero, mesero1, mesero2, admin1, admin2};

        for (Empleado empleado : empleados) {
            empleado.mostrar();
        }

        Empleado.mostrarEmpleados(1500, empleados);
    }
}

