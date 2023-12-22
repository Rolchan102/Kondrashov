from scipy.spatial import ConvexHull
import numpy as np


def convex_hull_area(points):
    hull = ConvexHull(points)
    return hull.volume  # volume возвращает площадь в 2D случае


# Пример использования
points = np.array([(0, 0), (1, 1), (2, 2), (0, 3), (-1, 2)])

area = convex_hull_area(points)
print("Площадь выпуклой оболочки:", area)
