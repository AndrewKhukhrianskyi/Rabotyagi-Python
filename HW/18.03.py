# Task 1: https://www.codewars.com/kata/56530b444e831334c0000020
def solve_task(sperm):
    if sperm[-1] == 'Y':
        children = 'son'
    else:
        children = 'daughter'
    return f"Congratulations! You're going to have a {children}." # вшиваем параметр в текст

print(solve_task('XY'))
print(solve_task('XX'))