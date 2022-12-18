## PART 1

filename = "day2.txt"
options = ["Rock", "Paper", "Scissors"]
opponent = ["A", "B", "C"]
player = ["X", "Y", "Z"]
total_score = 0

def get_score(opponent_choice, player_choice):
    score = 0
    if opponent_choice == player_choice:
        score += player_choice + 1 + 3
    elif opponent_choice == 2 and player_choice == 0: # scissors vs rock
        score += 1 + 6
    elif opponent_choice == 0 and player_choice == 1: # rock vs paper
        score += 2 + 6
    elif opponent_choice == 1 and player_choice == 2: # paper vs scissors
        score += 3 + 6
    elif opponent_choice == 1 and player_choice == 0: # paper vs rock
        score += 1
    elif opponent_choice == 2 and player_choice == 1: # scissors vs paper
        score += 2
    elif opponent_choice == 0 and player_choice == 2: # rock vs scissors
        score += 3
    return score

with open(filename) as rps_inputs:
    rps_guide = rps_inputs.read().split("\n")

for round_n in range(len(rps_guide)):
    opponent_choice = opponent.index(rps_guide[round_n][0])
    player_choice = player.index(rps_guide[round_n][2])
    total_score += get_score(opponent_choice, player_choice)

print(f"Total score: {total_score}")

## PART 2

outcomes = ["Lose", "Draw", "Win"]
total_score = 0

def get_score(opponent_choice, outcome):
    score = 0
    if outcome == 1: # draw
        score += opponent_choice + 1 + 3
    elif outcome == 0: # lose
        if opponent_choice == 0: # opponent rock
            score += 3
        elif opponent_choice == 1: # opponent paper
            score += 1
        elif opponent_choice == 2: # opponent scissors
            score += 2
    elif outcome == 2:
        if opponent_choice == 0: # opponent rock
            score += 2 + 6
        elif opponent_choice == 1: # opponent paper
            score += 3 + 6
        elif opponent_choice == 2: # opponent scissors
            score += 1 + 6
    return score

for round_n in range(len(rps_guide)):
    opponent_choice = opponent.index(rps_guide[round_n][0])
    outcome = player.index(rps_guide[round_n][2])
    total_score += get_score(opponent_choice, outcome)

print(f"Total score: {total_score}")