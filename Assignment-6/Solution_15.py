
class A:
    def show(self):
        print("Show method from class A")

class B(A):
    def show(self):
        print("Show method from class B")

class C(A):
    def show(self):
        print("Show method from class C")

class D(B, C):
    pass

d = D()
d.show()

print(D.__mro__)