import random

zufallszahl = random.randint(1, 100)

def zahlenraten():
    zufallszahl = random.randint(1, 100)
    zuege = 3
    while zuege != 0:
        user_eingabe = int(input("Bitte geben sie eine Zahl ein \n"))
        if user_eingabe == zufallszahl:
            print ("Glückwunsch: Sie haben gewonnen")
            break

        elif user_eingabe > zufallszahl:
            print("Die gesuchte Zahl ist kleiner")
        else:
            print("Die gesuchte Zahl ist größer")
        
        zuege -= 1
        print("Sie haben noch " ,zuege, "Züge")   

    print("Sorry, Sie haben leider Verloren. Die gesuchte Zahl wäre ", zufallszahl, "gewesen")

    weiter = input("Möchten sie nochmal spielen? [j, n] ")

    if weiter =="j":
        zahlenraten()
    print("Auf wiedersehen")

zahlenraten()
