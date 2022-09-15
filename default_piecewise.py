# y = x*k+b

class Dot():
    def __init__(self, coords: tuple) -> None:
        self.x = coords[0]
        self.y = coords[1]

class Section(Dot):
    def __init__(self, dot1:Dot, dot2:Dot) -> None:
        self.dot1 = dot1
        self.dot2 = dot2
        self.a = round((dot1.y - dot2.y) / (dot1.x - dot2.x), 2)
        self.b = round(-1 * (self.a * dot1.x - dot1.y), 2)

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
        self.dots = [dot1, dot2]

    def append_section(self, coords) -> None:
        dot = Dot(coords)
        if dot.x <= self.x_axios[0].dot1.x:
            section = Section(self.x_axios[0].dot1, dot)
        elif dot.x >= self.x_axios[-1].dot2.x:
            section = Section(self.x_axios[-1].dot2, dot) 
        else:
            raise Exception
        self.x_axios.append(section)
        self.dots.append(dot)

    def get_y(self, x: int) -> float:
        if x < self.x_axios[0].dot1.x or x > self.x_axios[-1].dot2.x:
            raise Exception
        for section in self.x_axios:
            if section.dot1.x <= x <= section.dot2.x:
                return x * section.a + section.b

    def __str__(self) -> str:
        max_x_length = len(str(self.x_axios[-1].dot2.x))
        max_a_length = len(str(max(self.x_axios, key=lambda item: len(str(item.a))).a))
        max_b_length = len(str(max(self.x_axios, key=lambda item: len(str(item.b))).b))
        emphasizing = f"{'-' * ((max_x_length+4)*2+max_a_length+max_b_length+5)}\n"
        string = f"| {' ' * int(max_x_length-2)}x1 | {' ' * int(max_x_length-2)}x2 "\
                 f"| {' ' * int(max_a_length-1)}a | {' ' * int(max_b_length-1)}b |\n"\
                 f"{emphasizing}"
        for section in self.x_axios:
            count_dot1_x_spaces = max_x_length-len(str(section.dot1.x))
            count_dot2_x_spaces = max_x_length-len(str(section.dot2.x))
            count_a_spaces = max_a_length-len(str(section.a))
            count_b_spaces = max_b_length-len(str(section.b))
            string += f"| {' ' * count_dot1_x_spaces}{section.dot1.x} | {' ' * count_dot2_x_spaces}{section.dot2.x} "\
                      f"| {' ' * count_a_spaces}{section.a} | {' ' * count_b_spaces}{section.b} |\n"\
                      f"{emphasizing}"
        return string


if __name__ == '__main__':
    a = Ordinate(((0, 100), (10, 122)))
    a.append_section((100, 1330))
    print(a.get_y(5))
    print(a.x_axios[1].a)
    print(a)

