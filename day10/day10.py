## PART 1

def get_signal_strength(cycle, value):
    if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
        print(f"cycle: {cycle}, value: {value}, signal strength: {cycle * value}")
        return cycle*value
    else:
        return 0

filename = "day10.txt"
cycle = 0
value = 1
signal_strength = 0

with open(filename) as program_input:
    program_instructions = program_input.read().split("\n")

for i in range(len(program_instructions)):
    if program_instructions[i] == 'noop':
        cycle += 1
        signal_strength += get_signal_strength(cycle, value)
    elif program_instructions[i][0:4] == 'addx':
        cycle += 1
        signal_strength += get_signal_strength(cycle, value)
        cycle += 1
        signal_strength += get_signal_strength(cycle, value)
        value += int(program_instructions[i][5:])

print(f"Signal strength: {signal_strength}")

## PART 2

def create_CRT(rows, cols): # 40 wide 6 tall
    crt = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append('.')
        crt.append(row)
    return crt

def create_sprite_position(number):
    sprite = []
    for i in range(3):
        sprite.append('#')
    for j in range(3, number):
        sprite.append('.')
    return sprite

def draw_crt(crt_screen, cycle, sprite_position, value, program_instructions):
    crt_screen[(cycle-1)//40][(cycle-1)%40] = sprite_position[(cycle-1)%40]
    for j in range(len(sprite_position)):
        if sprite_position[j] == '#':
            sprite_position[j] = '.'
    for k in range(value-1, value+2):
        sprite_position[k] = '#'

crt_screen = create_CRT(6, 40)
sprite_position = create_sprite_position(40)

cycle = 0
value = 1

for i in range(len(program_instructions)):
    if program_instructions[i] == 'noop':
        cycle += 1
        value += 0
        draw_crt(crt_screen, cycle, sprite_position, value, program_instructions)

    elif program_instructions[i][0:4] == 'addx':
        cycle += 1
        value += 0
        draw_crt(crt_screen, cycle, sprite_position, value, program_instructions)

        cycle += 1
        value += int(program_instructions[i][5:])
        draw_crt(crt_screen, cycle, sprite_position, value, program_instructions)

for x in crt_screen:
    print(x)
