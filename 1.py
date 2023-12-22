from shapely.geometry import Point, Polygon, LineString


def find_near_side(polygon, point):
    min_distance = float('inf')
    near_side = None

    for i in range(len(polygon.exterior.coords) - 1):
        side = LineString([polygon.exterior.coords[i], polygon.exterior.coords[i + 1]])
        distance = side.distance(point)

        if distance < min_distance:
            min_distance = distance
            near_side = side

    return near_side


# Пример использования
polygon_coords = [(0, 0), (0, 5), (5, 5), (5, 0)]
point_coords = (1, 1)

polygon = Polygon(polygon_coords)
point = Point(point_coords)

nearest_side = find_near_side(polygon, point)
print("Наименее удаленная сторона:", nearest_side)
