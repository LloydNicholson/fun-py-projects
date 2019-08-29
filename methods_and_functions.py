import math, string


def vol(rad):
    return (4 / 3 * math.pi) * (rad ** 3)


# print(vol(2))


def ran_bool(num, low, high):
    return low <= num <= high


# print(ran_bool(5, 5, 6))


def up_low(s):
    upper_count = 0
    lower_count = 0
    for i in s:
        if i.isupper():
            upper_count += 1
        elif i.islower():
            lower_count += 1
    return f'Lower count is {lower_count}\nUpper count is {upper_count}'


# string = 'Hello Mr. Rogers, how are you this fine Tuesday?'
# print(up_low(string))


def unique_list(numbers):
    return list(set(numbers))


# print(unique_list([1, 2, 2, 5, 6, 4, 5, 6, 8]))


def multiply(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total


# print(multiply([1, 2, 3, -4]))


def palindrome(s):
    return s == s[::-1]


print(palindrome('madam'))


def ispangram(str1, alphabet=string.ascii_lowercase):
    letters = list(set(str1.lower()))
    return len(letters) == 27


print(ispangram('The quick brown fox jumps over the lazy dog'))

