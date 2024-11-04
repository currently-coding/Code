#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct size {
  double width;
  double height;
} size;

typedef struct input {
  int num_fields;
  size size;
} input;

typedef struct output {
  int width_felder;
  int height_felder;
} output;

input read_file(const char filename[200]) {
  FILE *source = fopen(filename, "r");
  if (!source) {
    printf("Unable to open file.\n");
    exit(1);
  }

  input file_data;
  char buffer[10];

  for (int line = 0; fgets(buffer, sizeof(buffer), source) != NULL; line++) {
    switch (line) {
    case 0:
      file_data.num_fields = atoi(buffer);
      break;
    case 1:
      file_data.size.height = atof(buffer);
      break;
    case 2:
      file_data.size.width = atof(buffer);
      break;
    default:
      break;
    }
  }

  fclose(source);   // Close the file after reading
  return file_data; // Return the struct with parsed values
}

output find_distribution(input file_data) {
  int x_felder = 1;
  int y_felder = 1;
  float x_aufgeteilt = file_data.size.width / (double)x_felder;
  float y_aufgeteilt = file_data.size.height / (double)y_felder;
  while ((x_felder * y_felder) < file_data.num_fields) {
    x_aufgeteilt = file_data.size.width / (float)x_felder;
    y_aufgeteilt = file_data.size.height / (float)y_felder;
    if (x_aufgeteilt > y_aufgeteilt) {
      x_felder++;
    } else {
      y_felder++;
    }
  }
  output out = {x_felder, y_felder};
  return out;
}

int main(int argc, char *argv[]) {
  const char filename[200] = "garten5.txt";
  input data = read_file(filename);
  output out = find_distribution(data);

  // Additional helpful output
  double total_area =
      data.size.width * data.size.height; // Calculate total area
  double garden_area =
      total_area /
      (out.width_felder * out.height_felder); // Calculate area per garden
  double field_width =
      data.size.width / out.width_felder; // Width of each garden
  double field_height =
      data.size.height / out.height_felder; // Height of each garden

  // Normal output without formatting
  printf("\nDas Grundstück hat eine Größe von: %.2f m²\n",
         total_area); // Total area
  printf("Mindestanzahl der Kleingärten: %d\n",
         data.num_fields); // Minimum number of gardens
  printf("Maximale Anzahl der Kleingärten: %d\n",
         (int)(data.num_fields * 1.1)); // Maximum number of gardens
  printf("Größe jedes Kleingartens: %.2f m²\n",
         garden_area); // Area of each garden
  printf("Verhältnis Breite zu Höhe der Kleingärten: %.2f\n",
         (field_width / field_height)); // Width to height ratio

  // Final output
  printf(" -  - - - - - - - - - - - - - - - - - - - - - - - -");
  printf("Das Feld muss in Spalten aufgeteilt werden: %d\n", out.width_felder);
  printf("Das Feld muss in Zeilen aufgeteilt werden: %d\n", out.height_felder);

  return EXIT_SUCCESS;
}
