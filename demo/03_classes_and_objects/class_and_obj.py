
class Vehicle:
    def __init__(self, max_speed):
        self.max_speed = max_speed
        self.speed = 0

    def set_speed(self, speed):
        if speed > self.max_speed:
            raise ValueError("We're going too fast!")
        else:
            self.speed = speed

    def get_speed(self):
        if self.speed == 0:
            print("Stationary")
        else:
            print(f"Travelling at {self.speed} kph")


class Bike(Vehicle):
    def __init__(self, max_speed):
        super().__init__(max_speed)

    def ring_bell(self):
        print("Ring! Ring!")


class Car(Vehicle):
    def __init__(self, locked):
        super().__init__(70)
        self.locked = bool(locked)

    def set_lock(self, locked):
        self.locked = bool(locked)

    def enter(self):
        if self.locked:
            print("ALARM!")
        else:
            print("Welcome in")


b = Bike(20)
b.get_speed()
b.set_speed(10)
b.ring_bell()
b.get_speed()

try:
    b.set_speed(30)
except ValueError as exc:
    print(exc)


c = Car(True)
c.enter()

c.set_lock(False)
c.enter()
c.set_speed(50)
c.get_speed()
