public class Videojuego {
    String nombre, plataforma;
    int cantidadJugadores;
    
    public Videojuego(String nombre, String plataforma, int cantidadJugadores) {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.cantidadJugadores = cantidadJugadores;
    }
    
    public void mostrar() {
        System.out.println(nombre + " - " + plataforma + " - Jugadores: " + cantidadJugadores);
    }
    
    public void agregarJugadores() {
        cantidadJugadores++;
    }
    
    public void agregarJugadores(int cantidad) {
        cantidadJugadores += cantidad;
    }
    
    public static void main(String[]args) {
        Videojuego juego1 = new Videojuego("Minecraft", "PC", 5);
        Videojuego juego2 = new Videojuego("Watchdogs", "XBOX ONE", 1);
        
        juego1.mostrar();
        juego2.mostrar();
        
        juego1.agregarJugadores(3);
        juego1.mostrar();
    }
}