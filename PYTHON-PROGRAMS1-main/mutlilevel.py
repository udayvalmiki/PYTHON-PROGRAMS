
class animal:
    def animal_level_1_method():
        return "Im animal method"
class dog(animal):
    def dog_level_2_method():
        return "Im dog method, im inherited from class animal"
class puppy(dog):
    def puppy_level_3_method():
        return "Im puppy method, im inherited from class dog"
obj1=puppy
print(obj1.animal_level_1_method())
print(obj1.dog_level_2_method())
print(obj1.puppy_level_3_method())