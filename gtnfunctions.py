def play_game():
    while True:
        selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")

        if selection == "A":
            play_game()
        elif selection == "B":
            for score_dict in get_top_scores():
                print(str(score_dict["attempts"]) + "attempts, date: " + score_dict.get("date"))
        else:
            break


def get_score_list1():
    with open("score_list1", "r") as score_file:
        score_list1 = json.loads(score_file.read())
    return score_list1

def get_top_scores():
    top_scores = get_top_scores()
    top_scores = sorted(score_list1, key=lambda k: k['attempts'])[:3]
    return top_scores


