class Element:
    def __init__(self, id_arr) -> None:
        self.id = id_arr

    def __repr__(self) -> str:

        res = ", ".join(str(item) for item in self.id)
        return res
