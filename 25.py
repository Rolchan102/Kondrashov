from tkinter import *
from itertools import combinations
from math import sqrt
from collections import OrderedDict


def distance(x1, y1, x2, y2):
    """Считает длину отрезка по координатам начала и конца"""
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def is_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    """Проверяет, пересекаются ли прямые. Случай, когда точкой пересечения являются концы отрезков (одна из вершин многоугольника) пересечением не считаются."""
    if min(x1, x2) <= max(x3, x4) and min(y3, y4) <= max(y1, y2) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(
            y3, y4):
        if ((x1 == x3) and (y1 == y3)) or ((x2 == x4) and (y2 == y4)) or ((x1 == x4) and (y1 == y4)) or (
                (x2 == x3) and (y2 == y3)):
            return False
        return True
    else:
        return False


def save_cord(event):
    """Сохраняет координаты, проставленные при помощи ЛКМ."""
    global loops, n
    coordinates.append((event.x, event.y))
    canvas.create_rectangle(event.x, event.y, event.x + 2, event.y + 2, width=2)
    loops += 1

    if loops == n:
        triangulate()


def triangulate():
    global coordinates
    # сохраняем рёбра многоугольника в список default
    for i in range(len(coordinates) - 1):
        default.append(list(coordinates[i]) + list(coordinates[i + 1]))

    # ребро, соединяющее начало и конец
    default.append(list(coordinates[0]) + list(coordinates[-1]))

    # Генерируем список всех возможных отрезков, соединяющих пары исходных точек.
    coordinates = list(combinations(coordinates, 2))
    # Преобразовываем координаты начала и конца к виду (x1,y1, x2,y2,x3,y3,x4,y4)
    for i in range(len(coordinates)):
        coordinates[i] = coordinates[i][0] + coordinates[i][1]

    # создаём словарь, в котором ключами будут координаты начала и конца отрезка, а значение будет хранить его длину
    dict_lenth = {}

    for i in coordinates:
        dict_lenth[i] = distance(*i)

    sorted_lenth = OrderedDict(sorted(dict_lenth.items(), key=lambda x: x[1]))
    sorted_coord = list(sorted_lenth.keys())

    # удаляем из всех возможных комбинаций те, которые уже использованы в каркасе
    for i in default:
        if tuple(i) in sorted_coord:
            sorted_coord.remove(tuple(i))

    # тут хранятся все вставленные рёбра
    inserted = []
    inserted.append(sorted_coord[0])

    for i in range(1, len(sorted_coord)):
        check = True
        for j in inserted:
            if is_intersect(*sorted_coord[i], *j):
                check = False
                break
        if check:
            inserted.append(sorted_coord[i])

    for i in default:
        canvas.create_line(*i)
    for i in inserted:
        canvas.create_line(*i)


tk = Tk()
canvas = Canvas(tk, height=800, width=800)
canvas.pack()

default = []
n = int(input("Введите количество точек многоугольника: "))
coordinates = []
loops = 0
canvas.bind("<Button-1>", save_cord)

tk.mainloop()
