# for i in range(0,11):
#     print(i,end=" ")

# sum=0
# for i in range (1,11):
#     sum=sum+i
#     print(sum)

# age=19
# if (age>18):
#     print("Age greater than 18")
# elif(age==18):
#     print("age is 18")
# else:
#     print("Age=18")

# a=10
# if(a%2 == 0):
#     print("Even")
# else:
#     print("odd")


# n=int(input())
# for i in range(1,n+1):
#     if i%2==0:
#         print(i,"Even")
#     else:
#         print(i,"Odd")

# c=0
# for i in range(1850,2025):
#     if i%4==0 and i%100!=0 or i%400==0:
#         c+=1
# print(c)

# n=int(input())
# flag=True
# for i in range(2,n//2):
#     if (n%i==0):
#         flag=False
# if flag:
#     print("Prime")
# else:
#     print("NOt Prime")

# n=int(input("Number is:"))
# s=0
# N=n
# while N>0:
#     r=N%10
#     s+=r*r*r
#     N=N//10
# if s==n:
#     print("it is armstrong")
# else:
#     print("Not an armstrong")

# Magic Number
# def magic(n):
#     s=0
#     while n>0:
#         r=n%10
#         s+=r
#         n//=10
#     return s

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
