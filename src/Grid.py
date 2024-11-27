import numpy as np

from src.ElemUniv import ElemUniv


class Grid:
    def __init__(self, elem_arr, node_arr) -> None:
        self.nodes_number = len(node_arr)
        self.elements_number = len(elem_arr)
        self.elem_arr = elem_arr
        self.node_arr = node_arr

        for elem in elem_arr:
            elem.points = [node_arr[i] for i in elem.id]

    def create_global_h_matrix(self, k, verbose=False):
        H = np.zeros((self.nodes_number, self.nodes_number))
        univ = ElemUniv("2-point")
        for elem in self.elem_arr:
            points = []
            for node in elem.points:
                points.append([node.x, node.y])
            h = univ.calculate_h_matrix(points, k)
            if verbose:
                print(f"Element {elem.id}")
                print(h)
            for i in range(4):
                for j in range(4):
                    H[elem.id[i], elem.id[j]] += h[i, j]
        return H

    def print_elem(self):
        for elem in self.elem_arr:
            print(elem)

    def display(self) -> str:

        print("*Node")
        for i in range(len(self.node_arr)):
            print(f"   {i}. {self.node_arr[i]}")

        print("\n*Element")
        for i in range(len(self.elem_arr)):
            print(f"   {i}. {self.elem_arr[i]}")
