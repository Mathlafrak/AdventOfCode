

def main():
    annexe = open("day01.in", "r")
    list_annexe = [int(i) for i in annexe.read().strip().split("\n")]
    compteur =0

    N = len(list_annexe)
    for i in range(1, N):
        if list_annexe[i] > list_annexe[i - 1]:
            compteur += 1
    print(compteur)

    compteur_fenetre = 0
    print(len(list_annexe))
    j = 0
    while j <= 1996:
        print("Iteration numero", j)
        fenetre1: int = list_annexe[j] + list_annexe[j+1] + list_annexe[j+2]
        fenetreSuivante: int = list_annexe[j+1] + list_annexe[j+2] + list_annexe[j+3]
        print(list_annexe[j], " + ", list_annexe[j+1], " + ", list_annexe[j+2], " = ", fenetre1)
        print(list_annexe[j+1], " + ", list_annexe[j+2], " + ", list_annexe[j+3], " = ", fenetreSuivante)
        if fenetreSuivante > fenetre1:
            compteur_fenetre += 1
            print("Sup")

        else:
            print("Eg ou Inf")

        j += 1


    print(compteur_fenetre)

    annexe.close()

if __name__ == "__main__":
    main()
