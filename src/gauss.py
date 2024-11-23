from math import sqrt


def gauss_quadrature_2d(f, scheme="2-point"):
    if scheme == "2-point":
        points = [sqrt(1 / 3), -sqrt(1 / 3)]
        weights = [1, 1]
    elif scheme == "3-point":
        points = [sqrt(3 / 5), 0, -sqrt(3 / 5)]
        weights = [5 / 9, 8 / 9, 5 / 9]
    else:
        raise ValueError("Choose between 2 or 3 points method")
    integral = 0.0
    for i, x in enumerate(points):
        for j, y in enumerate(points):
            integral += weights[i] * weights[j] * f(x, y)
    return integral


def f1(x, y):
    return -5 * x**2 * y + 2 * x * y + 10


integral_2_point = gauss_quadrature_2d(f1, "2-point")
integral_3_point = gauss_quadrature_2d(f1, "3-point")

print(integral_2_point, integral_3_point)
