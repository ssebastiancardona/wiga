
def ValidarEAN():
    codigoEAN = input("Digite su codigo EAN: " )
    sumaTotal = 0
    codigo = str(codigoEAN)
    control = 0
    paises = [
        ["0", "EEUU"],
        ["380", "Bulgaria"],
        ["50", "Inglaterra"],
        ["539", "Irlanda"],
        ["560", "Portugal"],
        ["70", "Noruega"],
        ["759", "Venezuela"],
        ["850", "Cuba"],
        ["890", "India"],
    ]

    if(codigo == "0"):
        ValidarEAN()
        return

    if(len(codigo) <= 8):
        codigo = ("00000000" + codigo)[-8:]
    if(len(codigo) > 8 and len(codigo) <= 13):
        codigo = ("00000" + codigo)[-13:]

    pais = "Desconocido"

    for i in paises:
        if(codigo.startswith(i[0])):
            pais = i[1]

    for i in reversed(codigo):
        f = int(i)
        if (control == 0):
            dv = int(i)

        if(control != 0):
            if(control % 2 != 0):
                sumaTotal += 3 * f

            if(control % 2 != 1):
                sumaTotal += 1 * f

        control = control +1
    dv = dv + sumaTotal

    if(len(codigo) == 8):
        pais = ""
    if(dv % 10 == 0):
        print(f"SI {pais}")
    else:
        print(f"NO {pais}")
    
    ValidarEAN()

ValidarEAN()