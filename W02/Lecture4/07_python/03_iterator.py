class Factorial():
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        self.total = 1
        self.previous = 1
        return self

    def __next__(self):
        if self.previous > self.value:
            raise StopIteration

        self.total *= self.previous
        self.previous += 1

        return self.total


fiveFactorial = Factorial(5)

for value in fiveFactorial:
    print(value)

print("---")

try:
    iterator = iter(fiveFactorial)
    while True:
        value = next(iterator)
        print(value)
except StopIteration:
    pass
