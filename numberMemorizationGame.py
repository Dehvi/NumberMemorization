#!/usr/bin/env python
import random
import time
import sys

# Generates random numbers for memorization
def randomNumbers(amount):
    # generate x amount of random numbers
    list_for_nums = []
    for i in range(0,amount):
        ranum = random.randint(0,99)
        if ranum < 10:
            list_for_nums.append(str(ranum).zfill(2))
        else:
            list_for_nums.append(ranum)
    return list_for_nums

# Countdown timer
def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format, end="\r")
        time.sleep(1)
        num_of_secs -= 1
        
# Groups the number pairs on lines
def printGroupNumbers(num_list, group):
    x=0 # Counter for when it's time to change to a new line
    for num in num_list:
        if x < group:
            print(str(num) + ' ', end='')
            x = x+1
        elif x == group:
            print()
            x=0
    print("\n") # make some padding between number list and countdown counter

# compares two lists and returns the total amount of correct pairs
def compareLists(correct_list, user_list):
    correct_numbers = 0
    for correct, user_input in zip(correct_list, user_list):
        if user_input == str(correct):
            correct_numbers += 1
    return correct_numbers

def main():
    # input how many numbers to generate
    try:
        numbers_to_memorize = int(input("Enter amount of numbers to memorize: "))
        time_to_memorize = int(input("Time for memorization: "))
    except ValueError:
       print("Enter a valid number") 
       sys.exit()

    # start the counter
    print("\033c", end="") # clears the terminal screen
    time.sleep(0.5)
    print("Starting...\n")
    time.sleep(1)

    # Generate the random numbers and specify the amount of pairs on one line
    random_numbers = randomNumbers(int(numbers_to_memorize))
    printGroupNumbers(random_numbers, 9) # Default is 9 pairs of numbers on one line

    # countdown timer
    print(f"\n\nTimer: {countdown(time_to_memorize)}") # Default time for memorization is 60s
    print("\033c", end="") # clears the terminal screen

    # ask user to input the memorized list of numbers
    user_input = input("Enter the numbers in the order and separate them with space.\nEnter here: ")
    user_test = user_input.split()
    correct_answer = compareLists(random_numbers, user_test)

    print(f"\nYou got {correct_answer} pair(s) correct.\nHere is both lists for comparison.")
    print(f"Random numbers: {random_numbers}")
    print(f"Your input: {user_test}")

if __name__ == "__main__":
    main()
