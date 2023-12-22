from shapely.geometry import Point, Polygon


def distance_to_polygon(polygon, point):
    if polygon.contains(point):
        return 0.0  # Точка внутри многоугольника, расстояние равно нулю

    # Найдем ближайшую точку на границе многоугольника
    nearest_point_on_boundary = polygon.exterior.interpolate(polygon.exterior.project(point))

    # Рассчитаем расстояние между точкой и ближайшей точкой на границе многоугольника
    distance = point.distance(nearest_point_on_boundary)

    return distance


# Пример использования
polygon_coords = [(0, 0), (0, 5), (5, 5), (5, 0)]
point_coords = (8, 3)

polygon = Polygon(polygon_coords)
point = Point(point_coords)

distance = distance_to_polygon(polygon, point)
print("Расстояние от точки до многоугольника:", distance)
