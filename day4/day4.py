## PART 1

filename = "day4.txt"
number_of_pairs = 0

with open(filename) as cleanup_input:
    pair_cleanup = cleanup_input.read().split("\n")

for i in range(len(pair_cleanup)):
    pair_cleanup[i] = pair_cleanup[i].split(",")
    first_range = pair_cleanup[i][0].split("-")
    second_range = pair_cleanup[i][1].split("-")

    if int(first_range[0]) <= int(second_range[0]) and int(first_range[1]) >= int(second_range[1]):
        number_of_pairs += 1
    
    elif int(second_range[0]) <= int(first_range[0]) and int(second_range[1]) >= int(first_range[1]):
        number_of_pairs += 1

print(f"Number of pairs that contain the other: {number_of_pairs}")

## PART 2

number_of_pairs = 0

for i in range(len(pair_cleanup)):
    first_range = pair_cleanup[i][0].split("-")
    second_range = pair_cleanup[i][1].split("-")

    if int(second_range[0]) <= int(first_range[1]) <= int(second_range[1]) or int(first_range[0]) <= int(second_range[1]) <= int(first_range[1]):
        number_of_pairs += 1

    elif int(first_range[0]) <= int(second_range[0]) and int(first_range[1]) >= int(second_range[1]):
        number_of_pairs += 1
    
    elif int(second_range[0]) <= int(first_range[0]) and int(second_range[1]) >= int(first_range[1]):
        number_of_pairs += 1

print(f"Number of pairs that overlap: {number_of_pairs}")