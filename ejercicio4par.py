#Una empresa de renta de transporte tiene varios tipos de vehículos a su
#disposición cada uno con sus características y coste de renta. La
#empresa periódicamente registra los nuevos vehículos que ingresan al
#lote para su posterior puesta en renta.
# Implementa la funcionalidad de rentar los vehículos disponibles
#tomando en cuenta los datos del cliente.

class Vehiculo:
    def __init__(self, tipo, costo_renta, disponible=True):
        self.tipo = tipo
        self.costo_renta = costo_renta
        self.disponible = disponible

    def __str__(self):
        disponibilidad = "Disponible" if self.disponible else "No disponible"
        return f"Tipo: {self.tipo}, Costo: ${self.costo_renta}, Estado: {disponibilidad}"


class Cliente:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion

    def __str__(self):
        return f"Nombre: {self.nombre}, ID: {self.identificacion}"


class SistemaDeRenta:
    def __init__(self):
        self.vehiculos = []
        self.rentas = []

    def registrar_vehiculo(self):
        tipo = input("Ingrese el tipo de vehículo: ")
        costo_renta = float(input("Ingrese el costo de renta del vehículo: $"))
        vehiculo = Vehiculo(tipo, costo_renta)
        self.vehiculos.append(vehiculo)
        print("Vehículo registrado con éxito.")

    def rentar_vehiculo(self):
        cliente_nombre = input("Ingrese el nombre del cliente: ")
        cliente_id = input("Ingrese la ID del cliente: ")
        cliente = Cliente(cliente_nombre, cliente_id)
        
        tipo_vehiculo = input("Ingrese el tipo de vehículo que desea rentar: ")
        
        for vehiculo in self.vehiculos:
            if vehiculo.tipo == tipo_vehiculo and vehiculo.disponible:
                vehiculo.disponible = False
                self.rentas.append((cliente, vehiculo))
                print(f"Vehículo {vehiculo.tipo} rentado con éxito a {cliente.nombre}.")
                return
        print(f"No hay vehículos disponibles del tipo {tipo_vehiculo}.")

    def mostrar_vehiculos_disponibles(self):
        print("Vehículos disponibles:")
        for vehiculo in self.vehiculos:
            if vehiculo.disponible:
                print(vehiculo)

    def mostrar_rentas(self):
        print("Historial de rentas:")
        for cliente, vehiculo in self.rentas:
            print(f"{cliente} - {vehiculo}")


def menu():
    sistema = SistemaDeRenta()
    
    while True:
        print("\n--- Sistema de Renta de Vehículos ---")
        print("1. Registrar vehículo")
        print("2. Rentar vehículo")
        print("3. Mostrar vehículos disponibles")
        print("4. Mostrar historial de rentas")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            sistema.registrar_vehiculo()
        elif opcion == '2':
            sistema.rentar_vehiculo()
        elif opcion == '3':
            sistema.mostrar_vehiculos_disponibles()
        elif opcion == '4':
            sistema.mostrar_rentas()
        elif opcion == '5':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
    #empresa de renta: mi codigo registra vehiculos, tenemos que registrar vehiculos, otro usuarios puede rentar
    #los vehiculos registrados, podemos pedir que nos muetre los vehiculos discponibles y mostrar el historial
    # de rentas.
