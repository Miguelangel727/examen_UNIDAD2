
class Candidato:
    """Representa a un candidato en una elección."""
    def __init__(self, nombre, partido):
        self.nombre = nombre
        self.partido = partido
        self.votos = 0


class Eleccion:
    """Gestiona el proceso de una elección, incluyendo candidatos y votos."""
    def __init__(self, nombre_eleccion):
        self.nombre_eleccion = nombre_eleccion
        self.candidatos = []

    def agregar_candidato(self, candidato):
        """Agrega un candidato a la lista, validando que no haya nombres repetidos."""
        for c in self.candidatos:
            if c.nombre.lower() == candidato.nombre.lower():
                print(f" Error: Ya existe un candidato con el nombre '{candidato.nombre}'.")
                return
        self.candidatos.append(candidato)
        print(f" Candidato '{candidato.nombre}' del partido '{candidato.partido}' agregado.")

    def votar(self, nombre_candidato):
        """Incrementa los votos de un candidato si existe."""
        for candidato in self.candidatos:
            if candidato.nombre.lower() == nombre_candidato.lower():
                candidato.votos += 1
                print(f"  Voto registrado para '{candidato.nombre}'. ¡Gracias por participar!")
                return
        print(f" Error: El candidato '{nombre_candidato}' no existe.")

    def mostrar_resultados(self):
        """Muestra los resultados actuales de la elección."""
        if not self.candidatos:
            print(" Aún no hay candidatos registrados.")
            return

        print(f"\n--- Resultados de la Elección: {self.nombre_eleccion} ---")
        for candidato in sorted(self.candidatos, key=lambda c: c.votos, reverse=True):
            print(f" {candidato.nombre} ({candidato.partido}): {candidato.votos} votos")

    def ganador(self):
        """Devuelve el candidato con más votos, manejando empates."""
        if not self.candidatos:
            return None

        
        ganador = max(self.candidatos, key=lambda c: c.votos)
        
        
        empate = [c for c in self.candidatos if c.votos == ganador.votos]
        if len(empate) > 1:
            print(" ¡Hay un empate entre los siguientes candidatos! 🚨")
            for c in empate:
                print(f"  - {c.nombre} ({c.partido}) con {c.votos} votos.")
            return None

        return ganador


def main():
    """Ejecuta el menú interactivo para gestionar la elección."""
    eleccion_estudiantil = Eleccion("Elecciones para Presidente Estudiantil")
    
    while True:
        print("\n--- Menú de Elecciones ---")
        print("1.   Agregar un nuevo candidato")
        print("2.   Votar por un candidato")
        print("3.  Mostrar resultados actuales")
        print("4.  Consultar al ganador")
        print("5.  Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == '1':
            nombre = input("Ingresa el nombre del candidato: ")
            partido = input("Ingresa el nombre del partido: ")
            nuevo_candidato = Candidato(nombre, partido)
            eleccion_estudiantil.agregar_candidato(nuevo_candidato)
            
        elif opcion == '2':
            if not eleccion_estudiantil.candidatos:
                print(" Aún no hay candidatos para votar. Agrega uno primero.")
                continue
            nombre_voto = input("Ingresa el nombre del candidato por el que quieres votar: ")
            eleccion_estudiantil.votar(nombre_voto)
            
        elif opcion == '3':
            eleccion_estudiantil.mostrar_resultados()
            
        elif opcion == '4':
            ganador_actual = eleccion_estudiantil.ganador()
            if ganador_actual:
                print(f"\n El ganador actual es: {ganador_actual.nombre} ({ganador_actual.partido}) con {ganador_actual.votos} votos.")
            elif eleccion_estudiantil.candidatos:
                pass
            else:
                print(" Aún no hay candidatos ni votos.")

        elif opcion == '5':
            print(" Saliendo del sistema de votación. ¡Hasta la próxima!")
            break
            
        else:
            print(" Opción no válida. Por favor, elige un número del 1 al 5.")


if __name__ == "__main__":
    main()