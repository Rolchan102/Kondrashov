import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import random


class Node:
    def __init__(self, point, left=None, right=None, axis=None):
        self.point = point
        self.left = left
        self.right = right
        self.axis = axis


class KDTree:
    def __init__(self, points):
        self.root = self.build_kdtree(points)

    def build_kdtree(self, points, depth=0):
        if not points:
            return None

        axis = depth % len(points[0])
        points.sort(key=lambda x: x[axis])

        median = len(points) // 2
        return Node(
            point=points[median],
            left=self.build_kdtree(points[:median], depth + 1),
            right=self.build_kdtree(points[median + 1:], depth + 1),
            axis=axis
        )

    def range_query(self, root, rect_min, rect_max, depth=0, result=[]):
        if root is None:
            return

        axis = depth % len(root.point)
        if rect_min[axis] <= root.point[axis] <= rect_max[axis]:
            if all(rect_min[i] <= root.point[i] <= rect_max[i] for i in range(len(rect_min))):
                result.append(root.point)

        if root.point[axis] >= rect_min[axis]:
            self.range_query(root.left, rect_min, rect_max, depth + 1, result)

        if root.point[axis] <= rect_max[axis]:
            self.range_query(root.right, rect_min, rect_max, depth + 1, result)

    def visualize(self, root, rect_min=None, rect_max=None, ax=None):
        if ax is None:
            fig, ax = plt.subplots()

        if root is not None:
            ax.plot(root.point[0], root.point[1], 'bo')

            if rect_min is not None and rect_max is not None:
                ax.add_patch(plt.Rectangle(rect_min, rect_max[0] - rect_min[0], rect_max[1] - rect_min[1], fill=False,
                                           edgecolor='red'))

            if root.left is not None:
                self.visualize(root.left, rect_min, rect_max, ax)

            if root.right is not None:
                self.visualize(root.right, rect_min, rect_max, ax)

        plt.show()


# Пример использования
if __name__ == "__main__":
    # Генерация случайных точек
    random.seed(42)
    points = [(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(20)]

    # Создание kd-дерева
    kdtree = KDTree(points)

    # Задание прямоугольника для поиска точек
    rect_min = (2, 2)
    rect_max = (8, 8)

    # Поиск точек в прямоугольнике
    result_points = []
    kdtree.range_query(kdtree.root, rect_min, rect_max, result=result_points)
    print("Points in rectangle:", result_points)

    # Визуализация
    kdtree.visualize(kdtree.root, rect_min, rect_max)
