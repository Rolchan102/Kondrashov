from sympy import symbols, Eq, solve


def count_intersection_points(equations):
    x, y = symbols('x y')
    points = set()

    for equation in equations:
        left, right = equation.split('=')
        left_expr = eval(left)
        right_expr = eval(right)
        equation = Eq(left_expr, right_expr)
        intersection_point = solve(equation, (x, y))

        if intersection_point:
            points.add(intersection_point[0])

    return points


# Пример использования (список уравнений прямых в виде строк)
equations = ["2*x + 3*y = 6", "4*x - 2*y = 8", "5*x + y = 10"]
intersection_points = count_intersection_points(equations)

print("Число точек пересечения:", len(intersection_points))
print("Точки пересечения:", intersection_points)
