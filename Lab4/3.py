def diz(lista):
    if not lista:
        return None

    if len(lista) == 1:
        return lista[0]

    srodek = len(lista) // 2
    lewa_polowa = lista[:srodek]
    prawa_polowa = lista[srodek:]

    maks_lewa = diz(lewa_polowa)
    maks_prawa = diz(prawa_polowa)

    return max(maks_lewa, maks_prawa)


wektor = [321, 125, 3, 5, 70, 823, 7, 11, 13, 11, 5, 17]
print(diz(wektor))