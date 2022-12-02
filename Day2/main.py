opponent_rock = "A"
opponent_paper = "B"
opponent_scissor = "C"

me_rock = "X"
me_paper = "Y"
me_scissor = "Z"

scores = {me_rock: 1, me_paper: 2, me_scissor: 3}

win = 6
draw = 3
lose = 0


def outcome(opponent: str, me: str):
    if (opponent == opponent_rock and me == me_rock) or (opponent == opponent_paper and me == me_paper) or (
            opponent == opponent_scissor and me == me_scissor):
        outcome_score_round = draw
    elif (opponent == opponent_rock and me == me_paper) or (opponent == opponent_paper and me == me_scissor) or (
            opponent == opponent_scissor and me == me_rock):
        outcome_score_round = win
    else:
        outcome_score_round = lose
    outcome_score_round += scores[me]
    return outcome_score_round


total_score = 0
for line in open("strategies.txt", "r").readlines():
    line = line.replace("\n", "")
    opponent_hand, me_hand = line.split(" ")
    outcome_score = outcome(opponent_hand, me_hand)
    total_score += outcome_score

print(total_score)
