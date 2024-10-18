#Solution to question 2 goes here
def find_mushroom():
    answer1 = input("Does your mushroom have gills? (yes/no): ").strip().lower()

    if answer1 == "no":
        print("The mushroom is: Cepe de bordeaux")
        return
    answer2 = input("Does your mushroom grow in a forest? (yes/no): ").strip().lower()

    if answer2 == "no":
        answer3 = input("Does your mushroom have a ring? (yes/no): ").strip().lower()

        if answer3 == "yes":
            print("The mushroom is: Coprin chevelu")
        else:
            print("The mushroom is: Agaric jaunissant")
    
    else:
        answer3 = input("Does your mushroom have a ring? (yes/no): ").strip().lower()

        if answer3 == "yes":
            print("The mushroom is: Amanite tue-mouche")
        else:
            answer4 = input("Does your mushroom have a convex cup? (yes/no): ").strip().lower()

            if answer4 == "yes":
                print("The mushroom is: Pied Bleu")
            else:
                print("The mushroom is: Girolle")
find_mushroom()
