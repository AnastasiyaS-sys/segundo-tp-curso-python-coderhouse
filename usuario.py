from cliente import Cliente

class UsuarioManager:
    def __init__(self):
        self.BD = {}

    def registro(self):
        usuario = input("Ingrese un nombre de usuario: ")
        contraseña = input("Ingrese una contraseña: ")
        if usuario in self.BD:
            print("El usuario ya está registrado.")
        else:
            self.BD[usuario] = Cliente(usuario, contraseña)
            print("Usuario registrado con éxito.")

    def login(self):
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")
        cliente = self.BD.get(usuario)

        if cliente and cliente.contraseña == contraseña:
            print(f"¡Bienvenido, {usuario}!")

            if not cliente.datos_completados:
                cliente.completar_datos()
            else:
                print("Datos ya registrados.")

            contratar = input("¿Deseás contratar un servicio? (si/no): ").lower()
            if contratar == "si":
                cliente.contratar_servicio()

            print("Volviendo al menú principal...")
        else:
            print("Usuario o contraseña incorrectos.")

    def mostrar_base_datos(self):
        print("Base de datos:")
        for cliente in self.BD.values():
            cliente.mostrar_datos()
