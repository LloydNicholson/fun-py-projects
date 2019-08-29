arr1 = [1, 1, 2, 3, 1]
arr2 = [1, 1, 2, 4, 1]
arr3 = [1, 1, 2, 1, 2, 3]

arr4 = ['Hello', 'Goodbye']
for s in arr4:
    print(s)


def array_check(array):
    for i in range(len(array) - 2):
        if array[i] == 1 and array[i + 1] == 2 and array[i + 2] == 3:
            return True
    return False


print(array_check(arr1))


def fix_teen(val):
    if val in [13, 14, 17, 18, 19]:
        return 0
    return val


def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


print(no_teen_sum(15, 9, 2))
