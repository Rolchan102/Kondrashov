def orientation(p, q, r):
    # Функция, определяющая ориентацию тройки точек (p, q, r)
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Точки коллинеарны
    return 1 if val > 0 else 2  # 1 - по часовой стрелке, 2 - против часовой стрелки


def jarvis_march(points):
    n = len(points)

    # Если меньше трех точек, то выпуклая оболочка не определена
    if n < 3:
        return None

    hull = []

    # Находим самую левую точку в качестве начальной точки выпуклой оболочки
    leftmost = min(points, key=lambda x: x[0])
    hull.append(leftmost)

    current_point = leftmost

    while True:
        next_point = points[0]

        for i in range(1, n):
            if points[i] == current_point:
                continue

            # Если следующая точка лучше текущей точки, обновляем ее
            turn = orientation(current_point, next_point, points[i])
            if turn == 2 or (
                    turn == 0 and (current_point[0] - points[i][0]) ** 2 + (current_point[1] - points[i][1]) ** 2 > (
                    current_point[0] - next_point[0]) ** 2 + (current_point[1] - next_point[1]) ** 2):
                next_point = points[i]

        # Когда найдена следующая точка, добавляем ее в выпуклую оболочку
        if next_point == leftmost:
            break  # Оболочка замкнута
        else:
            hull.append(next_point)
            current_point = next_point

    return hull


# Пример использования
points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
convex_hull = jarvis_march(points)

print("Выпуклая оболочка:", convex_hull)
