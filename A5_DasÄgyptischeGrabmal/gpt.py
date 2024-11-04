from pprint import pprint  # Added to use pprint for pretty printing


def read_file(path):
    print("Reading from")
    with open(path, "r") as f:
        lines = f.readlines()
    periods = [int(period.strip()) for period in lines[1:]]

    print(periods)
    return periods


class Maze:
    def __init__(self, path) -> None:
        self.periods = [period for period in read_file(path)]
        self.minute = 0
        self.cube = [False] * len(self.periods)
        self.persons = [False] * len(self.periods)
        self.path = []

    def update(self):
        """
        call every move to simulate the movements of the Maze
        """
        self.minute += 1
        change = False  # if nothing has changed dont bother calculating possible moves
        for i, _ in enumerate(self.periods):
            period = self.periods[i]
            if (self.minute % period) == 0:
                self.cube[i] = not self.cube[i]
                change = True
        return change

    def move(self):
        while not self.persons[-1]:  # Continue until the last person reaches the end
            if not self.update():
                continue  # Skip if there are no updates

            # Track the last occupied position to optimize movement
            last_occupied = -1

            for position in range(len(self.persons)):
                # Skip if the current position is closed and no one is present
                if not (self.persons[position] or self.cube[position]):
                    continue

                # Spawn a new person at position 0 if it is open and unoccupied
                if position == 0 and self.cube[position] and not self.persons[0]:
                    self.persons[position] = True

                # If a person is present at the current position
                if self.persons[position]:
                    # Check if they are dead
                    if self.dead(position):
                        self.persons[position] = False  # Remove if dead
                        continue  # Skip to next position

                    # Move to the current position if the previous is occupied
                    if position > 0 and self.persons[position - 1]:
                        self.persons[position] = True

                    # Update the last occupied position
                    last_occupied = position

            # Move all persons forward from the last occupied position
            if last_occupied != -1:  # Check if there was any occupied position
                for move_position in range(last_occupied + 1, len(self.cube)):
                    if not self.cube[move_position]:  # Stop if the next cube is closed
                        break
                    if self.persons[move_position]:  # If the next position is occupied
                        for idx in range(last_occupied + 1, move_position):
                            self.persons[idx] = True  # Move all persons in between

            pprint(self.persons)

    def dead(self, position):
        return not self.cube[position]  # True = not dead -> return False

    def calc_path(self):
        pass

    def output(self):
        pprint(self.cube)
        pprint(self.persons)
        self.calc_path()
        print("The end")

    def solve(self):
        self.move()
        self.output()


maze = Maze("grabmal2.txt").solve()
