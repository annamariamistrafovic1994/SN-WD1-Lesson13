from gtnfunctions import play_game(), get_score_list(), get_top_scores()

import datetime
import json
import random

secret = random.randint(1, 50)
attempts = 0

with open("score_list1.txt", "r") as score_file:
    score_list1 = json.loads(score_file.read())

print("Top scores: " + str(score_list1))

for score_dict in score_list1:
    print(str(score_dict["attempts"]) + "attempts, date: " + score_dict.get("date"))

while True:
    guess = int(input("Guess the secret number between 1 and 50: "))
    attempts += 1

    if guess == secret:
        score_list1.append({"attempts": attempts, "date": str(datetime.datetime.now())})
        with open("score_list1.txt", "w") as score_file:
            score_list1.write(json.dumps(score_list1))

        print("You've guessed it! Congrats! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break

    elif guess > secret:
        print("Your guess is not correct...try something smaller")
        print(attempts)

    elif guess < secret:
        print("Your guess is not correct...try something bigger")
        print(attempts)



