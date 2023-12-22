from shapely.geometry import Point, Polygon, LineString


def find_furthest_side(polygon, point):
    max_distance = 0
    far_side = None

    for i in range(len(polygon.exterior.coords) - 1):
        side = LineString([polygon.exterior.coords[i], polygon.exterior.coords[i + 1]])
        distance = side.distance(point)

        if distance > max_distance:
            max_distance = distance
            far_side = side

    return far_side


# Пример использования
polygon_coords = [(0, 0), (0, 5), (5, 5), (5, 0)]
point_coords = (1, 1)

polygon = Polygon(polygon_coords)
point = Point(point_coords)

furthest_side = find_furthest_side(polygon, point)
print("Наиболее удаленная сторона:", furthest_side)
