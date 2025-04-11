public class Coche {
    private String marca;
    private String modelo;
    private int velocidad = 0;
    
    public Coche(String marca, String modelo) {
        this.marca = marca;
        this.modelo = modelo;
    }
    
    public void acelerar() {
        velocidad += 10;
    }
    
    public void frenar() {
        velocidad -= 5;
    }
    
    public String toString() {
        return marca + " " + modelo + " - Velocidad: " + velocidad;
    }
    
    public static void main(String[] args) {
        Coche coche1 = new Coche("Toyota", "Corolla");
        Coche coche2 = new Coche("Ferrari", "296GTB");
        
        coche1.acelerar();
        coche1.acelerar();
        coche1.frenar();
        
        coche2.acelerar();
        coche2.frenar();
        coche2.frenar();
        
        System.out.println(coche1);
        System.out.println(coche2);
    }
}