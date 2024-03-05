
items = [
    None,
    True,
    False,
    0,
    1,
    -1,
    0.0,
    0.1234,
    [],
    ["non-empty list"],
    {},
    {"none": "empty dict"},
    object()
]

for item in items:
    if item:
        print(f"{item} is TRUE")
    else:
        print(f"{item} is FALSE")
