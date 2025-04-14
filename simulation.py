from typing import Optional
import random, threading

rows, cols = 4, 20
results = [[0 for i in range(cols)] for j in range(rows)]

def generate_password(chars: str, length):
    password = ''
    for i in range(length):
        rand_char = chars[random.randint(0, len(chars)-1)]
        password += rand_char

    return password

def crack_password(actual_password: str, valid_chars: str, length: int) -> Optional[str]:
    iterations = 0
    guess = list()
    len_char_ind = len(valid_chars)-1
    final_char = valid_chars[len_char_ind]
    for i in range(length):
        guess.append('a')

    while("".join(guess) != actual_password):
        iterations += 1

        if guess[0] == final_char:
            guess[0] = 'a'
            for i in range(1, length):
                if (guess[i] == final_char):
                    guess[i] = 'a'
                    continue
                else:
                    guess[i] = valid_chars[valid_chars.index(guess[i])+1]
                    break
        else:
            guess[0] = valid_chars[valid_chars.index(guess[0])+1]
        
    return "".join(guess), iterations

def get_valid_chars(case):
    valchar = "abcdefghijklmnopqrstuvwxyz"

    if (case >= 2):
        valchar += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if (case >= 3):
        valchar += "0123456789"

    if (case >= 4):
        valchar += "!@#$%^&*()[]+=.,<>-_"

    return valchar

def run_test(length, case):
    valid = get_valid_chars(case)
    password = generate_password(valid, length)
    pw, count = crack_password(password, valid, length)

    return count

def run_loop(length, case, loops):
    average_iterations = 0
    for i in range(loops):
        average_iterations += run_test(length, case)
    average_iterations = int(average_iterations/loops)

    results[case-1][length-1] = average_iterations

    return

def run_case(min_length, max_length, case, loops):
    for i in range(max_length-min_length+1):
        run_loop(min_length+i, case, loops)
    
    return

def run_sim(min, max, loops):
    threads = []
    for i in range(4):
        thread = threading.Thread(target=run_case, args=(min, max, i+1, loops))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    for i in range(4):
        print("")
        print("------------------------------ CASE", i+1, "------------------------------")
        for j in range(max-min+1):   
            print("Average iterations for password case", i+1, "at length", j+1,"over", loops, "loops:", results[i][j])

    print("")

#########################################################################
#                             MAIN FUNCTION                             #
#########################################################################

# Password Cases:
# 1 - Lowercase
# 2 - Lowercase + Uppercase
# 3 - Lowercase + Uppercase + Numbers
# 4 - Lowercase + Uppercase + Numbers + Special

if __name__ == '__main__':
    min = 1
    max = 3
    loops = 10

    run_sim(min, max, loops)