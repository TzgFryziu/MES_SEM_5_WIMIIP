import numpy as np
from Jacobian import Jacobian


class ElemUniv:
    def __init__(self, scheme="2-point"):
        if scheme == "2-point":
            self.ksi = np.array(
                [-1 / np.sqrt(3), 1 / np.sqrt(3), 1 / np.sqrt(3), -1 / np.sqrt(3)]
            )
            self.eta = np.array(
                [-1 / np.sqrt(3), -1 / np.sqrt(3), 1 / np.sqrt(3), 1 / np.sqrt(3)]
            )
            self.weights = np.array([1, 1, 1, 1])
        elif scheme == "3-point":
            sqrt_3_5 = np.sqrt(3 / 5)
            self.eta = np.array(
                [
                    -sqrt_3_5,
                    0,
                    sqrt_3_5,  # pc1, pc2, pc3
                    -sqrt_3_5,
                    0,
                    sqrt_3_5,  # pc4, pc5, pc6
                    -sqrt_3_5,
                    0,
                    sqrt_3_5,  # pc7, pc8, pc9
                ]
            )
            self.ksi = np.array(
                [
                    -sqrt_3_5,
                    -sqrt_3_5,
                    -sqrt_3_5,  # pc1, pc2, pc3
                    0,
                    0,
                    0,  # pc4, pc5, pc6
                    sqrt_3_5,
                    sqrt_3_5,
                    sqrt_3_5,  # pc7, pc8, pc9
                ]
            )
            self.weights = np.array([5 / 9, 8 / 9, 5 / 9])
        else:
            raise ValueError("Scheme must be '2-point' or '3-point'")

        self.dN_dksi = []
        self.dN_deta = []
        for i in range(len(self.ksi)):
            ksi = self.ksi[i]
            eta = self.eta[i]
            self.dN_dksi.append(
                np.array(
                    [
                        -0.25 * (1 - eta),
                        0.25 * (1 - eta),
                        0.25 * (1 + eta),
                        -0.25 * (1 + eta),
                    ]
                )
            )
            self.dN_deta.append(
                np.array(
                    [
                        -0.25 * (1 - ksi),
                        -0.25 * (1 + ksi),
                        0.25 * (1 + ksi),
                        0.25 * (1 - ksi),
                    ]
                )
            )

    def calculate_jacobian(self, points):
        x = np.array([point[0] for point in points])
        y = np.array([point[1] for point in points])

        results = []

        for i in range(len(self.dN_dksi)):
            J = np.zeros((2, 2))

            for j in range(4):
                J[0, 0] += self.dN_dksi[i][j] * x[j]  # ∂x/∂ksi
                J[0, 1] += self.dN_dksi[i][j] * y[j]  # ∂y/∂ksi
                J[1, 0] += self.dN_deta[i][j] * x[j]  # ∂x/∂eta
                J[1, 1] += self.dN_deta[i][j] * y[j]  # ∂y/∂eta

            results.append(Jacobian(J))

            # print(f"integration point{i + 1}:")
            # print("jacobi matrix:\n", results[i].j)
            # print("det j:", results[i].detj)
            # print("inverse j:\n", results[i].j1)
            # print("\n")

        return results

    def calculate_h_matrix(self, points, k):
        jacobians = self.calculate_jacobian(points)
        H = np.zeros((4, 4))

        # Obliczanie macierzy H dla każdego punktu całkowania i akumulacja ważonej sumy
        for i, jacobian_data in enumerate(jacobians):
            J_inv = jacobian_data.J1
            detJ = jacobian_data.detJ

            # Oblicz dN/dx i dN/dy dla każdej funkcji kształtu w tym punkcie całkowania
            dN_dx = []
            dN_dy = []
            for j in range(4):
                dN_dx_j = (
                    J_inv[0, 0] * self.dN_dksi[i][j] + J_inv[0, 1] * self.dN_deta[i][j]
                )
                dN_dy_j = (
                    J_inv[1, 0] * self.dN_dksi[i][j] + J_inv[1, 1] * self.dN_deta[i][j]
                )
                dN_dx.append(dN_dx_j)
                dN_dy.append(dN_dy_j)

            # Oblicz lokalną macierz H w tym punkcie całkowania
            h_local = np.zeros((4, 4))
            for m in range(4):
                for n in range(4):
                    h_local[m, n] = (
                        k * (dN_dx[m] * dN_dx[n] + dN_dy[m] * dN_dy[n]) * detJ
                    )

            w_ksi = self.weights[i % len(self.weights)]  # waga zależna od ksi
            w_eta = self.weights[i // len(self.weights)]  # waga zależna od eta
            h_local_weighted = h_local * w_ksi * w_eta

            # Wypisz ważoną lokalną macierz H dla tego punktu całkowania
            # print(
            #     f"Weigthed local H matrix at integration point {i+1}:\n",
            #     h_local_weighted,
            # )

            # Dodaj ważoną lokalną macierz H do globalnej macierzy H
            H += h_local_weighted

        # Wypisz końcową macierz H
        # print("Final H matrix:\n", H)

        return H


def main():
    elem = ElemUniv(scheme="2-point")
    points = []
    with open("wsp_scinanie", "r") as f:
        linie = f.readlines()
        for linia in linie:
            linia = linia.strip()
            linia = linia.split(",")
            points.append((float(linia[0]), float(linia[1])))
    elem.calculate_h_matrix(points)


if __name__ == "__main__":
    main()
