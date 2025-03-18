import random

# lower case = 97-122
# upper case = 65-90
# numbers = 48-57
# special characters = 33, 35, 36, 37, 38, 42, 60, 62, 63, 64, 94, 95

def main():
    password_length = 200
    password = ""

    userinput = ""
    while (userinput != "5"):
        password = ""
        print("MENU OPTIONS:\n",
              "1 - Lowercase\n",
              "2 - Lowercase + Uppercase\n",
              "3 - Lowercase + Uppercase + Numbers\n",
              "4 - Lowercase + Uppercase + Numbers + Special\n",
              "5 - Exit\n")
        userinput = input("Enter an option: ")
    
        if (userinput == '1'):
            upper_bound = 122
            lower_bound = 97

            for i in range(password_length):
                rand_char = random.randint(lower_bound, upper_bound)
                password += chr(rand_char)

        elif (userinput == '2'):
            upper_bound = 122
            lower_bound = 65

            for i in range(password_length):
                rand_char = random.randint(lower_bound, upper_bound)
                while (rand_char <= 96 and rand_char >= 91):
                    rand_char = random.randint(lower_bound, upper_bound)
                password += chr(rand_char)
        
        elif (userinput == '3'):
            upper_bound = 122
            lower_bound = 48

            for i in range(password_length):
                rand_char = random.randint(lower_bound, upper_bound)
                while ((rand_char <= 96 and rand_char >= 91) or (rand_char <= 64 and rand_char >= 58)):
                    rand_char = random.randint(lower_bound, upper_bound)
                password += chr(rand_char)

        elif (userinput == '4'):
            excluded = [34, 39, 44, 46, 47, 58, 59, 92, 96]
            upper_bound = 122
            lower_bound = 33

            for i in range(password_length):
                rand_char = random.randint(lower_bound, upper_bound)
                while (rand_char in excluded):
                    rand_char = random.randint(lower_bound, upper_bound)
                password += chr(rand_char)

        elif (userinput == '5'):
            break

        else:
            print("INVALID INPUT\n")
            continue

        print("PASSWORD: " + password, "\n")

    return

main()
