from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat
    def display(self):
        print(f"Name: {self.name}")
        print(f"Habitat: {self.habitat}")
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def __init__(self, name, habitat, breed):
        super().__init__(name, habitat)
        self.breed = breed
    def make_sound(self):
        return "Woof!"
class Parrot(Animal):
    def __init__(self, name, habitat, phrase):
        super().__init__(name, habitat)
        self.phrase = phrase
    def make_sound(self):
        return "Squawk!"
class Lion(Animal):
    def __init__(self, name, habitat, pride):
        super().__init__(name, habitat)
        self.pride = pride
    def make_sound(self):
        return "Roar!"
dog = Dog("Buddy", "Domestic", "Golden Retriever")
parrot = Parrot("Polly", "Tropical Rainforest", "Squawk!")
lion = Lion("Simba", "Savannah", "Pride of Lions")
print("=== Animal Sounds ===")
for animal in [dog, parrot, lion]:
    animal.display()
    animal_sound = animal.make_sound()
    print()