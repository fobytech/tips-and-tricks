# simple python programe to count vowels


def count_vowels(sentence: str):  # using type annotations :)
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for i in list(str(sentence.strip())):
        if i in vowels:
            count += 1
    return count


print(count_vowels("happy coding"))  # expecting 3 vowels
print(count_vowels("python is awesome"))  # expecting 6 vowels

#  Thanks for watching, like and subscribe for more...
