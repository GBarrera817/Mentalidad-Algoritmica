pass_usuario = input("Ingresa contrasena: ")
pass_temporal = ''

while pass_usuario != pass_temporal:
    pass_temporal = input("Ingresa nuevamente tu contrasenia: ")

    if pass_temporal == pass_usuario:
        print("Logeado")
    else:
        print("Te equivocaste. Vuelve a ingresar la contrasenia: ")
