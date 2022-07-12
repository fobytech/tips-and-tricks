#  hello welcome, back...
#  today we gonna create a simple programe to return the highest and lowest number passed to it
# let get going


def high_and_low(number_str: str):
    numbers: list[int] = [int(x) for x in number_str.split()]
    #  using type annotations and list comprehensions :)
    return f"Max is: {max(numbers)}, Min is: {min(numbers)}"


#  alternative method without list comprehension... (beginner frendly : ) )
def high_and_high_alt(number_str: str):
    numbers: list[int] = []
    for x in number_str.split():  # ignore my checker ...
        numbers.append(int(x))
    return f"Max is: {max(numbers)}, Min is: {min(numbers)}"


print(
    high_and_high_alt("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
)  # expecting Max is 42, Min is -9
print(high_and_high_alt("1 2 3 4 5"))  # expecting Max is 5, Min is 1
print(high_and_high_alt("1 2 -3 4 8"))  # expecting Max is 8, Min is -3

#  same result, you can use either method...

#  thanks for watching, like and subscribe for more ...
