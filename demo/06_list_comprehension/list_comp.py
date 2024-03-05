
fruits = [
    "apple",
    "banana",
    "coconut",
    "durian",
    "elderberry",
    "fig",
    "grape",
    "honeydew"
]

listcomp = [f.upper() for f in fruits if 'a' in f]

print(listcomp)
