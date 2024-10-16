from math import sqrt

# Updated coordinates of the nodes
X_COORDS = [0, 4, 4, 0]
Y_COORDS = [0, 0, 4, 5]


def calculate_derivatives_two_points():
    xi = -1 / sqrt(3)
    eta = -1 / sqrt(3)
    dn_dxi = [
        -1 / 4 * (1 - eta),
        1 / 4 * (1 - eta),
        1 / 4 * (1 + eta),
        -1 / 4 * (1 + eta),
    ]
    dn_deta = [-1 / 4 * (1 - xi), -1 / 4 * (1 + xi), 1 / 4 * (1 + xi), 1 / 4 * (1 - xi)]
    return dn_dxi, dn_deta


def calculate_jacobian_component(derivatives, coords):
    return sum(derivative * coord for derivative, coord in zip(derivatives, coords))


dn_dxi, dn_deta = calculate_derivatives_two_points()

dx_dxi = calculate_jacobian_component(dn_dxi, X_COORDS)
dx_deta = calculate_jacobian_component(dn_deta, X_COORDS)
dy_dxi = calculate_jacobian_component(dn_dxi, Y_COORDS)
dy_deta = calculate_jacobian_component(dn_deta, Y_COORDS)

print(dx_dxi, dx_deta, dy_dxi, dy_deta)
