class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.fins = 4
    
    # modify the parent's function
    def breathe(self):
        super().breathe()
        print("Doing this underwater")

    def swim(self):
        print("Moving in water")

nemo = Fish()
print(nemo.num_eyes)
nemo.breathe()