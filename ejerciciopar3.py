#Un hotel de playa cuenta con un recepcionista que se encarga de 
#presentar a los clientes las opciones de habitaciones disponibles junto 
#con sus precios. Tras la elección de la habitación, el recepcionista 
#solicita los datos personales del cliente y el número de noches que 
#permanecerá en el hotel. Finalmente, entrega al cliente una factura 
#detallada con el total de los gastos. 
#Adicionalmente, los clientes pueden solicitar servicios extra, 
#como el uso de la piscina o la cancha de golf, que tienen un costo 
#adicional. Implementa esta funcionalidad en tu programa 

class Habitacion:
    def __init__(self, tipo, precio_por_noche):
        self.tipo = tipo
        self.precio_por_noche = precio_por_noche

    def __repr__(self):
        return f"Habitacion(tipo={self.tipo}, precio_por_noche={self.precio_por_noche})"

class Cliente:
    def __init__(self, nombre, noches, servicios_extra):
        self.nombre = nombre
        self.noches = noches
        self.servicios_extra = servicios_extra

    def calcular_total(self, habitacion):
        total_habitacion = habitacion.precio_por_noche * self.noches
        total_servicios_extra = sum(self.servicios_extra.values())
        return total_habitacion + total_servicios_extra

    def __repr__(self):
        return f"Cliente(nombre={self.nombre}, noches={self.noches}, servicios_extra={self.servicios_extra})"

class Recepcionista:
    def __init__(self):
        self.habitaciones = []
        self.servicios_extra = {
            'piscina': 20.0,
            'cancha de golf': 50.0
        }

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones(self):
        print("Opciones de habitaciones:")
        for idx, habitacion in enumerate(self.habitaciones, start=1):
            print(f"{idx}. {habitacion.tipo} - ${habitacion.precio_por_noche} por noche")

    def mostrar_servicios_extra(self):
        print("Servicios extra disponibles:")
        for servicio, costo in self.servicios_extra.items():
            print(f"{servicio} - ${costo}")

    def solicitar_datos_cliente(self):
        nombre = input("Ingresa el nombre del cliente: ")
        noches = int(input("Número de noches que permanecerá en el hotel: "))
        self.mostrar_servicios_extra()
        
        servicios_extra = {}
        for servicio in self.servicios_extra:
            incluir = input(f"¿Desea incluir el servicio de {servicio}? (s/n): ").strip().lower()
            if incluir == 's':
                servicios_extra[servicio] = self.servicios_extra[servicio]
        
        return Cliente(nombre, noches, servicios_extra)

    def generar_factura(self, cliente, habitacion):
        total = cliente.calcular_total(habitacion)
        print("\n--- Factura ---")
        print(f"Nombre del cliente: {cliente.nombre}")
        print(f"Habitación: {habitacion.tipo}")
        print(f"Número de noches: {cliente.noches}")
        print(f"Precio por noche: ${habitacion.precio_por_noche:.2f}")
        print("Servicios extra:")
        for servicio, costo in cliente.servicios_extra.items():
            print(f"{servicio}: ${costo:.2f}")
        print(f"Total a pagar: ${total:.2f}")

def main():
    recepcionista = Recepcionista()
    
    # Agregar habitaciones al hotel
    recepcionista.agregar_habitacion(Habitacion("Suite", 150.0))
    recepcionista.agregar_habitacion(Habitacion("Doble", 100.0))
    recepcionista.agregar_habitacion(Habitacion("Individual", 75.0))
    
    while True:
        print("\n--- Menú del Hotel ---")
        recepcionista.mostrar_habitaciones()
        
        opcion = input("Elija una opción de habitación (o 'salir' para terminar): ")
        
        if opcion.lower() == 'salir':
            print("Saliendo del sistema...")
            break
        
        try:
            opcion = int(opcion) - 1
            if 0 <= opcion < len(recepcionista.habitaciones):
                habitacion = recepcionista.habitaciones[opcion]
                cliente = recepcionista.solicitar_datos_cliente()
                recepcionista.generar_factura(cliente, habitacion)
            else:
                print("Opción de habitación no válida. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()

#Hotel de Playa: Presenta opciones de habitaciones, registra clientes y sus estancias, 
#calcula costos incluyendo servicios adicionales, y emite facturas detalladas.