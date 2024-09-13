# Definimos una lista para los tickets disponibles
tickets_disponibles = [
    {"id": 1, "nombre": "Show de Magia", "precio": 50},
    {"id": 2, "nombre": "Concierto de Rock", "precio": 80},
    {"id": 3, "nombre": "Obra de Teatro", "precio": 60}
]

# Función para mostrar los tickets disponibles
def mostrar_tickets():
    print("Tickets Disponibles:")
    for ticket in tickets_disponibles:
        print(f"ID: {ticket['id']}, Nombre: {ticket['nombre']}, Precio: ${ticket['precio']}")

# Función para comprar un ticket
def comprar_ticket():
    mostrar_tickets()
    try:
        id_ticket = int(input("Introduce el ID del ticket que deseas comprar: "))
        ticket_encontrado = next((t for t in tickets_disponibles if t["id"] == id_ticket), None)
        
        if ticket_encontrado:
            print(f"Has comprado un ticket para: {ticket_encontrado['nombre']} a ${ticket_encontrado['precio']}")
        else:
            print("ID de ticket no válido.")
    except ValueError:
        print("Por favor, introduce un número válido.")

# Función principal para ejecutar el programa
def main():
    while True:
        print("\nMenu:")
        print("1. Mostrar Tickets Disponibles")
        print("2. Comprar Ticket")
        print("3. Salir")
        
        opcion = input("Selecciona una opción (1/2/3): ")
        
        if opcion == "1":
            mostrar_tickets()
        elif opcion == "2":
            comprar_ticket()
        elif opcion == "3":
            print("Gracias por usar el sistema de venta de tickets. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del menú.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
