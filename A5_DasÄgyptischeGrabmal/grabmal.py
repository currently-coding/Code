from pprint import pprint  # Added to use pprint for pretty printing
from collections import deque


def read_file(path):
    with open(path, "r") as f:
        lines = f.readlines()
    periods = [int(period.strip()) for period in lines[1:]]

    print(periods)
    return periods


class Maze:
    def __init__(self, path: str) -> None:
        self.periods = [period for period in read_file(path)]
        self.minute = 0
        self.cube: list[bool] = [False] * len(self.periods)
        self.persons: list[bool] = [False] * len(self.periods)
        self.path = {}

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
            if not self.update():
                continue
            self.path[self.minute] = []
            for position, _ in enumerate(self.persons):
                if self.dead(position):
                    self.persons[position] = False
                    continue
                if not (self.persons[position] or self.cube):
                    continue
                if position == 0 and self.cube[position]:
                    if not self.persons[0]:
                        self.persons[position] = True
                        self.path[self.minute].append((0, 1))
                if self.person_at(position - 1):
                    for index in range(position, self.moving(position, 1)):
                        self.persons[index] = True
                        self.path[self.minute].append((position, index + 1))
                elif self.person_at(position + 1):
                    for index in range(position, self.moving(position, -1), -1):
                        self.persons[index] = True
                        self.path[self.minute].append((position, index + 1))

        print("\n*" * 2)
        print(f"Person reached the end after {self.minute} Minutes.")
        print("\n*" * 2)

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

    def calc_path(self):
        start = 0
        end = len(self.cube)
        path_dict = self.path
        result = []

        # Queue holds (current_section, path_so_far)
        queue = deque([(start, [])])
        visited = set()  # To track visited sections

        while queue:
            current_section, path = queue.popleft()

            # If we reach the end section, return the path
            if current_section == end:
                result = []
                for step in path:
                    waiting_time = step[1] - step[0]
                    result.append(
                        f"Warte {waiting_time} Minuten, Gehe von Abschnitt {
                            step[0]} in Abschnitt {step[1]}."
                    )
                return "\n".join(result)

            # Mark the section as visited
            visited.add(current_section)

            # Traverse all neighbors
            for next_section, pairs in path_dict.items():
                for pair in pairs:
                    if pair[0] == current_section and pair[1] not in visited:
                        # Add to path and queue
                        queue.append((pair[1], path + [pair]))

        return result

    def output(self):
        pprint(self.cube)
        pprint(self.persons)
        print(self.calc_path())
        print("The end")

    def solve(self):
        self.move()
        self.output()


maze = Maze("grabmal3.txt").solve()
