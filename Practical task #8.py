from math import factorial
from collections import Counter


def count_anagrams(word):
    letter_counts = Counter(word)

    total_anagrams = factorial(len(word))

    for count in letter_counts.values():
        if count > 1:
            total_anagrams //= factorial(count)

    return total_anagrams


word = input("Введіть слово: ")
print("Кількість анаграм: ", count_anagrams(word))
