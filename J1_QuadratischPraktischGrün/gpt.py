def read_input(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()

    file = {
        "fields": int(lines[0].strip()),
        "height": float(lines[1].strip()),
        "width": float(lines[2].strip()),
    }

    return file


def find_best_field_configuration(num_fields, width, height):
    # Calculate the minimum and maximum number of fields allowed
    min_size = num_fields
    max_size = int(num_fields * 1.1)

    best_config = (0, 0, 0)  # field_size, field_height, field_width
    best_diff = float("inf")  # To find the most square-like configuration

    for fields in range(min_size, max_size + 1):
        # Calculate potential dimensions
        field_width = width / fields**0.5  # Width based on sqrt of number of fields
        field_height = height / fields**0.5  # Height based on sqrt of number of fields

        field_size = field_width * field_height  # Calculate field size

        # Measure how square-like the configuration is
        diff = abs(
            field_width - field_height
        )  # The difference between width and height

        # Store the best configuration
        if diff < best_diff:
            best_diff = diff
            best_config = (field_size, field_height, field_width)

    return best_config


def solve(path):
    file = read_input(path)
    solution = find_best_field_configuration(
        file["fields"], file["width"], file["height"]
    )
    return solution, file


def output(solution, file):
    print("Field size: ", solution[0])
    print("Field width: ", solution[1])
    print("Field height: ", solution[2])
    print("\tNumber of fields: ", (file["height"] * file["width"]) / solution[0])
    print("Vertical: ", file["height"] / solution[2])
    print("Horizontal: ", file["width"] / solution[1])
    print("Wanted: ", file["fields"])


custom_predefined = "garten"
for num in range(5):
    path = f"{custom_predefined}{num}.txt"
    print(path)
    solution, file = solve(path)
    output(solution, file)
