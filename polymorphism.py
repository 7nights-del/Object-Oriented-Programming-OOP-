class Animal:
    def move(self):
        pass

class Dog(Animal):
    def move(self):
        return "The dog runs on four legs."

class Bird(Animal):
    def move(self):
        return "The bird flies in the sky."

class Fish(Animal):
    def move(self):
        return "The fish swims in the water."

# Demonstrate polymorphism
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    print(animal.move())
