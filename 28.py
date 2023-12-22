from math import atan2


def graham_scan(points):
    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0  # Коллинеарны
        return 1 if val > 0 else 2  # По часовой или против часовой

    def graham_compare(p1, p2):
        o = orientation(p0, p1, p2)
        if o == 0:
            return -1 if distance(p0, p2) >= distance(p0, p1) else 1
        return -1 if o == 2 else 1

    def distance(p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    if len(points) < 3:
        return points  # Невозможно построить выпуклую оболочку

    # Найти точку с минимальной y-координатой (и самой левой, если таких точек несколько)
    p0 = min(points, key=lambda point: (point[1], point[0]))

    # Сортировка точек с учетом угла относительно p0
    sorted_points = sorted(points, key=lambda point: (atan2(point[1] - p0[1], point[0] - p0[0]), point))

    # Удаляем коллинеарные точки
    filtered_points = [sorted_points[0]]
    for i in range(1, len(sorted_points)):
        while i < len(sorted_points) - 1 and orientation(p0, sorted_points[i], sorted_points[i + 1]) == 0:
            i += 1
        filtered_points.append(sorted_points[i])

    # Если после фильтрации осталось меньше 3 точек, возвращаем оставшиеся точки
    if len(filtered_points) < 3:
        return filtered_points

    # Инициализация стека
    stack = [filtered_points[0], filtered_points[1], filtered_points[2]]

    # Обработка оставшихся точек
    for i in range(3, len(filtered_points)):
        while len(stack) > 1 and orientation(stack[-2], stack[-1], filtered_points[i]) != 2:
            stack.pop()
        stack.append(filtered_points[i])

    return stack


# Пример использования
if __name__ == "__main__":
    input_points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
    convex_hull = graham_scan(input_points)
    print("Выпуклая оболочка:", convex_hull)
