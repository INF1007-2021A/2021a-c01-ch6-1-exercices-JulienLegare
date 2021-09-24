#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    liste = []
    counter = 1
    if values is None:
        # TODO: demander les valeurs ici
        while counter <= 10:
            valeur = input("Veuillez entrer une valeur")
            liste.append(valeur)
            counter += 1
    liste.sort()
    return liste


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        mot1 = input("entrer un mot")
        mot2 = input("entrer un autre mot")
        listMot1 = list(mot1)
        listMot2 = list(mot2)
        listMot1.sort()
        listMot2.sort()
        if listMot1 == listMot2:
            return True
        else:
            return False


def contains_doubles(items: list) -> bool:
    pass


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    moyBob = 0
    moyAlice = 0
    for number in student_grades["Bob"]:
        moyBob += number
    for note in student_grades["Alice"]:
        moyAlice += note
    moyBob /= 3
    moyAlice /= 3
    moyFinalAlice = {"Alice": moyAlice}
    moyFinalBob = {"Bob": moyBob}
    if moyAlice > moyBob:
        return moyFinalAlice
    else:
        return moyFinalBob


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    sentList = []
    over5list = []
    listeFinale = {}
    for lettre in sentence:
        sentList.append(lettre)
    for char in sentList:
        nbreChar = sentList.count(char)
        if char in over5list or char == " ":
            continue
        elif nbreChar >= 5:
            over5list.append(char)
            ajouteur = {char: nbreChar}
            listeFinale.update(ajouteur)
    listeFinaleSorted = sorted(listeFinale.items(), key=lambda item: item[1])
    return listeFinaleSorted


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    livre_de_recettes = {}
    x = input("Voulez vous ajouter une recette")

    if x == "yes":
        nom = input("Donnez le nom d'une recette")
        recette = input("Veuilles donner les ingredients separes d'un espace")
        recette.strip()
        recette = recette.split(" ")
        newRecipe = {nom: recette}
        livre_de_recettes.update(newRecipe)
        return get_recipes()
    else:
        print(livre_de_recettes)
        return livre_de_recettes


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    print(order())

    print(f"On vérifie les anagrammes...")
    print(anagrams())


    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    print(frequence(sentence))

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
