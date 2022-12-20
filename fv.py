import random


def beker(parameter="Kérek egy", par2="PÁROS számot kérek!"):
    paros = int(input(f"{parameter}páros számot! "))
    while paros % 2 != 0:
        paros = int(input(f"Ez nem páros! {par2}"))
    return paros


def parose(mennyi=1):
    lista = []
    i = 1
    while i <= mennyi:
        ujszam = beker(f"Kérem az {i}. ", f"Kérem az {i}. páros számot!")
        lista.append(ujszam)
        i += 1
    print(f"Az általad megadott számok a következők: {lista}.")
    return lista


def legkisebb(lista):
    i = 0
    hely = 0
    kicsi = lista[0]
    while i < len(lista):
        if lista[i] < kicsi:
            kicsi = lista[i]
            hely = i
        i += 1
    print(f"{hely+1}. lépésben adta meg a legkisebb páros számot, melynek értéke: {kicsi}")


def lista_keszites():
    
    veletlen_szamok = []
    
    while len(veletlen_szamok) < 13:
        vel = int(random.random()*191)-40
        veletlen_szamok.append(vel)
    print(f"A lista: {veletlen_szamok}")
    
    return veletlen_szamok
    

def ketjegyuek_szama(lista):
    
    i = 0
    ketjegyu_db = 0

    while i < len(lista):
        osztott = abs(lista[i] / 10)
        if osztott < 10 and osztott >= 1:
            ketjegyu_db += 1
        i += 1
    return ketjegyu_db


def paros_osszege(lista):
    osszeg = 0
    i = 0
    while i < len(lista):
        if lista[i] % 2 == 0:
            osszeg += lista[i]
        i += 1
    return osszeg


def paratlan_osszege(lista):
    osszeg = 0
    i = 0
    while i < len(lista):
        if lista[i] % 2 != 0:
            osszeg += lista[i]
        i += 1
    return osszeg


def nagyobb(lista):
    paros = paros_osszege(lista)
    paratlan = paratlan_osszege(lista)
    ketjegyu = ketjegyuek_szama(lista)

    if paros < paratlan:
        rel = " < "
    else:
        rel = " >"
    print(f"A párosok összege: {paros} {rel} a páratlanok összege: {paratlan}")
    print(f"A kétjegyűek száma: {ketjegyu}")