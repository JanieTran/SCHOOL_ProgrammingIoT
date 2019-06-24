class Factorial():
    def __init__(self, value):
        self.value = value

    def values(self):
        total = 1
        previous = 1
        while previous <= self.value:
            total *= previous
            previous += 1
            yield total


fiveFactorial = Factorial(5)

for value in fiveFactorial.values():
    print(value)
