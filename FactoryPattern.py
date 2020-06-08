from random import randint


class Creator:
    def factory_method(self):
        pass

    def do_stuff(self):
        print('Doing stuff...')


class RandomCreator(Creator):
    def factory_method_creator(self):
        rand_num = randint(0, 1)
        if rand_num == 0:
            detector = FakeDetector()
        else:
            detector = MegaDetector()
        return detector


class DeterministicCreator(Creator):
    def factory_method_creator(self, choice):
        if choice == 0:
            detector = FakeDetector()
        else:
            detector = MegaDetector()
        return detector


class Detector:
    def __init__(self, x1, x2, size, can_work):
        self.x1 = x1
        self.x2 = x2
        self.size = size
        self.can_work = can_work

    def change_location(self, in_x1, in_x2):
        self.x1 += in_x1
        self.x2 += in_x2


class FakeDetector(Detector):
    def __init__(self):
        super().__init__(randint(-100, 100), randint(-100, 100), 10, False)


class MegaDetector(Detector):
    def __init__(self):
        super().__init__(randint(-100, 100), randint(-100, 100), 100, True)
