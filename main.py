from usuario import UsuarioManager

gestor = UsuarioManager()

while True:
    opcion = input("Elige una opción (registro, login, base de datos, salir): ").lower()

    if opcion == "registro":
        gestor.registro()
    elif opcion == "login":
        gestor.login()
    elif opcion == "base de datos":
        gestor.mostrar_base_datos()
    elif opcion == "salir":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida.")
