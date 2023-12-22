def count_intersections(x1, y1, x2, y2):
    # Определение границ отрезка
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)

    # Определение числа пересечений
    vertical_intersections = max_x - min_x
    horizontal_intersections = max_y - min_y

    total_intersections = vertical_intersections + horizontal_intersections

    return total_intersections


# Пример использования
x1, y1 = 1, 2
x2, y2 = 4, 5

result = count_intersections(x1, y1, x2, y2)
print("Число пересечений:", result)
