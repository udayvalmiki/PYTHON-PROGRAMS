# def check_even_odd(n):
#     for i in range(1, n + 1):
#         if i % 2 == 0:
#             print(i, "Even")
#         else:
#             print(i, "Odd")

# n = int(input("Enter a number: "))
# check_even_odd(n)

# def sum(n):
#     total=0
#     for i in range (1,n+1):
#         total=total+i
#     return total
# n=int(input())
# print(sum(n))

# number = int(input())
# num_str = str(number)
# if num_str == num_str[::-1]:
#     print(f"{number} is a palindromic number.")
# else:
#     print(f"{number} is not a palindromic number.")

# Single Inheritance
# class Calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(a,b):
#         return a+b
#     def sub(a,b):
#         return a-b
#     def mul(a,b):
#         return a*b
#     def div(a,b):
#         return a/b
# obj1=Calculator
# print(obj1.add(3,6))
# print(obj1.sub(3,4))
# print(obj1.mul(3,2))
# print(obj1.div(6,3))

# class animal:
#     def animal_level_1_method():
#         return "Im animal method"
# class dog(animal):
#     def dog_level_2_method():
#         return "Im dog method, im inherited from class animal"
# class puppy(dog):
#     def puppy_level_3_method():
#         return "Im puppy method, im inherited from class dog"
# obj1=puppy
# print(obj1.animal_level_1_method())
# print(obj1.dog_level_2_method())
# print(obj1.puppy_level_3_method())

# odd or even
# n=int(input())
# for i in range(1,n+1):
#     if i%2==0:
#         print(i,"Even")
#     else:
#         print(i,"Odd")


# Sum of digits
# def sumOfNumbers(a,b):
#     return a+b
# c=sumOfNumbers(18,20)
# print(c)
