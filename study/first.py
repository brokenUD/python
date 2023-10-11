class a:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
    def add(self):
        print(self.a+self.b)

cc = a(3,4)
cc.add()

