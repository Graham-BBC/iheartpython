
from time import sleep

counter = 3

while counter > 0:
    try:
        sleep(1)
        print(f"still sleeping ({counter})")
    except:
        counter -= 1
