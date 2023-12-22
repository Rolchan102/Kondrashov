def area_of_triangle(point1, point2, point3):
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)


def find_second_minimum_area_triangle(points):
    n = len(points)
    min_area = float('inf')
    second_min_area = float('inf')
    min_triangle = None
    second_min_triangle = None

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                current_area = area_of_triangle(points[i], points[j], points[k])

                if current_area > 0:
                    if current_area < min_area:
                        second_min_area = min_area
                        second_min_triangle = min_triangle
                        min_area = current_area
                        min_triangle = (points[i], points[j], points[k])
                    elif current_area < second_min_area:
                        second_min_area = current_area
                        second_min_triangle = (points[i], points[j], points[k])

    return second_min_triangle, second_min_area


# Пример использования
points = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 2)]
second_min_triangle, second_min_area = find_second_minimum_area_triangle(points)

print("Вторая по минимальности ненулевая площадь:", second_min_area)
print("Тройка точек, образующая второй по минимальности треугольник:", second_min_triangle)
