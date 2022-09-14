# y = x*k+b

class Dot():
    def __init__(self, coords: tuple) -> None:
        self.x = coords[0]
        self.y = coords[1]

class Section(Dot):
    def __init__(self, dot1:Dot, dot2:Dot) -> None:
        self.dot1 = dot1
        self.dot2 = dot2
        self.k = (dot1.y - dot2.y) / (dot1.x - dot2.x)
        self.b = -1 * (self.k * dot1.x - dot1.y)

class Ordinate():
    def __init__(self, coords: tuple[tuple]) -> None:
        if coords[0][0] < coords[1][0]:
            dot1 = Dot(coords[0])
            dot2 = Dot(coords[1])
        else:
            dot1 = Dot(coords[1])
            dot2 = Dot(coords[0])

        section = Section(dot1, dot2)
        self.x_axios = [section]

    def append_section(self, coords):
        dot = Dot(coords)
        if dot.x <= self.x_axios[0].dot1.x:
            section = Section(self.x_axios[0].dot1, dot)
        elif dot.x >= self.x_axios[-1].dot2.x:
            section = Section(self.x_axios[-1].dot2, dot) 
        else:
            raise Exception       
        self.x_axios.append(section)

    def get_y(self, x: int):
        if x < self.x_axios[0].dot1.x or x > self.x_axios[-1].dot2.x:
            raise Exception
        for section in self.x_axios:
            if section.dot1.x <= x <= section.dot2.x:
                return x * section.k + section.b

    def __str__(self) -> str:
        string = ""
        for section in self.x_axios:
            string += f"| {section.dot1.x} | {section.dot2.x} |\n" 
        return string

a = Ordinate(((0, 100), (10, 122)))
a.append_section((20, 133))
print(a.get_y(5))
print(a.x_axios[1].k)
print(a)

