
fruits = [
    "cherry",
    "apple",
    "banana",
    "avocado",
    "berry",
    "coconut"
]

first_letters = set([l[0] for l in fruits])


def starts_with(letter):
    return lambda s: s.startswith(letter)


groups = {l: list(filter(starts_with(l), fruits)) for l in first_letters}

print(groups)
