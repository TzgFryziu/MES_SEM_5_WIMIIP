from Grid import *
from Node import *
from Element import *
from math import sqrt


class GlobalData:
    def __init__(
        self,
        simulation_time,
        simulation_step_time,
        conductivity,
        alfa,
        tot,
        initial_temp_100,
        density,
        specific_heat,
        nodes_number,
        elements_number,
        width,
        height,
    ) -> None:
        self.simulation_time = simulation_time
        self.simulation_step_time = simulation_step_time
        self.conductivity = conductivity
        self.alfa = alfa
        self.tot = tot
        self.initial_temp_100 = initial_temp_100
        self.density = density
        self.specific_heat = specific_heat
        self.nodes_number = nodes_number
        self.elements_number = elements_number
        self.width = width
        self.height = height

    def __repr__(self) -> str:
        return (
            f"simulation_time={self.simulation_time}, \n"
            f"simulation_step_time={self.simulation_step_time}, \n"
            f"conductivity={self.conductivity}, \nalfa={self.alfa}, \ntot={self.tot}, \n"
            f"initial_temp_100={self.initial_temp_100}, \ndensity={self.density}, \n"
            f"specific_heat={self.specific_heat}, \nnodes_number={self.nodes_number}, \n"
            f"elements_number={self.elements_number}\n"
            f"width={self.width}, height={self.height}"
        )

    def create_grid(self):
        nodes_arr = create_nodes_arr(
            self.nodes_number, self.elements_number, self.width, self.height
        )
        elements_arr = create_elements_arr(self.nodes_number, self.elements_number)
        return Grid(elements_arr, nodes_arr)


def create_nodes_arr(nodes_number, elements_number, width, height):
    nodes_number = int(nodes_number)
    elements_number = int(elements_number)

    step_y = width / (sqrt(nodes_number) - 1)
    step_x = height / (sqrt(nodes_number) - 1)

    res = []

    for i in range(int(sqrt(nodes_number))):
        y = 0 - step_y * i
        for j in range(int(sqrt(nodes_number))):
            x = width - step_x * j
            res.append(Node(x, y))
    return res


def create_elements_arr(nodes_number, elements_number):
    nodes_number_row = int(sqrt(nodes_number))
    res = []
    add = 0
    for i in range(int(elements_number)):
        if (i + 1) % nodes_number_row == 0:
            add += 1
        curr = i + add
        res.append(
            Element(
                [curr, curr + 1, curr + nodes_number_row + 1, curr + nodes_number_row]
            )
        )
    return res
