def point_in_star_polygon(point, star_polygon):
    x, y = point
    intersections = 0
    n = len(star_polygon)

    for i in range(n):
        x1, y1 = star_polygon[i]
        x2, y2 = star_polygon[(i + 1) % n]

        # Проверка, лежит ли точка на горизонтальном ребре многоугольника
        if y == y1 == y2 and min(x1, x2) <= x <= max(x1, x2):
            return "На границе"

        # Проверка, лежит ли точка выше или ниже ребра многоугольника
        if min(y1, y2) <= y <= max(y1, y2):
            # Проверка, лежит ли точка справа от ребра
            if x > max(x1, x2):
                intersections += 1
            # Проверка, лежит ли точка слева от ребра
            elif x < min(x1, x2):
                intersections += 1
            # Проверка, лежит ли точка на вершине ребра (пересекает вершину)
            elif y1 == y2 and x == x1:
                intersections += 1
            # Проверка, лежит ли точка выше ребра и находится справа от вершины ребра
            elif y > y1 and y > y2 and x1 < x2:
                intersections += 1
            # Проверка, лежит ли точка выше ребра и находится слева от вершины ребра
            elif y > y1 and y > y2 and x1 > x2:
                intersections += 1
            # Проверка, лежит ли точка ниже ребра и находится справа от вершины ребра
            elif y < y1 and y < y2 and x1 < x2:
                intersections += 1
            # Проверка, лежит ли точка ниже ребра и находится слева от вершины ребра
            elif y < y1 and y < y2 and x1 > x2:
                intersections += 1

    # Если количество пересечений нечетное, точка внутри многоугольника
    return "Внутри" if intersections % 2 == 1 else "Снаружи"


# Пример использования
if __name__ == "__main__":
    star_polygon = [(1, 1), (3, 5), (5, 1), (3, 3), (7, 3)]
    point_inside = (4, 4)
    point_outside = (2, 2)

    result_inside = point_in_star_polygon(point_inside, star_polygon)
    result_outside = point_in_star_polygon(point_outside, star_polygon)

    print(f"Точка {point_inside} находится {result_inside} многоугольника.")
    print(f"Точка {point_outside} находится {result_outside} многоугольника.")
