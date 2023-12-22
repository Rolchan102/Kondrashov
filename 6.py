def draw_line(x1, y1, x2, y2):
    points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    error = dx - dy

    while True:
        points.append((x1, y1))

        if x1 == x2 and y1 == y2:
            break

        e2 = 2 * error

        if e2 > -dy:
            error -= dy
            x1 += sx

        if e2 < dx:
            error += dx
            y1 += sy

    return points


def points_on_polygon_edges(vertices):
    total_points = set()

    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % len(vertices)]

        line_points = draw_line(x1, y1, x2, y2)
        total_points.update(line_points)

    return total_points


# Пример использования
polygon_vertices = [(0, 0), (0, 5), (5, 5), (5, 0)]

result_points = points_on_polygon_edges(polygon_vertices)
print("Количество целочисленных точек на сторонах многоугольника:", len(result_points))
