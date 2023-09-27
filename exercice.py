#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    number_string = str(number)
    number_absolute = number_string[1:]
    absolute = float(number_absolute)
    return absolute

def use_prefixes():
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    nom = ""
    list_nom = []
    for i in prefixes:
        nom = i + suffixe
        list_nom.append(nom)
    return list_nom


def prime_integer_summation() -> int:
    prime = [2, 3, 5]
    number = 6
    while len(prime) < 100:
        is_prime = True
        for i in range(2, number // 2):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            prime.append(number)

        number += 1

    return sum(prime)
   

def factorial(number: int) -> int:
    n = 1
    for i in range (1, number + 1):
        n *= i
    return n


def use_continue() -> None:
    for i in range(10):
        if i == 5:
            continue
        print(i)


def verify_ages(groupe):
    list_groupe = []
    for list in groupe:
        if (len(list) > 10) or (len(list) < 3):
            continue
        else:
            for n in list:
                if 25 in list:
                    list_groupe.append(list)
                    break
                elif n < 18:
                    break
                elif (n > 70) and (50 in list):
                    break
                elif list[len(list) - 1] == n:
                    list_groupe.append(list)

    return list_groupe
                

def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groupe = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groupe}")
    print(f"L'acceptance des groupes est: {verify_ages(groupe)}")


if __name__ == '__main__':
    main()
