## PART 1

filename = "day6.txt"

with open(filename) as datastream_input:
    datastream = datastream_input.read()

for i in range(len(datastream)-3):
    four_chars = datastream[i:i+4]
    counter = 4
    duplicates = []
    for j in range(len(four_chars)):
        for x in range(1, counter):
            if four_chars[j] != four_chars[-counter + x]:
                duplicates.append(False)
            else:
                duplicates.append(True)
        counter -= 1
    if sum(duplicates) == 0:
        marker = i+4
        break

print(f"Number of characters to process: {marker}")

## PART 2

for i in range(len(datastream)-13):
    fourteen_chars = datastream[i:i+14]
    counter = 14
    duplicates = []
    for j in range(len(fourteen_chars)):
        for x in range(1, counter):
            if fourteen_chars[j] != fourteen_chars[-counter + x]:
                duplicates.append(False)
            else:
                duplicates.append(True)
        counter -= 1
    if sum(duplicates) == 0:
        marker = i+14
        break

print(f"Number of characters to process: {marker}")
