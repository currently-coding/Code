from pprint import pprint  # For pretty printing


def read_file(path):
    with open(path, "r") as f:
        lines = f.readlines()
    periods = [int(period.strip()) for period in lines[1:]]
    print(periods)
    return periods


class Maze:
    def __init__(self, path: str) -> None:
        self.periods = read_file(path)
        self.minute = 0
        self.cube: list[bool] = [False] * len(self.periods)
        self.persons: list[bool] = [False] * len(self.periods)
        self.path = {}  # {(minute): [(start_pos, end_pos), ...]}

    def update(self):
        """Simulate cube state changes per minute."""
        self.minute += 1
        change = False
        for i, period in enumerate(self.periods):
            if (self.minute % period) == 0:
                self.cube[i] = not self.cube[i]
                change = True
        return change

    def move(self):
        while not self.persons[-1]:  # Continue until the last position is reached
            self.path[self.minute] = []
            if not self.update():
                continue

            for position in range(len(self.persons)):
                if self.dead(position):
                    self.persons[position] = False
                    continue

                # Movement logic
                if self.person_at(position - 1) and not self.cube[position]:
                    new_pos = self.moving(position, 1)
                    for idx in range(position, new_pos):
                        self.persons[idx] = True
                        self.path[self.minute].append((position, idx + 1))

                elif self.person_at(position + 1) and not self.cube[position]:
                    new_pos = self.moving(position, -1)
                    for idx in range(position, new_pos, -1):
                        self.persons[idx] = True
                        self.path[self.minute].append((position, idx - 1))

        print("\n**")
        print(f"Person reached the end after {self.minute} minutes.")
        print("**\n")

    def dead(self, position):
        return not self.cube[position] and self.persons[position]

    def moving(self, position, direction):
        """Find the next valid position in a direction."""
        current = position
        while 0 <= current < len(self.cube) and self.cube[current]:
            current += direction
        return current

    def person_at(self, position):
        """Check if there is a person at a position."""
        return 0 <= position < len(self.persons) and self.persons[position]

    def calc_path(self):
        tracked_path = []
        end_pos = len(self.cube) - 1
        current_pos = end_pos
        current_min = self.minute

        while current_pos != 0:
            tracked_path.append((current_pos, current_min))
            current_min -= 1
            for start, end in self.path.get(current_min, []):
                if end == current_pos:
                    current_pos = start
                    break

        tracked_path.reverse()
        pprint(tracked_path)
        return tracked_path

    def output(self):
        pprint(self.cube)
        pprint(self.persons)
        tracked_path = self.calc_path()
        pprint(self.path)
        print("Tracked Path:", tracked_path)
        print("The end")

    def solve(self):
        self.move()
        self.output()


maze = Maze("grabmal0.txt").solve()
