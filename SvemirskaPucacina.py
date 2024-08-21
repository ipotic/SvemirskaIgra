import random

# Početno stanje igrača
energija_stita = 100
rakete = 3
broj_neprijatelja_unistenih = 0

def laserski_napad():
    if random.random() <= 0.8:  # 80% šansa za pogodak
        steta = random.randint(10, 20)
        print(f"Laserski napad je uspešan! Naneli ste {steta} štete neprijatelju.")
        return steta
    else:
        print("Laserski napad je promašio!")
        return 0

def ispaliti_raketu():
    global rakete
    if rakete > 0:
        rakete -= 1
        if random.random() <= 0.9:  # 90% šansa za pogodak
            steta = random.randint(30, 40)
            print(f"Raketa je pogodila! Naneli ste {steta} štete neprijatelju.")
            return steta
        else:
            print("Raketa je promašila!")
            return 0
    else:
        print("Nemate više raketa!")
        return 0

def pokusaj_bekstva():
    if random.random() <= 0.5:  # 50% šansa za uspešno bekstvo
        print("Uspešno ste pobegli!")
        return True
    else:
        print("Bekstvo nije uspelo!")
        return False

# Glavna petlja igre
for sektor in range(1, 6):
    print(f"\nSektor: {sektor}/5")
    print(f"Energija štita: {energija_stita}")
    print(f"Rakete: {rakete}")

    # Generisanje događaja u sektoru
    if random.random() <= 0.8:  # 80% šansa za pojavu neprijateljskog broda
        neprijateljski_hp = 50
        print("Neprijateljski brod se pojavio!")
        print(f"HP neprijatelja: {neprijateljski_hp}")

        while neprijateljski_hp > 0:
            print("\nIzaberite akciju:")
            print("a) Laserski napad")
            print("b) Ispaliti raketu")
            print("c) Pokušaj bekstva")
            akcija = input("Vaš izbor: ").strip().lower()

            if akcija == 'a':
                steta = laserski_napad()
                neprijateljski_hp -= steta
            elif akcija == 'b':
                steta = ispaliti_raketu()
                neprijateljski_hp -= steta
            elif akcija == 'c':
                if pokusaj_bekstva():
                    break
            else:
                print("Nevažeća akcija. Pokušajte ponovo.")
                continue

            if neprijateljski_hp <= 0:
                print("Neprijateljski brod je uništen!")
                broj_neprijatelja_unistenih += 1
                break

            # Neprijateljski napad
            if random.random() <= 0.7:  # 70% šansa za pogodak neprijatelja
                steta = random.randint(10, 15)
                energija_stita -= steta
                print(f"Neprijatelj vas je pogodio! Izgubili ste {steta} energije štita.")
            else:
                print("Neprijatelj je promašio!")

            if energija_stita <= 0:
                print("Vaš brod je uništen! Igra je završena.")
                break

    else:
        print("Prošli ste kroz sektor bez incidenta.")

    if energija_stita <= 0:
        break

# Završetak igre
if energija_stita > 0:
    print(f"\nČestitamo! Preživeli ste putovanje kroz 5 sektora.")
    print(f"Uništili ste {broj_neprijatelja_unistenih} neprijatelja.")
else:
    print(f"Nažalost, vaš brod nije preživeo putovanje.")