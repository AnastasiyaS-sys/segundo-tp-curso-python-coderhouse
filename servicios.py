class Servicios:
    def __init__(self):
        self.lista_servicios = {
            "1": "Pre-producción",
            "2": "Grabación",
            "3": "Mezcla",
            "4": "Mastering",
            "5": "Sonido en vivo"
        }

    def mostrar_servicios(self):
        print("Servicios disponibles:")
        for clave, servicio in self.lista_servicios.items():
            print(f"{clave}. {servicio}")

    def contratar_servicio(self):
        self.mostrar_servicios()
        opcion = input("Selecciona el número del servicio que deseas contratar: ")

        servicio_elegido = self.lista_servicios.get(opcion)
        if servicio_elegido:
            descripcion = input(f"Describe brevemente lo que necesitas para '{servicio_elegido}': ")
            print("Solicitud de cotización enviada con éxito.")
        else:
            print("Opción inválida. Intenta nuevamente.")
