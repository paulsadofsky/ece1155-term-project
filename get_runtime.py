from typing import Optional
import random, threading, time

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

    return average_iterations, average_time

#########################################################################
#                             MAIN FUNCTION                             #
#########################################################################

# Password Cases:
# 1 - Lowercase
# 2 - Lowercase + Uppercase
# 3 - Lowercase + Uppercase + Numbers
# 4 - Lowercase + Uppercase + Numbers + Special

if __name__ == '__main__':
    print("Running simulations and calculations...")
    avgitr, avgtime = run_loop(length=3, case=4, loops=100)
    seconds_per_guess = avgtime/avgitr

    rows, cols = 4, 10
    computation_time = [[0 for j in range(cols)] for i in range(rows)]

    for i in range(rows):
        print()
        for j in range(cols):
            num_combonations = pow(len(get_valid_chars(i+1)),j+1)
            avg_time_for_sim = ((num_combonations*seconds_per_guess)/2)*1000000
            print_statement = "Average time to crack a single case " + str(i+1) + " password at length " + str(j+1) + ":\t"

            # Microseconds
            if (avg_time_for_sim < 1000):
                print(print_statement, avg_time_for_sim, "microseconds")
                continue
            
            # Milliseconds
            avg_time_for_sim /= 1000
            if (avg_time_for_sim < 1000):
                print(print_statement, avg_time_for_sim, "milliseconds")
                continue

            # Seconds
            avg_time_for_sim /= 1000
            if (avg_time_for_sim < 60):
                print(print_statement, avg_time_for_sim, "seconds")
                continue
            
            # Minutes
            avg_time_for_sim /= 60
            if (avg_time_for_sim < 60):
                print(print_statement, avg_time_for_sim, "minutes")
                continue

            # Hours
            avg_time_for_sim /= 60
            if (avg_time_for_sim < 24):
                print(print_statement, avg_time_for_sim, "hours")
                continue

            # Days
            avg_time_for_sim /= 24
            if (avg_time_for_sim < 365):
                print(print_statement, avg_time_for_sim, "days")
                continue

            # Years
            avg_time_for_sim /= 365
            if (avg_time_for_sim < 10):
                print(print_statement, avg_time_for_sim, "years")
                continue

            # Decades
            avg_time_for_sim /= 10
            if (avg_time_for_sim < 10):
                print(print_statement, avg_time_for_sim, "decades")
                continue

            # Centuries
            avg_time_for_sim /= 10
            print(print_statement, avg_time_for_sim, "centuries")
            continue
            