## PART 1

def check_row(current_column_index, row_index, tree, visible_left=True, visible_right=True):
    for i in range(current_column_index):
        if tree[row_index][i] >= tree[row_index][current_column_index]:
            visible_left = False
    for j in range(current_column_index+1, 101):
        if tree[row_index][j] >= tree[row_index][current_column_index]:
            visible_right = False
    return visible_left or visible_right

def check_column(current_row_index, column_index, tree, visible_top=True, visible_bottom=True):
    for i in range(current_row_index):
        if tree[i][column_index] >= tree[current_row_index][column_index]:
            visible_top = False
    for j in range(current_row_index+1, 101):
        if tree[j][column_index] >= tree[current_row_index][column_index]:
            visible_bottom = False
    return visible_top or visible_bottom

filename = "day8.txt"
inside_tree_map = []
visible_trees = []
number_of_visible_trees = 0

with open(filename) as map_input:
    tree_map = map_input.read().split("\n")

inside_tree_map.append([0]*101)
for i in range(0, len(tree_map)):
    trees = []
    trees.append(0)
    for char in tree_map[i]:
        trees.append(int(char))
    trees.append(0)
    inside_tree_map.append(trees)
inside_tree_map.append([0]*101)

for j in range(1, len(inside_tree_map)-1):
    for k in range(1, len(inside_tree_map[j])-1):
        if j == 1 or k == 1:
            visible_trees.append([j, k, inside_tree_map[j][k]])
            number_of_visible_trees += 1
        elif j == 99 or k == 99:
            visible_trees.append([j, k, inside_tree_map[j][k]])
            number_of_visible_trees += 1
        else:
            if check_row(k, j, inside_tree_map) == True or check_column(j, k, inside_tree_map) == True:
                visible_trees.append([j, k, inside_tree_map[j][k]])
                number_of_visible_trees += 1

print(f"Number of visible trees: {number_of_visible_trees}")

## PART 2

inside_tree_map = []
visible_trees = {} # {(row, col): [left, right, top, bottom]}
scenic_scores = []

with open(filename) as map_input:
    tree_map = map_input.read().split("\n")

for i in range(0, len(tree_map)):
    trees = []
    for char in tree_map[i]:
        trees.append(int(char))
    inside_tree_map.append(trees)

for row in range(1, len(inside_tree_map)-1): # row no.
    for col in range(1, len(inside_tree_map[row])-1): # col.
        visible_trees.update({(row, col):[col, 98-col, row, 98-row]})
        scenic_score = 1
        for j in range(col): # check left
            if inside_tree_map[row][j] >= inside_tree_map[row][col]:
                visible_trees[(row, col)][0] = col-j
        for k in range(98, col, -1): # check right
            if inside_tree_map[row][k] >= inside_tree_map[row][col]:
                visible_trees[(row, col)][1] = k-col
        for x in range(row): # check top
            if inside_tree_map[x][col] >= inside_tree_map[row][col]:
                visible_trees[(row, col)][2] = row-x
        for y in range(98, row, -1): # check bottom
            if inside_tree_map[y][col] >= inside_tree_map[row][col]:
                visible_trees[(row, col)][3] = y-row
        for viewing_distance in visible_trees[(row, col)]:
            scenic_score *= viewing_distance
        scenic_scores.append(scenic_score)

print(f"Highest possible scenic score is: {max(scenic_scores)}")