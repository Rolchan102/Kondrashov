def is_point_inside_polygon(x, y, polygon):
    n = len(polygon)
    inside = False

    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]

        # Проверяем, пересекает ли горизонтальная линия (y) сторону многоугольника
        if min(y1, y2) < y <= max(y1, y2) and x < max(x1, x2):
            # Находим x-координату пересечения линии со стороной многоугольника
            x_intersection = (y - y1) * (x2 - x1) / (y2 - y1) + x1

            # Если x_intersection меньше заданной x-координаты, меняем флаг
            if x <= x_intersection:
                inside = not inside

    return inside


def points_inside_polygon(polygon):
    min_x = min(point[0] for point in polygon)
    max_x = max(point[0] for point in polygon)
    min_y = min(point[1] for point in polygon)
    max_y = max(point[1] for point in polygon)

    inside_points = set()

    for x in range(min_x + 1, max_x):
        for y in range(min_y + 1, max_y):
            if is_point_inside_polygon(x, y, polygon):
                inside_points.add((x, y))

    return inside_points


# Пример использования
polygon_vertices = [(0, 0), (0, 5), (5, 5), (5, 0)]
result_points = points_inside_polygon(polygon_vertices)
print("Множество точек внутри многоугольника:", result_points)
