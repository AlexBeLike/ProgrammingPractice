import math


def find_intersections(x1, y1, r1, x2, y2, r2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    if distance == 0 and r1 == r2:
        return -1

    if distance > r1 + r2 or distance < abs(r1 - r2):
        return 0

    if distance == r1 + r2 or distance == abs(r1 - r2):
        return 1

    return 2


while True:
    try:
        variables = list(map(int, input("x1 y1 r1 x2 y2 r2\n").split()))
        if variables.__len__() > 6:
            print("Too many values, please try again...")
            continue
        x1 = variables[0]
        y1 = variables[1]
        r1 = variables[2]

        x2 = variables[3]
        y2 = variables[4]
        r2 = variables[5]

        print(find_intersections(x1, y1, r1, x2, y2, r2))
        repeat = input("Want to try again? (y/n): ").lower()

        if repeat == 'y':
            continue
        exit()
    except ValueError:
        print("You should write values not symbols...")
        continue
        