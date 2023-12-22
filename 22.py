import math


def orientation(p, q, r):
    # Функция, определяющая ориентацию тройки точек (p, q, r)
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Точки коллинеарны
    return 1 if val > 0 else 2  # 1 - по часовой стрелке, 2 - против часовой стрелки


def graham_scan(points):
    n = len(points)

    # Если меньше трех точек, то выпуклая оболочка не определена
    if n < 3:
        return None

    # Находим точку с наименьшей y-координатой (и самой левой, если таких точек несколько)
    pivot = min(points, key=lambda x: (x[1], x[0]))

    # Сортируем остальные точки по полярному углу относительно pivot
    sorted_points = sorted(points, key=lambda x: (math.atan2(x[1] - pivot[1], x[0] - pivot[0]), x))

    hull = [pivot, sorted_points[0], sorted_points[1]]

    for i in range(2, n):
        while len(hull) > 1 and orientation(hull[-2], hull[-1], sorted_points[i]) != 2:
            hull.pop()
        hull.append(sorted_points[i])

    return hull


# Пример использования
points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
convex_hull = graham_scan(points)

print("Выпуклая оболочка:", convex_hull)
