from typing import List
import matplotlib
import matplotlib.pyplot as plt
import lib.filemanager as fm
from lib.lift import Lift

# matplotlib.use('qtagg')


def show_bar_charts(name: str, rm: float):
    lis: List[Lift] = fm.make_lift_list(name)

    if lis == []:
        return "*workout not found...*"
    try:
        dates = [l.date for l in lis]
        vols = [l.volume() for l in lis]
        rints = [l.rel_int(rm) for l in lis]

        _, axes = plt.subplots(2, 1, constrained_layout=True)
        a1 = axes[0]
        a2 = axes[1]
        a1.set_title("Volume (weight * reps * sets) vs Time")
        a1.set_ylabel("Volume")
        a2.set_title("Relative intensity (%) vs Time")
        a2.set_xlabel("Date (m-d-y)")
        a2.set_ylabel("Relative Intensity (%)")

        for i in range(len(dates)):
            a1.bar(dates[i], vols[i])
            a1.text(dates[i], vols[i] // 2, s=f"{vols[i]}", ha="center")
            a2.bar(dates[i], rints[i])
            a2.text(dates[i], rints[i] // 2, s=f"{round(rints[i], 3)}%", ha="center")

        plt.show()

    except:
        return "*error cannot print graph*"
