class MultipyClass:

    def __init__(self) -> None:
        self.a = 0
        self.b = 0
        print(self.a, self.b)


    def multiply(self, c, d):
        self.a = c
        self.b = d
        return self.a * self.b