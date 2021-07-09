class add(int):
    def __call__(self, n):
        print("call", self)
        return add(self + n)
print(add(1),2)
print(add(1)(2))