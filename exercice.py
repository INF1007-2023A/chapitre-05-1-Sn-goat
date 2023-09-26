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
    nombre = 0
    w = 0
    for i in range(100000):
        if i == 1:
            continue
        elif (i > 2) and ((i % 2 == 0) or ( i // 2 == 2 * i )):
            continue
        elif (i > 3) and ((i % 3 == 0) or ( i // 3 == 3 * i )):
            continue
        elif (i > 5) and ((i % 5 == 0) or ( i // 5 == 5 * i )):
            continue
        elif (i > 7) and ((i % 7 == 0) or ( i // 7 == 7 * i )):
            continue
        else:
            nombre = nombre + i
            w += 1
            if w == 100:
                return nombre


def factorial(number: int) -> int:
    return 0


def use_continue() -> None:
    pass


def verify_ages(groups: List[List[int]]) -> List[bool]:
    return []


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
