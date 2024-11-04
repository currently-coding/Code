FILEPATH = "garten0.txt"


def read_input(filepath):
    with open(filepath, "r") as f:
        # Read and strip lines, then parse values into a dictionary
        lines = [line.strip() for line in f.readlines()]

    return {
        "fields": int(lines[0]),  # Number of fields
        "height": float(lines[1]),  # Height of the property
        "width": float(lines[2]),  # Width of the property
    }

def find(data):
    height = data["height"]
    width = data["width"]
    num_fields = 1 # no divisions yet
    height_divisions = 1 
    width_divisions = 1
    md_height = height/height_divisions
    md_width = width/width_divisions

    while num_fields < data["fields"]:
        if md_height > md_width:
            



data = read_input(FILEPATH)
