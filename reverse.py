# reverse numbers in python


def reverse_number(n: int):
    if str(n).startswith("-"):
        _num = abs(n)  # to make the number positive
        return int(f"-{str(_num)[::-1]}")
    return int(str(n)[::-1])  # if number is already positive


print(reverse_number(1234))
print(reverse_number(-1234))

print(reverse_number(5789))
