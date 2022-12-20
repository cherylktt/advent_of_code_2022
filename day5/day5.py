## PART 1

filename = "day5.txt"

with open(filename) as crate_input:
    crate_arrangements = crate_input.read().split("\n")

crates = crate_arrangements[:8]
instructions = crate_arrangements[10:]

# Get crates matrix
def get_crates_matrix(crates):
    crates_matrix = []
    for row in crates:
        row = row.replace("    ", "  0 ").split()
        for i in range(len(row)):
            if row[i] != "0":
                row[i] = row[i][1]
        crates_matrix.append(row)
    return crates_matrix

# Get instructions
def get_instructions(instruction):
    if instruction[6].isnumeric():
        return int(instruction[5:7]), int(instruction[-6])-1, int(instruction[-1])-1 # double digit number of boxes, initial column, final column
    else:
        return int(instruction[5]), int(instruction[-6])-1, int(instruction[-1])-1 # single digit number of boxes, initial column, final column

# Get box to move
def get_box(column):
    for row in range(len(crates_matrix)):
        if crates_matrix[row][column] != "0":
            return crates_matrix[row][column], row # box, original row

# Replace initial position of box with "0"
def replace_with_empty(row, column):
    crates_matrix[row][column] = "0"

# Move box to new column
def move_box(box, column):
    for row in range(len(crates_matrix)):
        if crates_matrix[row][column] != "0":
            if row == 0:
                crates_matrix.insert(0, ["0", "0", "0", "0", "0", "0", "0", "0", "0"])
                crates_matrix[0][column] = box
                break
            else:
                crates_matrix[row-1][column] = box
                break
        elif crates_matrix[-1][column] == "0":
            crates_matrix[-1][column] = box
            break

crates_matrix = get_crates_matrix(crates)

for i in range(len(instructions)):
    number_of_boxes, box_column_initial, box_column_final = get_instructions(instructions[i])
    while number_of_boxes > 0:
        box, box_row = get_box(box_column_initial)
        replace_with_empty(box_row, box_column_initial)
        move_box(box, box_column_final)
        number_of_boxes -= 1

top_crates = ""
for column_n in range(9):
    for row_n in range(len(crates_matrix)):
        if crates_matrix[row_n][column_n] != "0":
            top_crates += crates_matrix[row_n][column_n]
            break

print(f"Crates on top: {top_crates}")

## PART 2

# Get box to move
def get_box(number_of_boxes, column):
    boxes = []
    boxes_rows = []
    while number_of_boxes > 0:
        for row in range(len(crates_matrix)):
            if crates_matrix[row][column] != "0":
                boxes.append(crates_matrix[row][column])
                boxes_rows.append(row)
                crates_matrix[row][column] = "0"
                break
        number_of_boxes -= 1
    return boxes, boxes_rows

crates_matrix = get_crates_matrix(crates)

for i in range(len(instructions)):
    number_of_boxes, box_column_initial, box_column_final = get_instructions(instructions[i])
    boxes, boxes_rows = get_box(number_of_boxes, box_column_initial)
    for j in range(1, len(boxes)+1):
        replace_with_empty(boxes_rows[-j], box_column_initial)
        move_box(boxes[-j], box_column_final)

top_crates = ""
for column_n in range(9):
    for row_n in range(len(crates_matrix)):
        if crates_matrix[row_n][column_n] != "0":
            top_crates += crates_matrix[row_n][column_n]
            break

print(f"Crates on top: {top_crates}")