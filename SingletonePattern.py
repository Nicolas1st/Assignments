class Singleton(type):

    instance = None

    def __call__(cls, x1, x2):
        if cls.instance is None:

            cls.instance = super().__call__(x1, x2)
        return cls.instance


class Detector(metaclass=Singleton):
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2


a = Detector(1, 2)
b = Detector(3, 4)
print(b.x1)
b.x1 = 10
print(a.x1)
print(a is b)
