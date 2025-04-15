from typing import Optional
import random, threading, time

rows, cols = 4, 20
results = [[0 for i in range(cols)] for j in range(rows)]
results_time = [[0 for i in range(cols)] for j in range(rows)]

def generate_password(chars: str, length):
    password = ''
    for i in range(length):
        rand_char = chars[random.randint(0, len(chars)-1)]
        password += rand_char

    return password

def crack_password(actual_password: str, valid_chars: str, length: int) -> Optional[str]:
    iterations = 0
    len_valid = len(valid_chars)
    guess_indices = []
    target_indices = []
    for i in range(length):
        guess_indices.append(0)
        target_indices.append(valid_chars.index(actual_password[i]))

    start_time = time.time()
    while(guess_indices != target_indices):
        iterations += 1

        index = 0
        while index < length:
            guess_indices[index] += 1
            if guess_indices[index] < len_valid:
                break
            guess_indices[index] = 0
            index += 1

    end_time = time.time()
    execution_time = end_time - start_time
    
    return iterations, execution_time

from typing import Optional


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
    count, time = crack_password(password, valid, length)

    return count, time

def run_loop(length, case, loops):
    average_iterations = 0
    average_time = 0
    for i in range(loops):
        run_count, run_time = run_test(length, case)
        average_iterations += run_count
        average_time += run_time
    average_iterations = int(average_iterations/loops)
    average_time = average_time/loops

    results[case-1][length-1] = average_iterations
    results_time[case-1][length-1] = average_time

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
            print("Average iterations for password case", i+1, "at length", j+1,"over", loops, "loops:", results[i][j],"(",results_time[i][j],"seconds )")

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
    max = 5
    loops = 1

    run_sim(min, max, loops)
