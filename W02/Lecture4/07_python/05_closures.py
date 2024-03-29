# Reference: https://www.programiz.com/python-programming/closure
def make_multiplier_of(n):
    def multiplier(x):
        return x * n

    return multiplier


# Multiplier of 3.
times3 = make_multiplier_of(3)

# Multiplier of 5.
times5 = make_multiplier_of(5)

# Output: 27
print(times3(9))

# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))

print("---")

print(times3.__closure__[0].cell_contents)
print(times5.__closure__[0].cell_contents)
