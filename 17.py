from itertools import combinations


def count_intersection_segments(lines):
    intersection_points = set()

    # Находим все точки пересечения прямых
    for i in range(len(lines) - 1):
        for j in range(i + 1, len(lines)):
            intersection = find_intersection(lines[i], lines[j])
            if intersection:
                intersection_points.add(intersection)

    # Находим все вершины отрезков
    segment_vertices = set()
    for line in lines:
        x1, y1, x2, y2 = line
        segment_vertices.add((x1, y1))
        segment_vertices.add((x2, y2))

    # Добавляем точки пересечения, которые не являются вершинами отрезков
    intersection_points -= segment_vertices

    # Формируем отрезки, учитывая бесконечные отрезки
    segments = []
    for point in intersection_points:
        for vertex in segment_vertices:
            if point != vertex:
                segments.append((point, vertex))

    return len(segments)


def find_intersection(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2

    det = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

    if det == 0:
        return None  # Прямые параллельны или совпадают

    intersection_x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / det
    intersection_y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / det

    return (intersection_x, intersection_y)


# Пример использования
lines = [(0, 0, 1, 1), (0, 1, 1, 0), (0, 2, 2, 0)]
result = count_intersection_segments(lines)

print("Число полученных отрезков с вершинами в точках пересечения:", result)
