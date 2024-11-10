from os import wait
from datetime import datetime


def read_file(path):
    with open(path, "r") as f:
        lines = f.readlines()
    periods = [int(period.strip()) for period in lines[1:]]

    return periods


class Maze:
    def __init__(self, path: str) -> None:
        self.periods = [period for period in read_file(path)]
        self.minute = 0
        self.cube: list[bool] = [False] * len(self.periods)
        self.persons: list[bool] = [False] * len(self.periods)
        self.path = {}  # {(pos, min): pos}

    def update(self):
        """
        call every move to simulate the movements of the Maze
        """
        self.minute += 1
        change = False  # if nothing has changed dont bother calculating possible moves

        for i in range(len(self.periods)):
            period = self.periods[i]
            if (self.minute % period) == 0:
                self.cube[i] = not self.cube[i]
                change = True
        return change

    def move(self):
        while not self.persons[-1]:
            # self.path[self.minute] = []
            if not self.update():
                self.path[self.minute] = []
                continue
            self.path[self.minute] = []
            tmp = []
            for position, _ in enumerate(self.persons):
                if self.dead(position):
                    self.persons[position] = False
                    continue
                if not (self.persons[position] or self.cube):
                    continue
                if position == 0 and self.cube[position]:
                    if not self.persons[0]:
                        self.persons[position] = True
                    tmp.append((0, 1))
                if self.person_at(position - 1):
                    for index in range(position, self.moving(position, 1)):
                        self.persons[index] = True
                        tmp.append((index, index + 1))
                elif self.person_at(position + 1):
                    for index in range(position, self.moving(position, -1), -1):
                        self.persons[index] = True
                        tmp.append((index, index + 1))
            tmp = list(set(tmp))
            self.path[self.minute].append(tmp)

    def dead(self, position):
        return (not self.cube[position]) and self.persons[position]

    def moving(self, position, dir):
        current = position
        while (-1 < current < len(self.cube)) and self.cube[current]:
            current += dir
        return current

    def person_at(self, position):
        if 0 <= position < len(self.persons):
            return self.persons[position]
        else:
            return False

    def trace_path(self):
        start = 0
        end = len(self.cube)
        current = end
        minute = self.minute
        path = {}
        while current != start and minute > -1:
            pathb = []
            if len(self.path[minute]) > 0:
                pathb = self.path[minute][0]
            path[minute] = []
            for _ in pathb:
                for pair in pathb:
                    if pair[1] == current:
                        current = pair[0]
                        path[minute].append((pair[1], pair[0]))
            minute -= 1
        self.path = path

    def calc_path(self):
        self.path = {key: value for key, value in self.path.items() if value}
        current_sector = 0
        path_result = [0]
        duration_result = []
        end = len(self.cube)
        last = 0

        # We will trace from sector 0 and find the transitions
        while current_sector != end:
            for key, transitions in self.path.items():
                for next_sec, prev in transitions:
                    if prev == current_sector:
                        path_result.append(next_sec)
                        duration_result.append(
                            key - last
                        )  # The current key represents the time spent in the sector
                        current_sector = next_sec
                        last = key
                        break
        self.path = [path_result, duration_result]

    def instructions(self):
        total_time = 0
        for idx in range(len(self.path[0]) - 1):
            total_time += self.path[1][idx]
            print(
                f"Warte {self.path[1][idx]} Minuten in Abschnitt  {self.path[0][idx]}, gehe dann in Abschnitt {self.path[0][idx+1]}"
            )
        print("Total time: ", self.minute)
        print("Total path time: ", total_time)
        print("Difference: ", self.minute - total_time)

    def output(self):
        self.trace_path()
        self.calc_path()
        self.instructions()

    def solve(self):
        print("Solving Maze...")
        n1 = datetime.now()
        self.move()
        n2 = datetime.now()
        print(f"\nMaze completed after {n2-n1}s. Calculating path...\n")
        n3 = datetime.now()
        self.output()
        n4 = datetime.now()
        print(f"\nFinished path calculation in {n4-n3}s.\n")
        print("Total execution time: ", n4 - n1, "s")


maze = Maze("grabmal5.txt").solve()
