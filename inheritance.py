class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale and Exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Under water")

    def swim(self):
        print("Move in water")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
