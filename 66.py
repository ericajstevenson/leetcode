def plusOne1(digits):

    for i in range(len(digits)-1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
    return [1] + digits


def plusOne2(digits):
    # convert list to int
    num = int(''.join(map(str, digits)))
    # add 1 and convert back to list, return
    return [int(x) for x in str(num+1)]
    # could also nest the two list comprehensions



print(plusOne([9,9]))