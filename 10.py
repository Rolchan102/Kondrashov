def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        return 0

    area = 0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += (x1 * y2 - x2 * y1)

    area = abs(area) / 2.0
    return area


def centroid_of_polygon(vertices):
    n = len(vertices)
    if n < 3:
        return None

    sum_x = 0
    sum_y = 0
    total_length = 0

    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]

        length = distance((x1, y1), (x2, y2))
        total_length += length

        sum_x += (x1 + x2) * length
        sum_y += (y1 + y2) * length

    centroid_x = sum_x / (3 * total_length)
    centroid_y = sum_y / (3 * total_length)

    return (centroid_x, centroid_y)


# Пример использования
polygon_vertices = [(0, 0), (0, 5), (5, 5), (5, 0)]
centroid = centroid_of_polygon(polygon_vertices)

print("Центр тяжести многоугольника (по 2D мере границы):", centroid)
