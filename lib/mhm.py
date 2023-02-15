"""
Mead Head Math [mhm] module.
Provides the basic math behind calculating / predicting weights and or
intesities.
"""
from typing import Tuple


def one_rep_max(reps: float, weight: float) -> float:
    """
    Cummings and Finn:
    1RM (kg) = 1.175 RepWt + 0.839 Reps –4.29787
    """
    rm = weight / (1.0278 - 0.0278 * reps)
    return rm


def relative_intensity(reps: float, weight: float, one_rm: float):
    """
    Realtive Intensity:
    takes the weight you did for a number of reps divided by the highest
    weight you could do at that rep range
    """
    max_weight = one_rm * (1.0278 - 0.0278 * reps)
    ai = (weight) / one_rm
    ri = ai / (max_weight / one_rm)
    return map(lambda x: round(x, 3), (ai, ri))


def increased_ai(reps: int, desired_ri: float) -> float:
    """
    Allow users to determine the increase in actual intensity for a desired
    increase in relative intensity in a given rep range.
    """
    mi = 1.0278 - 0.0278 * reps
    new_ai = (mi * (desired_ri)) / 100
    return round(new_ai, 3)
