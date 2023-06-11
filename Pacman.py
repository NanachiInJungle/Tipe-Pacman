import tkinter as tk
import keyboard
import time
import random

hauteur_map = 20
largeur_map = 20


def create_map(hauteur_map, largeur_map):
    map = []
    for i in range(hauteur_map):
        if i == 0 or i == hauteur_map - 1:
            map.append([1 for k in range(largeur_map)])
        else:
            map.append([])
            map[i].append(1)
            for j in range(1, largeur_map - 1):
                map[i].append(0)
            map[i].append(1)
    return map


def neighbours_list(map, i, j):
    neigh_l = []
    if map[i + 1][j] != 1:
        neigh_l.append((i + 1, j))
    if map[i - 1][j] != 1:
        neigh_l.append((i - 1, j))
    if map[i][j + 1] != 1:
        neigh_l.append((i, j + 1))
    if map[i][j - 1] != 1:
        neigh_l.append((i, j - 1))
    return neigh_l


def create_dict_adj(map):
    mat_adj = {}
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0 :
                liste_voisins = neighbours_list(map,i,j)
                mat_adj[(i, j)] = liste_voisins
    #print(mat_adj, len(mat_adj))
    return mat_adj


def position_ini(map):
    pac_man = 5
    map[hauteur_map // 2][largeur_map // 2] = pac_man
    pos_x = hauteur_map // 2
    pos_y = largeur_map // 2
    return map, pos_x, pos_y


def create_condition_sortie(map, pos_x, pos_y):
    while True:
        pos_x_sortie = random.randint(1, hauteur_map - 2)
        pos_y_sortie = random.randint(1, largeur_map - 2)
        if pos_x_sortie != pos_x and pos_y_sortie != pos_y and map[pos_x_sortie][pos_y_sortie] != 1: break
    map[pos_x_sortie][pos_y_sortie] = 3
    return map, pos_x_sortie, pos_y_sortie


def get_key():
    key = keyboard.read_key()
    return key


def test_wall(map, key, pos_x, pos_y):
    if key == "z":
        if pos_x == 1:
            return False
        elif map[pos_x - 1][pos_y] == 1:
            return False
        else:
            return True
    elif key == "s":
        if pos_x == hauteur_map - 2:
            return False
        elif map[pos_x + 1][pos_y] == 1:
            return False
        else:
            return True
    elif key == "d":
        if pos_y == largeur_map - 2:
            return False
        elif map[pos_x][pos_y + 1] == 1:
            return False
        else:
            return True
    elif key == "q":
        if pos_y == 1:
            return False
        elif map[pos_x][pos_y - 1] == 1:
            return False
        else:
            return True


def test_sortie(key, pos_x, pos_y, pos_x_sortie, pos_y_sortie):
    if key == "z" and pos_x - 1 == pos_x_sortie and pos_y == pos_y_sortie:
        return True
    elif key == "s" and pos_x + 1 == pos_x_sortie and pos_y == pos_y_sortie:
        return True
    elif key == "q" and pos_x == pos_x_sortie and pos_y - 1 == pos_y_sortie:
        return True
    elif key == "d" and pos_x == pos_x_sortie and pos_y + 1 == pos_y_sortie:
        return True


def afficher_map_ini(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            x0 = j * 20
            y0 = i * 20
            x1 = x0 + 20
            y1 = y0 + 20
            if map[i][j] == 1:
                canvas.create_rectangle(x0, y0, x1, y1, fill="blue")
            elif map[i][j] == 0:
                canvas.create_rectangle(x0, y0, x1, y1, fill="black")
            elif map[i][j] == 5:
                canvas.create_rectangle(x0, y0, x1, y1, fill="yellow")
            elif map[i][j] == 3:
                canvas.create_rectangle(x0, y0, x1, y1, fill="red")
            elif map[i][j] == 4:
                canvas.create_rectangle(x0, y0, x1, y1, fill="magenta2")


def get_coord_square(pos_x, pos_y):
    l0 = pos_y * 20
    c0 = pos_x * 20
    l1 = l0 + 20
    c1 = c0 + 20
    return l0, c0, l1, c1


def test_key(map, key, pos_x, pos_y):
    if key == "z":
        map[pos_x][pos_y], map[pos_x - 1][pos_y] = map[pos_x - 1][pos_y], map[pos_x][pos_y]
        l0, c0, l1, c1 = get_coord_square(pos_x - 1, pos_y)
        pos_x = pos_x - 1
        return l0, c0, l1, c1, pos_x, pos_y
    elif key == "s":
        map[pos_x][pos_y], map[pos_x + 1][pos_y] = map[pos_x + 1][pos_y], map[pos_x][pos_y]
        l0, c0, l1, c1 = get_coord_square(pos_x + 1, pos_y)
        pos_x = pos_x + 1
        return l0, c0, l1, c1, pos_x, pos_y
    elif key == "d":
        map[pos_x][pos_y], map[pos_x][pos_y + 1] = map[pos_x][pos_y + 1], map[pos_x][pos_y]
        l0, c0, l1, c1 = get_coord_square(pos_x, pos_y + 1)
        pos_y = pos_y + 1
        return l0, c0, l1, c1, pos_x, pos_y
    else:
        map[pos_x][pos_y], map[pos_x][pos_y - 1] = map[pos_x][pos_y - 1], map[pos_x][pos_y]
        l0, c0, l1, c1 = get_coord_square(pos_x, pos_y - 1)
        pos_y = pos_y - 1
        return l0, c0, l1, c1, pos_x, pos_y


def BFS(map, pos_x_e, pos_y_e, pos_x_s, pos_y_s ):
    frontiere = [(pos_x_e, pos_y_e)]
    entree = (pos_x_e, pos_y_e)
    sortie = (pos_x_s, pos_y_s)
    precedent = {entree : None}

    while frontiere: # tant que la liste des cases frontières à la zone connue n'est pas vide
        noeud = frontiere.pop(0) #on étudie la première des cases frontières

        if noeud == sortie: #si la case étudiée est celle de sortie, alors on arrète de parcourir le graphe
            break

        voisins = neighbours_list(map, noeud[0], noeud[1])  # on créer une liste des cases voisines à celle étudiée
        #Pour chacune des cases voisines, on l'associe dans le dictionnaire à la case par laquelle il faut passer juste avant pour l'atteindre
        for voisin in voisins:
            if voisin not in precedent :
                frontiere.append(voisin)
                precedent[voisin] = noeud
    print(sortie, precedent)

    # ici on pars de notre case de sortie dans le dictionnaire et on remonte jusqu'à la case d'arrivée en ajoutant toutes les cases par lesquelles on passe dans la liste chemin
    current = sortie
    chemin =  []
    while current != entree :
        chemin.append(current)
        current = precedent[current]
    chemin.append(entree)
    chemin.reverse() #on inverse la liste pour retrouver le chemin à parcourir de l'entrée à la sortie et non l'inverse
    print(chemin)
    return chemin

def map_chemin(map, chemin):
    for (i,j) in chemin[1:-1]:
        map[i][j] = 4
    return map


def move_pacman():
    #mapini = create_map(hauteur_map, largeur_map)
    mapini = create_map(hauteur_map, largeur_map)
    map1, pos_x, pos_y = position_ini(mapini)
    map, pos_x_sortie, pos_y_sortie = create_condition_sortie(map1, pos_x, pos_y)
    #dico = create_dict_adj(map)
    #for elem in dico.items():
    #    print(elem)
    global root
    global canvas_h
    global canvas_l
    global canvas
    chemin = BFS(map, pos_x, pos_y, pos_x_sortie, pos_y_sortie)
    map = map_chemin(map, chemin)
    root = tk.Tk()
    root.title("Pacman")
    canvas_l = len(map[0]) * 20
    canvas_h = len(map) * 20
    canvas = tk.Canvas(root, width=canvas_l, height=canvas_h)
    canvas.pack()
    afficher_map_ini(map)
    root.update()
    while True:
        key = get_key()
        time.sleep(0.2)
        if key == "z" or key == "s" or key == "q" or key == "d" or key == "r":
            if key == "r":
                break
            elif test_sortie(key, pos_x, pos_y, pos_x_sortie, pos_y_sortie):
                break
            elif test_wall(map, key, pos_x, pos_y):
                x0, y0, x1, y1 = get_coord_square(pos_x, pos_y)
                l0, c0, l1, c1, pos_x, pos_y = test_key(map, key, pos_x, pos_y)
                canvas.create_rectangle(x0, y0, x1, y1, fill="black")
                canvas.create_rectangle(l0, c0, l1, c1, fill="yellow")
                root.update()
    root.destroy()
    return ("Finito")

vrai_map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

move_pacman()
