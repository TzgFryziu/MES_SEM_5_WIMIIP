class Grid:
    def __init__(self, nodes_number, elements_number, elem_arr, node_arr) -> None:
        self.nodes_number = nodes_number
        self.elements_number = elements_number
        self.elem_arr = elem_arr
        self.node_arr = node_arr

    def display(self) -> str:

        print("*Node")
        for i in range(len(self.node_arr)):
            print(f"   {i+1}. {self.node_arr[i]}")

        print("\n*Element")
        for i in range(len(self.elem_arr)):
            print(f"   {i+1}. {self.elem_arr[i]}")
