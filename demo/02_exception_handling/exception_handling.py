
class FiveException(Exception):
    pass

def print_non_five_number(num):
    if num == 5:
        raise FiveException("Sorry, that was 5")
    else:
        print(f"Number {num}")

numbers = [1, 2, 5, 7]

for num in numbers:
    try:
        print_non_five_number(num)
    except FiveException as exc:
        print(f"{exc}")
