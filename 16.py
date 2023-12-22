import math


def count_circle_intersections(circles):
    count = 0
    n = len(circles)

    for i in range(n - 1):
        for j in range(i + 1, n):
            x1, y1, r1 = circles[i]
            x2, y2, r2 = circles[j]
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            if distance < r1 + r2:
                # Окружности пересекаются
                count += 2 if distance > abs(r1 - r2) else 1

    return count


# Пример использования
circles = [(0, 0, 1), (0, 1, 1), (1, 1, 1)]
intersection_count = count_circle_intersections(circles)

print("Число точек пересечения окружностей:", intersection_count)
