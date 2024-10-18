#Solution to question 2 goes here
def identify_mushroom():
    has_gills = input("Does your mushroom have gills? (yes/no): ").strip().lower()
    if has_gills == "no":
        return "The mushroom is Cepe de bordeaux."
    grows_in_forest = input("Does your mushroom grow in a forest? (yes/no): ").strip().lower()
    if grows_in_forest == "no":
        has_ring = input("Does your mushroom have a ring? (yes/no): ").strip().lower()
        if has_ring == "yes":
            return "The mushroom is Coprin chevelu."
        else:
            return "The mushroom is Agaric jaunissant."
    has_convex_cup = input("Does your mushroom have a convex cup? (yes/no): ").strip().lower()

    if has_convex_cup == "yes":
        has_ring = input("Does your mushroom have a ring? (yes/no): ").strip().lower()
        if has_ring == "yes":
            return "The mushroom is Amanite tue-mouche."
        else:
            return "The mushroom is Pied Bleu."
    else:
        return "The mushroom is Girolle."
print(identify_mushroom())
