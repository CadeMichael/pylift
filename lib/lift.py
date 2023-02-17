import lib.mhm as mhm
from typing import List


class Lift:
    def __init__(self, date: str, sets: List):
        self.date = date
        self.sets = sets

    def volume(self) -> float:
        vol = 0
        for lift in self.sets:
            w, r, s = lift
            vol += w * r * s
        return vol

    def rel_int(self, rm: float) -> float:
        highest = 0
        for lift in self.sets:
            weight = lift[0]
            reps = lift[1]
            ri = mhm.relative_intensity(reps, weight, rm)[1]
            if ri > highest:
                highest = ri
        return highest * 100
