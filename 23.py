from sortedcontainers import SortedList


class Event:
    def __init__(self, x, segment, is_start):
        self.x = x
        self.segment = segment
        self.is_start = is_start

    def __lt__(self, other):
        # События сортируются по координате x
        return self.x < other.x


def find_intersection_points(segments):
    events = []

    for x1, y1, x2, y2 in segments:
        # Создаем события для начала и конца отрезка
        start_event = Event(x1, (x1, y1, x2, y2), is_start=True)
        end_event = Event(x2, (x1, y1, x2, y2), is_start=False)

        events.extend([start_event, end_event])

    # Сортируем события по координате x
    events.sort()

    active_segments = SortedList()
    intersection_points = []

    for event in events:
        x, (x1, y1, x2, y2), is_start = event.x, event.segment, event.is_start

        if is_start:
            # Добавляем отрезок в активные
            active_segments.add((y1, (x1, y1, x2, y2)))
        else:
            # Удаляем отрезок из активных
            active_segments.remove((y1, (x1, y1, x2, y2)))

        # Проверяем пересечения с соседними активными отрезками
        index = active_segments.bisect_left((y1, (x1, y1, x2, y2)))

        if 0 < index < len(active_segments):
            # Если есть сосед слева, проверяем пересечение
            _, (x3, y3, x4, y4) = active_segments[index - 1]
            intersection_points.append((x, y1 + (x - x3) * (y4 - y3) / (x4 - x3)))

        if 0 < index < len(active_segments) - 1:
            # Если есть сосед справа, проверяем пересечение
            _, (x5, y5, x6, y6) = active_segments[index + 1]
            intersection_points.append((x, y1 + (x - x5) * (y6 - y5) / (x6 - x5)))

    return intersection_points


# Пример использования
segments = [(1, 1, 3, 3), (2, 1, 2, 4), (1, 2, 4, 2)]
intersection_points = find_intersection_points(segments)

print("Множество точек пересечения:", intersection_points)
