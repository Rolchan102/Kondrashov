def centroid_of_polygon(vertices):
    n = len(vertices)
    if n == 0:
        return None

    sum_x = sum(x for x, y in vertices)
    sum_y = sum(y for x, y in vertices)

    centroid_x = sum_x / n
    centroid_y = sum_y / n

    return (centroid_x, centroid_y)


# Пример использования
polygon_vertices = [(0, 0), (0, 5), (5, 5), (5, 0)]
centroid = centroid_of_polygon(polygon_vertices)

print("Центр тяжести многоугольника:", centroid)
