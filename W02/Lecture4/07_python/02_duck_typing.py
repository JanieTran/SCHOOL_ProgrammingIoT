class Duck:
    def quack(self):
        print("Quack")


class Flock:
    def __init__(self, ducks):
        self.ducks = ducks

    def report(self):
        print("There are {} ducks in this flock.".format(len(self.ducks)))
        for duck in self.ducks:
            duck.quack()
        print()


flock = Flock([Duck(), Duck(), Duck()])
flock.report()


class Dog:
    def quack(self):
        print("BARK! BARK! BARK!")


flock = Flock([Duck(), Duck(), Dog(), Duck()])
flock.report()
