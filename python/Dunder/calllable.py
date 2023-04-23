class A:
    def __init__(self, x):
        self.y = x

    def __call__(self):
        return self.y
    




a = A(10)
print(a.y)
print(a())