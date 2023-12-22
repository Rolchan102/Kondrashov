def is_point_inside_triangle(p, a, b, c):
    # Функция, проверяющая, лежит ли точка внутри треугольника
    def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

    d1 = sign(p, a, b)
    d2 = sign(p, b, c)
    d3 = sign(p, c, a)

    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

    return not (has_neg and has_pos)


def count_points_inside_triangle(points, triangle_vertices):
    count = 0
    a, b, c = triangle_vertices

    for point in points:
        if is_point_inside_triangle(point, a, b, c):
            count += 1

    return count


# Пример использования
triangle_vertices = [(0, 0), (1, 0), (0.5, 1)]
points = [(0.2, 0.2), (0.5, 0.5), (0.8, 0.2), (0.3, 0.7), (0.7, 0.7)]

result = count_points_inside_triangle(points, triangle_vertices)

print("Количество точек, попадающих внутрь треугольника:", result)
