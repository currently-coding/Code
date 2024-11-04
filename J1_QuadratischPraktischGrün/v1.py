def read_input(filepath):
    with open(filepath, "r") as f:
        # Read and strip lines, then parse values into a dictionary
        lines = [line.strip() for line in f.readlines()]

    return {
        "fields": int(lines[0]),  # Number of fields
        "height": float(lines[1]),  # Height of the property
        "width": float(lines[2]),  # Width of the property
    }


def binary_search(num_fields, width, height):
    low, high = 0, 1
    min_size = num_fields
    max_size = int(num_fields * 1.05)

    while True:
        mid = (low + high) / 2
        size = (width**mid) * (height**mid)  # Area calculation

        if size < min_size:
            low = mid  # Increase mid if size is too small
        elif size > max_size:
            high = mid  # Decrease mid if size is too large
        else:
            return mid  # Return the exponent if within bounds


def calculate_width_and_height(exponent, width, height):
    # Calculate field dimensions based on the exponent
    field_width = width / (width**exponent)  # Corrected division for dimensions
    field_height = height / (height**exponent)
    field_size = field_width * field_height
    return (field_size, field_height, field_width)


def solve(path):
    # Read input data
    file = read_input(path)
    # Find the exponent using binary search
    exponent = binary_search(file["fields"], file["width"], file["height"])
    # Calculate field dimensions
    solution = calculate_width_and_height(exponent, file["width"], file["height"])
    return solution, file


def output(solution, file):
    print(f"Vorgeschlagene Aufteilung für {file['fields']} Kleingärten:")

    print(f"Feldgröße: {solution[0]:.6f} m²")  # Field size
    print(f"\tFeldbreite: {solution[2]:.6f} m")  # Field width
    print(f"\tFeldhöhe: {solution[1]:.6f} m")  # Field height
    print(
        f"Anzahl der Felder: {int((file['height'] * file['width']) / solution[0])}"
    )  # Total number of fields
    print(
        f"\tVertikale Aufteilung: {file['height'] / solution[1]:.6f} Felder"
    )  # Vertical count of fields
    print(
        f"\tHorizontale Aufteilung: {file['width'] / solution[2]:.6f} Felder"
    )  # Horizontal count of fields
    print(
        f"\nWunschanzahl der Interessenten: {file['fields']}"
    )  # Wanted number of fields


# Main execution block
custom_predefined = "garten"
for num in range(5):
    path = f"{custom_predefined}{num}.txt"
    print(" - " * 30)
    print(path)
    solution, file = solve(path)
    output(solution, file)
