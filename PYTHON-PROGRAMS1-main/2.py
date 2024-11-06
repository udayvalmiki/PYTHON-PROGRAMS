# n=int(input("Number"))
# t=magic(n) 
# if t>9:
#     t1=magic(t)
#     print(t1)
# else:
#     print(t)/

# 1.positional argument
# def sumOfNumbers(a,b):
#     print(a)
#     print(b)
#     return a+b
# c=sumOfNumbers(18,20)
# print(c)

# 2. default argument

# def myself(name,age=24):
#     print(name)
#     print(age)
#     return None
# myself("Sri",age=24)


# 3.Keyword argument
# def goodmorning(name,age):
#     print(name)
#     print(age)


# my_list=[1,2,3,4]
# print(my_list)

# my_list.append(5)
# print(my_list)

# my_list.remove(5)
# print(my_list)

# my_list.extend([6,7,8])
# print(my_list)

# my_list.clear()
# print(my_list)

# my_list.copy()
# print(my_list)

# my_list.insert(7,11)
# print(my_list)

# my_list.pop()
# print(my_list)

# my_list.count()
# print(my_list)



# def evenOdd(n):
#     if(n%2==0):
#         print("Even")
#     else:
#         print("Odd")
# c=evenOdd(7)

#-------------------LISTs----------------------------------------

# input_list=input("Enter the numbers separated by spaces:")
# numbers=list(map(int,input_list.split()))
# print(input_list)

# numbers.insert(4,11)
# print(numbers)

# numbers.append(7)
# print(numbers)

# numbers.remove(3)
# print(numbers)

# numbers.copy()
# print(numbers)

# numbers.clear()
# print(numbers)

# numbers.extend([8,9,10])
# print(numbers)

# numbers.pop(2)
# print(numbers)

# numbers.reverse()
# print(numbers)

# numbers.copy()
# print(numbers)


#------------------------------TUPLES-------------------------------------

# my_tuple=(1,2,3,4,5)

# index=my_tuple.index(4)
# print("Index of 3:",index)

# count=my_tuple.count(5)
# print("count of :",count)

# my_set={1, 2, 3, 4, 5}
 
# my_set.add(6)
# print("After add(6):",my_set)

# my_set.update({7,8})
# print("After update{7,8}:",my_set)

# my_set.remove(4)
# print("After remove(4):",my_set)

# my_set.pop()
# print("After pop():",my_set)

# my_set.discard(5)
# print("After discard(5):",my_set)

# my_set.copy()
# print("After copy:",my_set)

# s1={1,2,3,4}
# s2={5,6,7,8}

# s=s1.union(s2)
# print("After union:",s)

# i=s1.intersection(s2)
# print("After intersection:",i)

# c=s1.difference(s2)
# print("After Difference:",c)

# d=s1.symmetric_difference(s2)
# print("After Symmetric difference:",d)

# b=s1.isdisjoint(s2)
# print("After Disjoint:",b)

# my_dict=dict()
# my_dict=dict(one=1,two=2,three=3)
# print(my_dict)

# my_dict_new={'one':1,'two':2,'three':3}

# print(my_dict_new)

# my_dict_new.clear()

# keys=['one','two','three']
# values=0

# my_dict_new_2=dict.fromkeys(keys,values)
# print(my_dict_new_2)

# my_dict_new_3={'one':1,'two':2,'three':3}
# print(my_dict_new_3.get('one'))

# class operations:
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
# obj1=operations
# print(obj1.add(3,6))
# print(obj1.sub(3,4))
# print(obj1.mul(3,2))
# print(obj1.div(6,3))


# class animal:
#     def __init__(self,name):
#         self.name=name
#     def greet():
#         return "hey!!"
# class dog(animal):
#     def speck():
#         return "bark..."
# obj1=dog
# print(obj1.speck())

# class Father:
#     def father_method():
#         return "im his father"
# class Mother:
#     def mother_method():
#         return "im his  mother"
# class Kid(Father,Mother):
#     def kid_method():
#         return "im kid"
# obj2=Kid
# print(obj2.father_method())
# print(obj2.mother_method())
# print(obj2.kid_method())

# multi level

class mamals:
    def speak():
        return "we are all animals"
class dog(mamals):
    def about():
        return "im dog"
    
class puppy(dog):
    def who():
        return "im puppy"
ob=puppy
print(ob.about())
print(ob.speak())