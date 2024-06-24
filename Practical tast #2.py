def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def lcm_of_list(numbers):
    n = len(numbers)
    lcm_result = numbers[0]
    for i in range(1, n):
        lcm_result = lcm(lcm_result, numbers[i])
    return lcm_result

while True:
    p = int(input("Введіть кількість чисел (2-20): "))
    numbers = list(map(int, input(f"Введіть {p} натуральних чисел, розділених пробілом: ").split()))

    if 2 <= p <= 20:
        result = lcm_of_list(numbers)
        print("Найменше спільне кратне:", result)
        repeat = input("Want to try again? (y/n): ")

        if repeat.lower() == 'y':
            continue
        exit()

    else:
        print("Кількість чисел повинна бути від 2 до 20.")
        continue
