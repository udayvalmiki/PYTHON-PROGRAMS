# '''         1             
#         2   1   2
#     3   2   1   2   3
# 4   3   2   1   2   3   4
# # sum=1+5+11+19=36
# # '''

input_1=int(input())
result=input_1*1
num=2
for i in range(input_1-1,0,-1):
    result+=2*i*num
    num+=1
print(result)