class BasketballPlayer():
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

lebron = BasketballPlayer(first_name="Lebron", last_name="James", height_cm="205", weight_kg="112", points="158", rebounds="64", assists="25")
kev_dur = BasketballPlayer(first_name="Kevin", last_name="Duran", height_cm="200", weight_kg="100", points="126", rebounds="54", assists="31")

print(lebron.first_name)
print(lebron.height_cm)

print(kev_dur.last_name)

def weight_to_lbs(self):
    pounds = self.weight_kg * 2.2045
    return pounds

print(kev_dur.weight_kg)

class FootballPlayer():
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

ronaldo = FootballPlayer(first_name="Cristiano", last_name="Ronaldo", height_cm=184, weight_kg=79, goals=586, yellow_cards=95, red_cards=11)
messi = FootballPlayer(first_name="Lionel", last_name="Messi", height_cm=170, weight_kg=67, goals=575, yellow_cards=67, red_cards=0)

print(ronaldo.first_name)
print(ronaldo.goals)
print(messi.first_name)
print(messi.goals)

class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

bball_players = [lebron, kev_dur]

for player in bball_players:
    print(player.last_name + ", " + player.first_name)






