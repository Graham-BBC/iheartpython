
def generate_multiplier(multiple):
    return lambda n: n * multiple


doubler = generate_multiplier(2)
tripler = generate_multiplier(3)
halfer = generate_multiplier(0.5)

print(doubler(10))
print(tripler(10))
print(halfer(10))

square = lambda x: x ** 2
square(5)  # should be 25
