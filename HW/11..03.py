# Task 1 - Space counter

text = input('Enter text: ')
space_count = 0
for space in text:
    if space == ' ':
        space_count += 1

print(space_count)

# Task 2 - Runner

water = 20
count = 0

while water != 0:
    count += 1
    water -= .5

print(f'Круги: {count}')
