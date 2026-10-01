

partis = ["(Moderator)"]
parti = input("Ingresar el apellido del participante (0 - detener ingreso)")
while parti != "0":
    if parti in partis:
        print("¡Este participante ya ha sido registrado!")
    else:
        partis.append(parti)
    parti = input("Ingresar el apellido del participante (0 - detener ingreso)")
    partis.sort()
    print("El grupo esta escrito", partis)