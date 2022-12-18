## PART 1

filename = "day1.txt"
total_calories_per_elf = 0
max_calories = 0

with open(filename) as calorie_inputs:
    calories_per_elf = calorie_inputs.read().split("\n\n")

for i in range(len(calories_per_elf)):
    calories_per_elf[i] = calories_per_elf[i].split("\n")
    for j in calories_per_elf[i]:
        total_calories_per_elf += int(j)
    calories_per_elf[i] = total_calories_per_elf
    total_calories_per_elf = 0

for number in range(len(calories_per_elf)):
    if calories_per_elf[number] >= max_calories:
        max_calories = calories_per_elf[number]
        
print(f"Max calories: {max_calories} calories")

## PART 2

total_calories_per_elf = 0
max_calories = 0
second_max_calories = 0
third_max_calories = 0

for number in range(len(calories_per_elf)):
    if calories_per_elf[number] >= max_calories:
        third_max_calories = second_max_calories
        second_max_calories = max_calories
        max_calories = calories_per_elf[number]
    elif calories_per_elf[number] >= second_max_calories:
        third_max_calories = second_max_calories
        second_max_calories = calories_per_elf[number]
    elif calories_per_elf[number] >= third_max_calories:
        third_max_calories = calories_per_elf[number]
        
print(f"Sum of top three elves with most calories: {max_calories + second_max_calories + third_max_calories} calories")