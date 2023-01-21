import random
import database

def run_training(user):
    correct_count = 0
    for i in range(10):
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        result = num1 * num2
        answer = int(input(f"{num1} x {num2} = "))
        if answer == result:
            print("Correct!")
            correct_count += 1
        else:
            print("Incorrect.")
    print(f"{user}, you got {correct_count} out of 10 correct.")
    database.update_user(user, correct_count)
