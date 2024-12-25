# Vu qu'il est possible de mettre n'importe quoi dans une collection... il est possible de mettre une liste DANS une liste
# on appelle cela un tableau a 2 dimensions. Ils permettent de créer des grilles de données. Comme une grille de bataille navale.
# ici les case "eau" sont marqués par un ".", tandis que les cases "navire" sont marquées par un "#"
# pour plus de lisibilité, les liste dans la liste sont écrites sur plusieurs lignes
"""
grid = [
        ['.','.','.'],
        ['#','.','.'],
        ['.','.','.']
    ]   
"""
# générez une grille de 3*3 avec au moins 1 navire et l'afficher.
# Bonus : arriverez vous a permettre à un.e utilisateur.ice de saisir une coordonnée (1,1 par exemple) et de dire si le tir touche un navire ?
# Bonus2 : et maintenant, de permettre de faire plusieurs tirs jusqu'a ce que le navire soit coulé ?

from random import randint

# génération de la grille
grid = [ ['.','.','.'], ['.','.','.'], ['.','.','.'] ]
ship_row = randint(0, 2)
ship_col = randint(0, 2)
grid[ship_row][ship_col] = '#'

# affichage de la grille
def print_grid():
    for row in grid:
        print(" ".join(row))

print("Grille de bataille navale !")
print_grid()

# jeu
hits = 0
while hits < 1:
    guess_row = int(input("Entrez un numéro de ligne (0, 1 ou 2) : "))
    guess_col = int(input("Entrez un numéro de colonne (0, 1 ou 2) : "))

    if grid[guess_row][guess_col] == '#':
        print("Touché !")
        hits += 1
        grid[guess_row][guess_col] = 'X'
    else:
        print("Plouf !")
    
    print_grid()

print("Félicitations, vous avez coulé le navire !")