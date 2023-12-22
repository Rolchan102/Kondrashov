def area_of_triangle(point1, point2, point3):
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)


def find_maximum_area_triangle(points):
    n = len(points)
    max_area = 0
    max_triangle = None

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                current_area = area_of_triangle(points[i], points[j], points[k])

                if current_area > max_area:
                    max_area = current_area
                    max_triangle = (points[i], points[j], points[k])

    return max_triangle, max_area


# Пример использования
points = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 2)]
max_triangle, max_area = find_maximum_area_triangle(points)

print("Максимальная площадь треугольника:", max_area)
print("Тройка точек, образующая треугольник максимальной площади:", max_triangle)
