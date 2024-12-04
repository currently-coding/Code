from os import walk
import sys
import re
from pathlib import Path


def read_file(filepath):
    """Reads and returns the content of the file."""
    with open(filepath, "r") as file:
        return file.read().strip()


def parse_input(input_data):
    """Parses the input data into a usable format."""
    # input_data = input_data.splitlines()
    input_data = input_data.split()
    data = []
    for a in range(len(input_data)):
        data.append([])
        for b in range(len(input_data[a])):
            data[a].append(input_data[a][b])

    # Example: split into lines and integers
    # return (
    #     [line for line in input_data if input_data.index(line) % 2 == 0],
    #     [line for line in input_data if input_data.index(line) % 2 != 0],
    # )
    return input_data


def rotate_45_and_trim(matrix):
    n = len(matrix)
    m = len(matrix[0])
    size = n + m - 1  # New matrix size for 45° rotation

    # Initialize the larger matrix to hold rotated values
    rotated_matrix = [[0 for _ in range(size)] for _ in range(size)]
    mid = size // 2  # Center index of the new matrix

    for i in range(n):
        for j in range(m):
            new_i = mid + i - j  # Compute new row index
            new_j = i + j  # Compute new column index
            rotated_matrix[new_i][new_j] = matrix[i][j]

    # Remove rows and columns containing only zeros
    trimmed_matrix = [row for row in rotated_matrix if any(row)]
    max_width = max(len(row) for row in trimmed_matrix)
    trimmed_matrix = [[val for val in row if val != 0] for row in trimmed_matrix]

    return trimmed_matrix


def p(data):
    print("Printing")
    for a in data:
        print("".join(a))


def solve_part1(data):
    """Solves Part 1 of the problem."""
    data = data
    data1 = list(zip(*data[::-1]))
    data2 = list(zip(*data1[::-1]))
    data3 = list(zip(*data2[::-1]))
    data4 = rotate_45_and_trim(data1)
    data5 = rotate_45_and_trim(data2)
    data6 = rotate_45_and_trim(data3)
    data7 = rotate_45_and_trim(data)
    all = [data4, data5, data6, data7]
    print(all)
    # Add solution logic here

    count = 0
    prev_line, next_line = [], []
    for outer, i in enumerate(all):
        for inner, o in enumerate(i):
            for i, char in enumerate(o):
                print(prev_line, next_line)
                if len(next_line) > 0:
                    for index in next_line[1:]:
                        if (
                            all[outer][inner][index - 1] == "M"
                            and all[outer][inner][index] == "A"
                            and all[outer][inner][index + 1] == "S"
                        ):
                            count += 1
                        if (
                            all[outer][inner][index - 1] == "S"
                            and all[outer][inner][index] == "A"
                            and all[outer][inner][index + 1] == "M"
                        ):
                            count += 1
                    next_line = []
                if len(prev_line) > 0:
                    for index in prev_line[1:]:
                        if (
                            all[outer][inner][index - 1] == "M"
                            and all[outer][inner][index] == "A"
                            and all[outer][inner][index + 1] == "S"
                        ):
                            count += 1
                        if (
                            all[outer][inner][index - 1] == "S"
                            and all[outer][inner][index] == "A"
                            and all[outer][inner][index + 1] == "M"
                        ):
                            count += 1

                    prev_line = []
                print(all[outer][inner])
                if all[outer][inner][i] == "S":
                    next_line.append(inner)
                if all[outer][inner][i] == "2":
                    prev_line.append(inner)

                print(prev_line, next_line)

        # out = re.findall(r"XMAS", "".join(o))
        # out += re.findall(r"SAMX", "".join(o))
        # count += len(out)
    return count


def solve_part2(data):
    """Solves Part 2 of the problem."""

    # Add solution logic here
    pass


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)

    # Read the input file
    input_filepath = Path(sys.argv[1])
    input_data = read_file(input_filepath)

    # Parse input
    data = parse_input(input_data)

    # Solve parts
    print("Part 1:", solve_part1(data))
    print("Part 2:", solve_part2(data))
