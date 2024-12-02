class Student:
    def marks(self, a, b, c=0):
        ttl = a + b + c

        return ttl
mk1 = Student()
print(mk1.marks(67, 89))
print(mk1.marks(87,88,92))