import time
import beepy

def cuisson(temps_cuisson):
    duree = temps_cuisson
    while duree != 0:
        minutes = duree // 60
        secondes = duree - minutes * 60
        print(f"Temps restant : {minutes:02d}:{secondes:02d} ", end="")
        for i in range (0, 10):
            time.sleep(1)
            print(".", end="", flush=True)
        duree -= 10
    print()
    print("Cuisson terminée")
    beepy.beep(sound="ping")

def menu():
    print("Cuisson des oeufs")
    print("-----------------")
    print("a) Oeufs à la coque - 3 min")
    print("b) Oeufs mollets - 6 min")
    print("c) Oeufs durs - 9 min")
    print()

while True:
    menu()
    choix = input("Quel est votre choix ? ")
    if choix == "a" or choix == "b" or choix == "b":
         break
    print("Choix non valide, veuillez saisir a, b ou c.")
    print()

if choix == "a":
    cuisson(180)

if choix == "b":
    cuisson(360)

if choix == "c":
    cuisson(540)

