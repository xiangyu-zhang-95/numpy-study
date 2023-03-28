class Even:
    def __init__(self):
        self.vv = -2

class Odd:
    def __init__(self):
        self.vv = -1

class A:
    def __new__(cls, x):
        if isinstance(x, int):
           residual = x % 2
           if residual == 0:
               return super().__new__(Even)
           else:
                return super().__new__(Odd)
        raise Exception("x should be an int")
    
    def __init__(self, x):
        print("here", self)
        type(self).__init__(self)
        self.v = x

a = A(12)
# print(f"type(a): {type(a)}, a.vv = {a.vv}")

# b = A(11)
# print(f"type(b): {type(b)}, b.vv = {b.vv}" )
