numberOfGuests = 3

while True:
    t1 = int(input("Введіть час (годин) за який гість 1 з'їсть пиріг: "))
    t2 = int(input("Введіть час (годин) за який гість 2 з'їсть пиріг: "))
    t3 = int(input("Введіть час (годин) за який гість 3 з'їсть пиріг: "))

    if (t1 > 10000 or t1 <= 0) or (t2 > 10000 or t2 <= 0) or (t3 > 10000 or t3 <= 0):
        print("Invalid value, please try again...")
        continue

    timeForEat = ((t1 + t2 + t3) / 3) / numberOfGuests

    print(f"Час, необхідний для з'їдання пирога: {round(timeForEat, 2)} годин")

    repeat = input("Want to try again? (y/n): ")

    if repeat.lower() == 'y':
        continue
    print("Goodbye")
    exit()
