class Even:
    def __init__(self):
        self.vv = -2

class A:
    def __new__(cls, x):
        print("inside __new__")
        return super().__new__(Even)
    
    def __init__(self, x):
        print("inside __init__")
        type(self).__init__(self)
        self.v = x
        return "hey"

a = A(12)
print(f"type(a): {type(a)}, a.v = {a.v}, a.vv = {a.vv}")

# b = A(11)
# print(f"type(b): {type(b)}, b.vv = {b.vv}" )
print(Even().vv)