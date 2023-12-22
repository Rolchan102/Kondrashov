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


def points_on_polygon_boundary(polygon):
    boundary_points = set()

    n = len(polygon)

    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]

        line_points = draw_line(x1, y1, x2, y2)
        boundary_points.update(line_points)

    return boundary_points


# Пример использования
polygon_vertices = [(0, 0), (0, 5), (5, 5), (5, 0)]
result_points = points_on_polygon_boundary(polygon_vertices)
print("Множество точек на границе многоугольника:", result_points)
