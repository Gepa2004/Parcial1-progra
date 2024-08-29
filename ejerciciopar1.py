#Un consultorio médico atiende a una serie de pacientes, solo está una 
#secretaria y en el consultorio hay varios doctores cada paciente llega y 
#deja sus datos además del motivo de su consulta y posteriormente la 
#secretaria les asigna la fecha de su consulta. 
#En el caso que una persona ya tenga una consulta previa en lugar 
#de tomar datos se le pasará a sala de esperas. Implementa esta 
#problemática a tu código.

from datetime import datetime

class Paciente:
    def __init__(self, nombre, motivo_consulta):
        self.nombre = nombre
        self.motivo_consulta = motivo_consulta
        self.cita_asignada = False

    def __repr__(self):
        return f"Paciente(nombre={self.nombre}, motivo_consulta={self.motivo_consulta}, cita_asignada={self.cita_asignada})"

class Consultorio:
    def __init__(self):
        self.pacientes = {}
        self.pacientes_en_espera = []
        self.fecha_consulta = 1

    def registrar_paciente(self, nombre, motivo_consulta):
        if nombre in self.pacientes:
            paciente = self.pacientes[nombre]
            if paciente.cita_asignada:
                self.pacientes_en_espera.append(paciente)
                return f"{nombre} ya tiene una consulta previa y ha sido enviado a sala de espera."
        else:
            paciente = Paciente(nombre, motivo_consulta)
            self.pacientes[nombre] = paciente
            paciente.cita_asignada = True
            self.asignar_cita(paciente)
            return f"Paciente {nombre} registrado y cita asignada para el día {self.fecha_consulta}."

    def asignar_cita(self, paciente):
        self.fecha_consulta += 1  # Aumenta la fecha de consulta para el siguiente paciente

    def mostrar_pacientes(self):
        return {"Pacientes registrados": list(self.pacientes.values()), "Pacientes en espera": self.pacientes_en_espera}

def main():
    consultorio = Consultorio()
    
    while True:
        print("\n--- Menú del Consultorio Médico ---")
        print("1. Registrar Paciente")
        print("2. Mostrar Pacientes")
        print("3. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            nombre = input("Ingresa el nombre del paciente: ")
            motivo_consulta = input("Ingresa el motivo de la consulta: ")
            resultado = consultorio.registrar_paciente(nombre, motivo_consulta)
            print(resultado)
        
        elif opcion == '2':
            pacientes = consultorio.mostrar_pacientes()
            print("Pacientes registrados:")
            for paciente in pacientes["Pacientes registrados"]:
                print(paciente)
            print("Pacientes en espera:")
            for paciente in pacientes["Pacientes en espera"]:
                print(paciente)
        
        elif opcion == '3':
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()


#Consultorio Médico: Gestiona pacientes y citas, asignando fechas de consulta y manejando pacientes con 
#citas previas mediante la sala de espera, evitando la duplicación de datos.