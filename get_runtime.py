from typing import Optional
import random, threading, time

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

#########################################################################
#                             MAIN FUNCTION                             #
#########################################################################

if __name__ == '__main__':
    print("Running simulations and calculations...")

    # Characters that make up the passwords for case 4
    valid = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()[]+=.,<>-_"
    
    length = 3
    case = 4
    loops = 100
    
    # Runs the generation and cracking function at a user-defined number of times, then averages the guesses and time taken to complete
    average_iterations = 0
    average_time = 0
    for i in range(loops):
        password = generate_password(valid, length)
        run_count, run_time = crack_password(password, valid, length)
        average_iterations += run_count
        average_time += run_time
    avgitr = int(average_iterations/loops)
    avgtime = average_time/loops

    # Calculates the rate of the system's performance in terms of seconds per password guess generation and validation
    seconds_per_guess = avgtime/avgitr

    rows, cols = 4, 10
    computation_time = [[0 for j in range(cols)] for i in range(rows)]

    # Sorts password by proper order of magnitude for better intuitive interpretations of the data
    for i in range(rows):
        print()
        for j in range(cols):
            num_combonations = pow(len(valid),j+1)
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
            