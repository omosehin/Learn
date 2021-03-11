def lesser_of_two_even(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a > b:
            print(b)
        else:
            print(a)
    elif a % 2 != 0 or b % 2 != 0:
        if a > b:
            print(a)
        else:
            print(b)


lesser_of_two_even(4, 8)


def makes_twenty(n1, n2):
    return n1 + n2 == 20 or n1 == 20 or n2 == 20


def capitalisetext(text):
    result = ''
    for v, m in enumerate(text):
        if v == 0 or v == 3:
            result += text[v].upper()
        else:
            result += text[v]

    return result


def reversestring(text):
    word = text.split()
    reversed_word_list = word[::-1]
    return ' '.join(reversed_word_list)


# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere
def has_33(nums):
    for ll in range(0, len(nums) - 1):
        if nums[ll] == 3 and nums[ll + 1] == 3:
            return True

    return False


def paper_doll(word):
    textin = ''

    for char in word:
        textin += char * 3
    return textin


def blackjack(a, b, c):
    if sum([a, b, c]) <= 21:
        return sum([a, b, c])
    elif 11 in [a, b, c] and sum([a, b, c]) <= 31:
        return sum([a, b, c]) - 10
    else:
        return "BUST"


def sumafter(arr):
    total = 0
    add = True

    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break

    return total


# print(sumAfter([1,3,5]))

def spy_game(arr):
    code = [0, 0, 7, 'x']
    for j in arr:
        if j == code[0]:
            code.pop(0)

    return len(code) == 1


# print('spy',spy_game([1,2,4,5,0,0,9,7]))

def count_primes2(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


def square(num):
    return num ** 2


my_nums = [1, 2, 4, 5, 8]
for ii in map(square, my_nums):
    print('square root', ii)

list_data = list(map(square, my_nums))


# print(list_data)

def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return mystring[0]


names = ['andy', 'Eve', 'Sally']
map_result = list(map(splicer, names))
print('slit', map_result)


def check_even(num):
    return num % 2 == 0


mynnums = [1, 2, 3, 4, 5, 6]

myresult = list(filter(check_even, mynnums))
print('myresult', myresult)

for k in filter(check_even, mynnums):
    print(k)

squarelamda = lambda num: num ** 2
print('lambda', squarelamda(3))

print('hello', list(map(lambda num: num * 4, mynnums)))

print('get first letter',list(map(lambda v: v[0], names)))
print('lambda example',list(map(lambda g:g[::-1],names)))
