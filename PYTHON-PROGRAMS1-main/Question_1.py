'''There is a ant on your balcony. It wants to leave the rail so sometimes it moves
right and sometimes it moves left until it gets exhausted. Given an integer array A of size N
which consists of integer 1 and -1 only representing ant's moves.
where 1 means ant moved unit distance towards the right side and -1 menas it moved unit idstance towards the left.
Your tsak is to find and return the integer value representing how many times the ant reaches back to original starting position.
Note:
* Assume 1-based indexing
* Assume that the railing extends infinitely on the either sides
Input format:
input1: An integer value N representing the number of moves made by the ant
input2: An integer array A consisting of the ant's moves towards either side'''

# def count_returns_to_origin(N, A):
#     position = 0
#     return_count = 0
#     for move in A:
#         position += move
#         if position == 0:
#             return_count += 1
#     return return_count

# # Example usage:
# N = 7
# A = [1, -1, 1, -1, 1, -1, 1]
# print(count_returns_to_origin(N, A))  # Output: 3


n=int(input())
arr=list(map(int,input().split()))
count=0
for i in range(n):
    if(sum(arr[:i+1])==0):
        count=count+1
print(count)
