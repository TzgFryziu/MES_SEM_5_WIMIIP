from GlobalData import *
from Grid import *


def file_data(filename) -> GlobalData:
    with open(filename, "r") as file:
        data = {}
        for line in file.readlines():
            key, value = line.strip().rsplit(" ", maxsplit=1)
            data[key] = float(value)

    return GlobalData(
        simulation_time=data["SimulationTime"],
        simulation_step_time=data["SimulationStepTime"],
        conductivity=data["Conductivity"],
        alfa=data["Alfa"],
        tot=data["Tot"],
        initial_temp_100=data["InitialTemp"],
        density=data["Density"],
        specific_heat=data["SpecificHeat"],
        nodes_number=data["Nodes number"],
        elements_number=data["Elements number"],
        width=data["Width"],
        height=data["Height"],
    )


data = file_data("test.txt")
grid = data.create_grid()
# grid.display()
# grid.print_elem()
print("Global H matrix:")
h = grid.create_global_h_matrix(data.conductivity, True)
for i in range(16):
    for j in range(16):
        print("{:.3f}".format(h[i, j]), end=" ")
    print()
