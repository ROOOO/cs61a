"""
    This file contains your final_strategy that will be submitted to the contest.
    It will only be run on your local machine, so you can import whatever you want!
    Remember to supply a unique PLAYER_NAME or your submission will not succeed.
"""

from hog import GOAL_SCORE, bacon_strategy, extra_turn, free_bacon


PLAYER_NAME = 'ROOOO'  # Change this line!


def final_strategy(score, opponent_score):
    """
    1. If current score plus free_bacon score is higher than GOAL_SCORE, roll 0 dice.
    2. Try to force extra turns.
    3. Take fewer risk if score is almost achieve the GOAL_SCORE.
    4. CUTOFF and NUM_ROLLS are 11 and 5 respectively when average win rate is highest
    which is about 60% when versus to always_roll(6) and approximatey 70% when versus
    to always_roll(4).
    """
    score_bacon = free_bacon(opponent_score)
    if score + score_bacon >= GOAL_SCORE:
        return 0
    if extra_turn(score + score_bacon, opponent_score):
        return 8 # addition game rule
    if score >= 94:
        return 1
    elif score >= 88:
        return 2
    return bacon_strategy(score, opponent_score, 11, 5)
