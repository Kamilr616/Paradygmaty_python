from random import randint


def main():
    randNumber = randint(1, 10)
    step = 3
    int(step)
    int(randNumber)
    while(step):
        number = int(input("Zgadnij liczbę >>"))
        step -= 1
        if number == randNumber:
            print("Gratulacje, zgadłeś!")
            break
        else:
            print("Pozostało prób :", step)
            if randNumber > number:
                print("Podana liczba jest mniejsza")
            else:
                print("Podana liczba  jest większa")
    else:
        print("Koniec prób!")


main()
