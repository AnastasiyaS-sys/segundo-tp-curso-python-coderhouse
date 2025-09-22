from servicios import Servicios

class Cliente:
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña
        self.nombre = ""
        self.apellido = ""
        self.email = ""
        self.domicilio = ""
        self.telefono = ""
        self.datos_completados = False

    def __str__(self):
        nombre_completo = f"{self.nombre} {self.apellido}" if self.nombre and self.apellido else "Datos incompletos"
        return f"Cliente: {nombre_completo} | Usuario: {self.usuario}"

    def completar_datos(self):
        if self.datos_completados:
            print("Los datos ya fueron completados.")
            return

        print("Completa tus datos personales:")
        self.nombre = input("Nombre: ")
        self.apellido = input("Apellido: ")
        self.email = input("Email: ")
        self.domicilio = input("Domicilio: ")
        self.telefono = input("Teléfono: ")
        self.datos_completados = True
        print("Datos completados con éxito.")

    def mostrar_datos(self):
        print(f"""
Usuario: {self.usuario}
Nombre: {self.nombre}
Apellido: {self.apellido}
Email: {self.email}
Domicilio: {self.domicilio}
Teléfono: {self.telefono}
""")

    def contratar_servicio(self):
        servicio = Servicios()
        servicio.contratar_servicio()
