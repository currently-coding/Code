#include <math.h>
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

input read_file(char filename[200]) {
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

double binary_search(int num_fields, double width, double height) {
  double low = 0;
  double high = 1;
  double min_size = num_fields;
  double max_size = num_fields * 1.1;

  while (1) {
    double mid = (low + high) / 2;
    double size = pow(width, mid) * pow(height, mid);

    if (size < min_size) {
      low = mid;
    } else if (size > max_size) {
      high = mid;
    } else {
      return mid;
    }
  }
}

size calc_width_and_height(double exponent, double width, double height) {
  size size;
  size.width = width / pow(width, exponent);
  size.height = height / pow(height, exponent);
  return size;
}

size solve(char path[20]) {
  input input = read_file(path);
  double exponent =
      binary_search(input.num_fields, input.size.width, input.size.height);
  size solution =
      calc_width_and_height(exponent, input.size.width, input.size.height);
  return solution;
}

void output(size solution) {
  printf("Field size: %lf\n", solution.width * solution.height);
  printf("Field height: %lf\n", solution.height);
  printf("Field width: %lf\n", solution.width);
}

int main() {
  char path[20];
  for (int i = 0; i < 5; i++) {
    sprintf(path, "garten%d.txt", i);
    output(solve(path));
  }
}
