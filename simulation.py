from typing import Optional
import random, threading, time

# Initializes arrays to store simulation results into
rows, cols = 4, 20
results = [[0 for i in range(cols)] for j in range(rows)]
results_time = [[0 for i in range(cols)] for j in range(rows)]

def generate_password(chars: str, length):
    password = ''
    for i in range(length):
        # Generates a random character from list of random characters based off of length
        rand_char = chars[random.randint(0, len(chars)-1)]
        password += rand_char

    return password

def crack_password(actual_password: str, valid_chars: str, length: int) -> Optional[str]:
    iterations = 0
    len_valid = len(valid_chars)
    guess_indices = []
    target_indices = []

    # Breaks the actual password into a list of indices from the valid_chars string
    # Uses this to generate "guess_indices" until all indices match
    for i in range(length):
        guess_indices.append(0)
        target_indices.append(valid_chars.index(actual_password[i]))

    start_time = time.time()
    # Loop until guess is correct
    while(guess_indices != target_indices):
        # Increment counter for number of guess the attack has taken
        iterations += 1

        # If the lowest indices has reached its maximum value, it should reset to 0 and the next index should increment
        index = 0
        while index < length:
            guess_indices[index] += 1
            if guess_indices[index] < len_valid:
                break
            guess_indices[index] = 0
            index += 1

    end_time = time.time()
    execution_time = end_time - start_time
    
    # Exiting the while loop signifies that the password has been cracked
    return iterations, execution_time

# Returns the characters that make up the passwords at each case
def get_valid_chars(case):
    # Base Case (1)
    valchar = "abcdefghijklmnopqrstuvwxyz"

    if (case >= 2):
        # Case 2
        valchar += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if (case >= 3):
        # Case 3
        valchar += "0123456789"

    if (case >= 4):
        # Case 4
        valchar += "!@#$%^&*()[]+=.,<>-_"

    return valchar

# Wrapper function to run a single password generation and crack
def run_test(length, case):
    valid = get_valid_chars(case)
    password = generate_password(valid, length)
    count, time = crack_password(password, valid, length)

    return count, time

# Runs the generation and cracking function at a user-defined number of times, then averages the guesses and time taken to complete
def run_loop(length, case, loops, min_length):
    average_iterations = 0
    average_time = 0
    for i in range(loops):
        run_count, run_time = run_test(length, case)
        average_iterations += run_count
        average_time += run_time
    average_iterations = int(average_iterations/loops)
    average_time = average_time/loops

    results[case-1][length-min_length] = average_iterations
    results_time[case-1][length-min_length] = average_time

    return

# Runs loop function for a specified password case from a minimum length to a maximum length
def run_case(min_length, max_length, case, loops):
    for i in range(max_length-min_length+1):
        run_loop(min_length+i, case, loops, min_length)
    
    return

# Multi-threds teh execution of the run_case function across the four cases to decrease simulation runtime
def run_sim(min, max, loops):
    threads = []
    for i in range(4):
        thread = threading.Thread(target=run_case, args=(min, max, i+1, loops))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Print results to terminal
    for i in range(4):
        print("")
        print("------------------------------ CASE", i+1, "------------------------------")
        for j in range(max-min+1):   
            print("Average iterations for password case", i+1, "at length", j+min,"over", loops, "loops:", results[i][j],"(",results_time[i][j],"seconds )")

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
    loops = 100

    # Calculates the average number of guesses and time taken to crack a password over a specified number of runs between a minimum and maximum password length
    # Results are outputted to the terminal
    run_sim(min, max, loops)