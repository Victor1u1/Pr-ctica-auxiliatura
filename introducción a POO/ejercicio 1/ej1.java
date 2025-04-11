public class Persona {
    private String nombre;
    private int edad;
    private String ciudad;
    
    public Persona(String nombre, int edad, String ciudad) {
        this.nombre = nombre;
        this.edad = edad;
        this.ciudad = ciudad;
    }
    
    public String saludo() {
        return "Hola, soy " + nombre + " de " + ciudad;
    }
    
    public boolean esMayorEdad() {
        return edad >= 18;
    }

    public String getNombre() {
        return nombre;
    }

    public static void main(String[] args) {
        Persona persona1 = new Persona("Luis", 20, "La Paz");
        Persona persona2 = new Persona("Melani", 21, "La Paz");
        Persona persona3 = new Persona("Yadira", 23, "Cochabamba");
        
        System.out.println(persona1.saludo());
        System.out.println(persona2.saludo());
        System.out.println(persona3.saludo());
        
        System.out.println(persona1.getNombre() + " es mayor de edad: " + persona1.esMayorEdad());
        System.out.println(persona2.getNombre() + " es mayor de edad: " + persona2.esMayorEdad());
        System.out.println(persona3.getNombre() + " es mayor de edad: " + persona3.esMayorEdad());
    }
}
