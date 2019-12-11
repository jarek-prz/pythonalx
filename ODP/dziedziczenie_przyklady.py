class Animal:
    def __init__(self, name):
        self.name=name
        self.energy = 100

    @property
    def is_alive(self):
        return self.energy>0

    def move(self, distance):
        self.energy -= 0.1*distance
        if self.is_alive:
            return distance
        else:
            return self.is_alive

    def eat(self, calories):
        self.energy+=0.2*calories

    def make_noise(self):
        print("Making noise")


# klasa Dog dziedziczy po klasie Animal
# czyli ma co najmniej wszystkie te metody i properties, co klasa Animal
class Dog(Animal):
    def __init(self, name, species):
        super().__init__(name)
        self.species = species


    def bark(self):
        super().make_noise()
        print("How how")
        self.energy-=0.1

a=Animal("Zenek")
print(a.move(5000))

azor = Dog("Azor")
print(azor.bark())

