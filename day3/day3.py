## PART 1

filename = "day3.txt"
first_compartment, second_compartment = [], []
items = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
sum_of_priorities = 0

with open(filename) as rucksack_input:
    rucksacks = rucksack_input.read().split("\n")

for i in range(len(rucksacks)):
    half_rucksack = int(len(rucksacks[i])/2)
    first_compartment.append(rucksacks[i][:half_rucksack])
    second_compartment.append(rucksacks[i][half_rucksack:])

    for j in range(len(first_compartment[i])):
        for k in range(len(second_compartment[i])):
            if first_compartment[i][j] == second_compartment[i][k]:
                duplicate = (first_compartment[i][j])
    sum_of_priorities += items.index(duplicate) + 1

print(f"Sum of priorities: {sum_of_priorities}")

## PART 2

sum_of_priorities = 0

for i in range(0, len(rucksacks), 3):
    first_line, second_line, third_line = rucksacks[i], rucksacks[i+1], rucksacks[i+2]
    for x in first_line:
        for y in second_line:
            for z in third_line:
                if x == y == z:
                    duplicate = x
    sum_of_priorities += items.index(duplicate) + 1

print(f"Sum of priorities: {sum_of_priorities}")