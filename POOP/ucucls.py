class Ucu:
    e_platform = 'alpha'
    def __init__(self, address):
        self.address = address

    @classmethod
    def myuni(cls):
        return cls.e_platform

print(Ucu.e_platform)
