

class A:
    def __init__(self, i):
        self.i = i

    def __gt__(self, other):
        return self.i > other.i

a1 = A(1)
a2 = A(2)

r = max([a1, a2])
print(r.i)

