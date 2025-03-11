import random

# lower case = 97-122
# upper case = 65-90
# numbers = 48-57
# special characters = 33, 35, 36, 37, 38, 42, 60, 62, 63, 64, 94, 95

excluded = [34, 39, 40, 41, 43, 44, 45, 46, 47, 58, 59, 61, 91, 92, 93, 96]
upper_bound = 122
lower_bound = 33
password = ""
password_length = 10

for i in range(password_length):
    rand_char = random.randint(lower_bound, upper_bound)
    while (rand_char in excluded):
        rand_char = random.randint(lower_bound, upper_bound)
    password += chr(rand_char)

print("PASSWORD: " + password)

