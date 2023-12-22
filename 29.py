from sortedcontainers import SortedList


class Event:
    def __init__(self, x, segment, event_type):
        self.x = x
        self.segment = segment
        self.event_type = event_type

    def __lt__(self, other):
        return self.x < other.x or (self.x == other.x and self.event_type < other.event_type)


def sweep_line(segments):
    events = []

    for segment in segments:
        events.append(Event(segment[0][0], segment, "left"))
        events.append(Event(segment[1][0], segment, "right"))

    events.sort()

    active_segments = SortedList()
    intersections = []

    for event in events:
        if event.event_type == "left":
            active_segments.add(event.segment)
            above = active_segments.bisect_left(event.segment)
            below = above - 1

            if above < len(active_segments):
                if intersect(event.segment, active_segments[above]):
                    intersections.append((event.segment, active_segments[above]))

            if below >= 0:
                if intersect(event.segment, active_segments[below]):
                    intersections.append((event.segment, active_segments[below]))

        elif event.event_type == "right":
            above = active_segments.bisect_left(event.segment)
            below = above - 1

            if above < len(active_segments) and below >= 0:
                if intersect(active_segments[above], active_segments[below]):
                    intersections.append((active_segments[above], active_segments[below]))

            active_segments.remove(event.segment)

    return intersections


def intersect(segment1, segment2):
    x1, y1 = segment1[0]
    x2, y2 = segment1[1]
    x3, y3 = segment2[0]
    x4, y4 = segment2[1]

    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0
        return 1 if val > 0 else 2

    o1 = orientation((x1, y1), (x2, y2), (x3, y3))
    o2 = orientation((x1, y1), (x2, y2), (x4, y4))
    o3 = orientation((x3, y3), (x4, y4), (x1, y1))
    o4 = orientation((x3, y3), (x4, y4), (x2, y2))

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and on_segment((x1, y1), (x3, y3), (x2, y2)):
        return True
    if o2 == 0 and on_segment((x1, y1), (x4, y4), (x2, y2)):
        return True
    if o3 == 0 and on_segment((x3, y3), (x1, y1), (x4, y4)):
        return True
    if o4 == 0 and on_segment((x3, y3), (x2, y2), (x4, y4)):
        return True

    return False


def on_segment(p, q, r):
    return min(q[0], r[0]) <= p[0] <= max(q[0], r[0]) and min(q[1], r[1]) <= p[1] <= max(q[1], r[1])


# Пример использования
if __name__ == "__main__":
    input_segments = [((1, 1), (4, 4)), ((2, 0), (5, 3)), ((5, 2), (7, 1)), ((2, 5), (6, 1))]
    intersections = sweep_line(input_segments)
    print("Пересечения отрезков:", intersections)
