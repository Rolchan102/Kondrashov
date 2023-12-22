import numpy as np
from scipy.spatial import Delaunay


def point_location(triangulation, point):
    # Находит треугольник, внутри которого находится данная точка
    for simplex in triangulation.simplices:
        A, B, C = triangulation.points[simplex]
        D = np.array(point)

        sign_ABD = np.linalg.det([[A[0] - D[0], A[1] - D[1]], [B[0] - D[0], B[1] - D[1]]])
        sign_BCD = np.linalg.det([[B[0] - D[0], B[1] - D[1]], [C[0] - D[0], C[1] - D[1]]])
        sign_CAD = np.linalg.det([[C[0] - D[0], C[1] - D[1]], [A[0] - D[0], A[1] - D[1]]])

        if (sign_ABD > 0 and sign_BCD > 0 and sign_CAD > 0) or (sign_ABD < 0 and sign_BCD < 0 and sign_CAD < 0):
            return simplex

    return None


# Пример использования
points = np.array([(0, 0), (1, 0), (0.5, 1), (0.5, 0.5)])
triangulation = Delaunay(points)

point_to_locate = (0.5, 0.5)
triangle_index = point_location(triangulation, point_to_locate)

if triangle_index is not None:
    print(
        f"Точка {point_to_locate} находится внутри треугольника с вершинами {triangulation.simplices[triangle_index]}")
else:
    print(f"Точка {point_to_locate} не принадлежит ни одному треугольнику в триангуляции.")
