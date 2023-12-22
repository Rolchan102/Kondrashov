import numpy as np
from scipy.spatial import ConvexHull


def minimum_area_rectangle(points):
    points = np.array(points)
    hull = ConvexHull(points)

    min_area = float('inf')

    for i in range(len(hull.vertices)):
        p1 = hull.points[hull.vertices[i]]
        p2 = hull.points[hull.vertices[(i + 1) % len(hull.vertices)]]
        edge_vector = p2 - p1

        perpendicular_vector = np.array([-edge_vector[1], edge_vector[0]])

        min_x = min(np.dot(points, edge_vector))
        max_x = max(np.dot(points, edge_vector))

        min_y = min(np.dot(points, perpendicular_vector))
        max_y = max(np.dot(points, perpendicular_vector))

        area = (max_x - min_x) * (max_y - min_y)
        min_area = min(min_area, area)

    return min_area


# Пример использования
points = [(0, 0), (1, 1), (1, 0), (0, 1), (0.5, 0.5)]
result = minimum_area_rectangle(points)

print("Минимальная площадь прямоугольника:", result)
