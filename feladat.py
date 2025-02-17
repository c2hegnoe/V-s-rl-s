f = open('vasarlas.csv', 'r')

for szam in f:
    szam = szam.strip()
    tmp = szam.split(";")


def napok(tmp):
    napokSzama=0

    for nap in tmp:
        napokSzama += 1
    print("Ennyi nap volt a hónapba: ", napokSzama)


def nullakoltes(tmp):
    nullaKoltes=0
    for nap in tmp:
        if nap == "0":
            nullaKoltes += 1
    print("Ennyi napon nem történt költés: ", nullaKoltes)


def atlagkoltes(tmp):
    szum = 0
    for nap in tmp:
        nap = int(nap)
        szum += nap
    print("Napi átlagköltés: ", szum/len(tmp), "Ft")


def minesmax(tmp):
    maxszam = -100000
    minszam = 100000

    for nap in tmp:
        nap = int(nap)
        if nap > maxszam:
            maxszam = nap

        if nap < minszam and nap!=0:
            minszam = nap

    print("Legnagyobb vásárlás:", maxszam, "Ft.")
    print("Legkisebb vásárlás:", minszam, "Ft.")




f.close()
napok(tmp)
nullakoltes(tmp)
atlagkoltes(tmp)
minesmax(tmp)

