import random
import time
import database

def run_test(user):
    score = 0
    start_time = time.time()
    while time.time() - start_time < 480:
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        result = num1 * num2
        answer = int(input(f"{num1} x {num2} = "))
        if answer == result:
            score += 1
    print(f"{user}, you got {score} points.")
    database.update_user(user, score)
    if score > database.get_highscore():
        print("Congratulations, you beat your previous record!")
