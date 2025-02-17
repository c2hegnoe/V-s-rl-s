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
        if nap == 0:
            nullaKoltes += 1
    print("Ennyi napon nem történt költés: ", nullaKoltes)

f.close()
napok(tmp)
nullakoltes(tmp)