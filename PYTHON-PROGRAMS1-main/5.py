# import re

# def check_password(password):
#     # At least 4 characters, at least one numeric digit, at least one capital letter
#     # Must not have space or slash (/), starting character must not be a number
#     if (len(password) >= 4 and
#         re.search(r"[A-Z]", password) and
#         re.search(r"[0-9]", password) and
#         not re.search(r"[\s/]", password) and
#         not password[0].isdigit()):
#         return 1
#     else:
#         return 0

# # Example usage:
# print(check_password('aA1_67'))  # Output: 1
# print(check_password('a987 abC012'))  # Output: 0


s = input()
list = ['a','e','i','o','u']
count = 0
for i in s:
    if i in list:
        count += 1
print(count)