import csv
from typing import List
from lib.lift import Lift
import configparser
import os


def get_lift_dir():
    try:
        config = configparser.ConfigParser()
        config.read(f"{os.environ.get('HOME')}/.config/pylift.ini")
        filepath = config["dir"]["lift_path"]
    except:
        filepath = f"{os.environ.get('HOME')}/Documents"
    return filepath


def read_lift(name: str, path: str = get_lift_dir()) -> List | str:
    try:
        file = f"{path}/{name}.csv"
        with open(file, newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")

            def conv_num(row):
                if len(row) == 3 and row[0] != "/* Weight":
                    return list(map(lambda x: float(x), row))
                return row

            try:
                rows = [conv_num(row) for row in reader]
            except:
                return f"Malformed {name}.csv"

            return rows[3:]
    except:
        return f"No file {name}.csv"


def make_lift_list(name: str, path: str = get_lift_dir()) -> List[Lift]:
    data = read_lift(name, path)
    if type(data) == str:
        return []
    lifts: List[Lift] = []
    date: str = ""
    sets: List = []

    # get rid of [] caused by newlines in the file
    data = [d for d in data if d != []]
    for row in data:
        if len(row) == 1 and sets != []:
            newlift = Lift(date, sets)
            lifts = [*lifts, newlift]
            date = row[0]
            sets = []
        elif sets == [] and len(row) == 1:
            date = row[0]
        else:
            sets.append(row)

    if sets != []:
        lifts.append(Lift(date, sets))

    return lifts


def create_lift(name: str, path: str = get_lift_dir()) -> str:
    try:
        file = f"{path}/{name}.csv"
        with open(file, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            rows = [["/* Date */ "], ["/* Weight", " Reps", " Sets */"], []]
            writer.writerows(rows)
            return f"New lift {name}.csv written."
    except:
        return "Name given is incorrect."
