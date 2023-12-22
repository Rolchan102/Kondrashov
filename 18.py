def are_parallel(segment1, segment2):
    # Проверка, являются ли отрезки параллельными
    x1, y1, x2, y2 = segment1
    x3, y3, x4, y4 = segment2

    slope1 = (y2 - y1) / (x2 - x1) if x2 - x1 != 0 else float('inf')
    slope2 = (y4 - y3) / (x4 - x3) if x4 - x3 != 0 else float('inf')

    return slope1 == slope2


def count_parallel_segments_pairs(segments):
    count = 0
    n = len(segments)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if are_parallel(segments[i], segments[j]):
                count += 1

    return count


# Пример использования
segments = [(0, 0, 1, 1), (0, 1, 1, 0), (0, 2, 2, 0), (2, 2, 3, 3)]
result = count_parallel_segments_pairs(segments)

print("Количество различных пар параллельных отрезков:", result)
