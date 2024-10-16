from math import sqrt


def gauss_quadrature_2d(f, p,a,b,c,d):

    if p == 2:
        points = [sqrt(1 / 3), -sqrt(1 / 3)]
        weights = [1, 1]
    elif p == 3:
        points = [sqrt(3 / 5), 0, -sqrt(3 / 5)]
        weights = [5 / 9, 8 / 9, 5 / 9]
    else:
        raise ValueError("Choose between 2 or 3 points method")

    integral = 0.0
    for i, x in enumerate(points):
        for j, y in enumerate(points):
            x_mapped = 0.5 * (b - a) * x + 0.5 * (a + b)
            y_mapped = 0.5 * (d - c) * y + 0.5 * (c + d)

            f_value = f(x_mapped, y_mapped)

            integral += weights[i] * weights[j] * f_value

    integral *= 0.25 * (b - a) * (d - c)

    return integral

def f1(x, y):
    return -5 * x**2 * y + 2 * x * y + 10


integral_2_point = gauss_quadrature_2d(f1, 2,-1,1,-1,1)
integral_3_point = gauss_quadrature_2d(f1, 3,-1,1,-1,1)

print(integral_2_point, integral_3_point)
