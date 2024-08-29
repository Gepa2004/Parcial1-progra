#Una biblioteca ofrece préstamos de libros a través de una tarjeta 
#impresa que contiene los datos de la persona que realiza el préstamo. El 
#sistema de préstamos registra la fecha en que se retira el libro y la fecha 
#límite para su devolución. Realiza un programa que solvente esto de 
#una manera más eficaz. 
# Implementar la sección de devolución la cual si la fecha excede la 
#que devolución se dará una sanción. 



from datetime import datetime, timedelta

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def __repr__(self):
        return f"Libro(titulo={self.titulo}, autor={self.autor}, disponible={self.disponible})"

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return f"Persona(nombre={self.nombre})"

class Prestamo:
    def __init__(self, libro, persona, fecha_prestamo, fecha_devolucion):
        self.libro = libro
        self.persona = persona
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.devuelto = False

    def devolver_libro(self, fecha_devolucion_actual):
        self.devuelto = True
        if fecha_devolucion_actual > self.fecha_devolucion:
            dias_retraso = (fecha_devolucion_actual - self.fecha_devolucion).days
            sancion = dias_retraso * 1.0  # Ejemplo: $1 por día de retraso
            return f"Libro devuelto con retraso. Sanción: ${sancion:.2f}"
        return "Libro devuelto a tiempo."

    def __repr__(self):
        return (f"Prestamo(libro={self.libro}, persona={self.persona}, "
                f"fecha_prestamo={self.fecha_prestamo}, fecha_devolucion={self.fecha_devolucion}, "
                f"devuelto={self.devuelto})")

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.prestamos = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def prestar_libro(self, libro, persona):
        if libro.disponible:
            fecha_prestamo = datetime.now()
            fecha_devolucion = fecha_prestamo + timedelta(days=14) 
            prestamo = Prestamo(libro, persona, fecha_prestamo, fecha_devolucion)
            libro.disponible = False
            self.prestamos.append(prestamo)
            return f"Libro '{libro.titulo}' prestado a {persona.nombre}. Fecha de devolución: {fecha_devolucion.date()}"
        return f"El libro '{libro.titulo}' no está disponible."

    def devolver_libro(self, libro, persona, fecha_devolucion_actual):
        for prestamo in self.prestamos:
            if prestamo.libro == libro and prestamo.persona == persona and not prestamo.devuelto:
                libro.disponible = True
                return prestamo.devolver_libro(fecha_devolucion_actual)
        return "No se encontró el préstamo."

    def __repr__(self):
        return (f"Biblioteca(libros={self.libros}, prestamos={self.prestamos})")

def main():
    biblioteca = Biblioteca()
    
    while True:
        print("\n--- Menú de Biblioteca ---")
        print("1. Agregar Libro")
        print("2. Prestar Libro")
        print("3. Devolver Libro")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            titulo = input("Ingresa el título del libro: ")
            autor = input("Ingresa el autor del libro: ")
            libro = Libro(titulo, autor)
            biblioteca.agregar_libro(libro)
            print(f"Libro '{titulo}' agregado a la biblioteca.")
        
        elif opcion == '2':
            nombre_persona = input("Ingresa el nombre de la persona: ")
            persona = Persona(nombre_persona)
            titulo_libro = input("Ingresa el título del libro a prestar: ")
            
            libro = next((libro for libro in biblioteca.libros if libro.titulo == titulo_libro), None)
            if libro:
                resultado = biblioteca.prestar_libro(libro, persona)
                print(resultado)
            else:
                print("El libro no está en la biblioteca.")
        
        elif opcion == '3':
            nombre_persona = input("Ingresa el nombre de la persona: ")
            persona = Persona(nombre_persona)
            titulo_libro = input("Ingresa el título del libro a devolver: ")
            fecha_devolucion_str = input("Ingresa la fecha de devolución (YYYY-MM-DD): ")
            fecha_devolucion_actual = datetime.strptime(fecha_devolucion_str, "%Y-%m-%d")
            
            libro = next((libro for libro in biblioteca.libros if libro.titulo == titulo_libro), None)
            if libro:
                resultado = biblioteca.devolver_libro(libro, persona, fecha_devolucion_actual)
                print(resultado)
            else:
                print("El libro no está en la biblioteca.")
        
        elif opcion == '4':
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()

#Sistema de Préstamos de Biblioteca: Administra el préstamo y devolución de libros, 
#calcula sanciones por retrasos, y genera facturas detalladas para los clientes.