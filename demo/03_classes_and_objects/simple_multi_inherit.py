
class Nose:
    def sniff(self, is_bad):
        if is_bad:
            print("Eugh!")
        else:
            print("Nice!")

class Legs:
    def walk(self):
        print("Walking...")

    def run(self, speed):
        print(f"Running at {speed} kp/h")


class Dog(Nose, Legs):
    pass


scooby = Dog()

scooby.sniff(False)
scooby.walk()
scooby.run(5)
