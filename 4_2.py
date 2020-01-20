class Polynom:
    def __init__(self, *args):
        self.kaef = []
        for arg in args:
            self.kaef.append(arg)

    def __len__(self):
        return len(self.kaef)

    def __repr__(self):
        _len = len(self.kaef)
        result = " + ".join(["{}x^{}".format(x, _len-i-1) for i, x in enumerate(self.kaef)])
        return result.replace("x^0", "")

    def __add__(self, right_polynom):
        kaef_left = self.kaef[::-1].copy()
        kaef_right = right_polynom.kaef[::-1].copy()

        if len(kaef_left) > len(kaef_right):
            kaef_result = kaef_left
        else:
            kaef_result = kaef_right

        for i, (a, b) in enumerate(zip(kaef_left, kaef_right)):
            kaef_result[i] = a+b
        kaef_result = kaef_result[::-1]

        return Polynom(*kaef_result)

    def _negative(self):
        return Polynom(*[-x for x in self.kaef])

    def __sub__(self, right_polynom):
        return self.__add__(right_polynom._negative())

    def __mul__(self, right_polynom):
        kaef_left = self.kaef[::-1].copy()
        kaef_right = right_polynom.kaef[::-1].copy()

        kaef_result = [0]*(len(kaef_right)+len(kaef_left)-1)

        for i, a in enumerate(kaef_left):
            for j, b in enumerate(kaef_right):
                kaef_result[i+j] += a*b
        kaef_result = kaef_result[::-1]

        return Polynom(*kaef_result)


x = Polynom(1, 2, 3)
y = Polynom(3, 2, 1)
print(x)
print(y)
print(len(x), ', ', len(y))
print(x+y)
print(x-y)
print(x*y)
