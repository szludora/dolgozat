def beolvas(fajl):

    f = open(fajl, "r", encoding="utf-8")

    fejlec = f.readline().strip().split(";")
    # print(fejlec)

    sorok = f.readlines()

    i = 0

    stadion = []
    varos = []
    csapat = []
    elso = []
    utolso = []

    while i < len(sorok):
        sor = sorok[i].strip().split(";")
        stadion.append(sor[0])
        varos.append(sor[1])
        csapat.append(sor[2])
        elso.append(sor[3])
        utolso.append(sor[4])
        i += 1

    print(f"A csapatok db száma: {len(csapat)}")

    ny_csapatok = []

    i = 0
    while i < len(varos):
        if varos[i] == "New York":
            print(f"{stadion[i]}, - {csapat[i]}")
        i += 1

