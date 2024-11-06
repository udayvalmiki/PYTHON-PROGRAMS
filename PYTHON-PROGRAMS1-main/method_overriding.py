class Animal:
    def speak():
        return "Animal is speaking"
class Dog(Animal):
    def speak():
        return "Dog is barking"
class Cat(Animal):
    def speak():
        return "Meow"
animal=Animal
dog=Dog
cat=Cat

print(animal.speak())
print(dog.speak())
print(cat.speak())