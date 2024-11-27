class Element:
    def __init__(self, id_arr) -> None:
        self.id = id_arr
        self.points = []

    def __repr__(self) -> str:
        res = ", ".join(str(item) for item in self.id)
        for point in self.points:
            res += f"\n{point}"
        return res
