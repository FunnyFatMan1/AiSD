def suma_diz(lista):
    if not lista:
        return 0

    if len(lista) == 1:
        return lista[0]

    srodek = len(lista) // 2
    lewa_polowa = lista[:srodek]
    prawa_polowa = lista[srodek:]

    suma_lewa = suma_diz(lewa_polowa)
    suma_prawa = suma_diz(prawa_polowa)

    return suma_lewa + suma_prawa


lista = [321, 125, 3, 5, 70, 823, 7, 11, 13, 11, 5, 17]
print(suma_diz(lista))
