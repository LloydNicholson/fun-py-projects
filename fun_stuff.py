import caesar_cipher2 as cc

# import math
#
# num = 6
# numSqrt = math.sqrt(num)
# print(numSqrt)
# numSqr = num ** 2
# print(numSqr)
#
# string1 = 'hello'
# newStr = string1[::-1]
# print(newStr)
# letter = newStr[0]
# print(letter)
#
# newList = list([0, 0, 0])
# print(newList)
# newList = [0, 0, 0]
# print(newList)
#
# # Getting a little tricker
# d = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
#
# val = d['k1'][0]['nest_key'][1][0]
# print(val)
#
# # This will be hard and annoying!
# newD = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}
#
# val1 = newD['k1'][2]['k2'][1]['tough'][2][0]
# print(val1)
#
# t = tuple(range(1, 4, 1))
# print(t)
#
# s = {1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2}
# # s.remove(4)
# print(s)
#
# print(not 3 >= 3)
#
# print(2651 % 53)
#
#
# def polynomial(x, y):
#     return x ** 2 + 5 * y + 4
#
#
# print(polynomial(4, 6))
#
# lamb = (lambda x: x ** 3 + 5 * x + 4)
# print(lamb(7))
#
# aList = [1, 2, 3, 4, 5]
# bList = list(map(lamb, aList))
# print(bList)

word = 'chillies'
for l, i in enumerate(word):
    print(l, i)

myOtherList = [x for x in range(0, 11) if x % 2 == 0]
print(myOtherList)

celcius = [0, 10, 20, 30, 40]
fahrenheit = [(9 / 5 * temp + 32) for temp in celcius]

print(fahrenheit)

compList = [a for a in range(1, 51) if a % 3 == 0]
print(compList)

stringOfWords = 'Print every word in this sentence that has an even number of letters'
words = stringOfWords.split()
for w in words:
    # if w.startswith('s'):
    #     print(w)
    if len(w) % 2 == 0:
        print(w + ' is even')

wrd = [word[0] for word in words]
print(wrd)

for x in words:
    print(x[0])

for i in range(1, 51):
    if i % 5 == 0 and i % 3 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

encString = cc.encrypt('A string of words', 4)
print(encString)


def pig_latin(currentword):
    first_letter = currentword[0]
    if first_letter in 'aeiou':
        pig_word = currentword + 'ay'
        return pig_word
    else:
        pig_word = currentword[1:] + first_letter + 'ay'
    return pig_word


print(pig_latin('apple'))

sentenceArr = 'Hello dude let\'s try this out and see what happens with some pig-latin'.split()
newSentence = ''
for word in sentenceArr:
    newSentence += pig_latin(word) + ' '

print(newSentence)


# # args use-case
# def func(*args):
#     print(args)
#     return sum(args) * 0.1
#
#
# print(func(40, 50, 70, 20, 90, 100))


# kwargs use-case (keyword-args)
def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('No fruit here!')


myfunc(fruit='apple', veggie='lettuce')


def mynewfunc(string):
    newstrlist = []
    for index, s in enumerate(string):
        if index % 2 == 0:
            newstrlist.insert(index, s.upper())
        else:
            newstrlist.insert(index, s.lower())
    return ''.join(newstrlist)


print(mynewfunc('Supercalafragilistic'))


def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        # return a if a < b else b
        return min(a, b)
    else:
        # return b if b > a else a
        return max(a, b)


print(lesser_of_two_evens(6, 8))


def makes_twenty(n1, n2):
    return (n1 + n2 == 20) or n1 == 20 or n2 == 20


print(makes_twenty(10, 1))


def oldmacdonald(text):
    first_half = text[:3]
    second_half = text[3:]

    return first_half.capitalize() + second_half.capitalize()


print(oldmacdonald('macdonald'))


# reverse the word order
def master_yoda(text):
    tempWords = text.split()
    tempWords.reverse()
    return ' '.join(tempWords)


print(master_yoda('I am Good'))


def has_33(nums):
    for it in range(0, len(nums) - 1):
        # if nums[it:i+2] == [3, 3]:
        if nums[it] == 3 and nums[it + 1] == 3:
            return True
    return False
    # found = 0
    # for num in nums:
    #     if num == 3:
    #         found += 1
    #     else:
    #         found = 0
    #     if found == 2:
    #         return True
    # return False


print(has_33([3, 9, 5, 5]))


def paper_doll(text):
    listtext = [s * 3 for s in text]
    return ''.join(listtext)


print(paper_doll('Hello there'))


def blackjack(a, b, c):
    # sumofcards = sum(args)
    sumofcards = sum([a + b + c])
    if sumofcards <= 21:
        return sumofcards
    # elif sumofcards > 21 and (11 in args):
    #     sumofcards -= 10
    #     if sumofcards > 21:
    #         return 'BUST'
    #     return sumofcards
    elif sumofcards <= 31 and 11 in [a, b, c]:
        return sumofcards - 10
    else:
        return 'BUST'


# print(blackjack(4, 2, 5, 3, 4, 11, 11))
print(blackjack(9, 10, 7))


def count_primes(num):
    counter = 0
    for n in range(2, num + 1):
        if num % n == 0:
            counter += 1
    return counter


print(count_primes(100))


def print_big(letter):
    patterns = {'a': ['   *    ', '  *  *  ', '  ****  ', '  *  *  ', '  *  *  ']}
    for key, val in patterns.items():
        print("\n".join(val))


print_big('a')


def hello(name='Lloyd'):
    print('This hello() function has been run')

    def greet():
        return 'This string is inside greet'

    def welcome():
        return 'This string is inside welcome'

    if name == 'Lloyd':
        return greet
    else:
        return welcome


# x = hello()


def new_decorator(func):
    def wrap_func():
        print('Code here before executing func')
        func()
        print('Func has been called')

    return wrap_func


@new_decorator
def func_needs_decorator():
    print('This function is in need of a decorator')


func_needs_decorator()
