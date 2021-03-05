

def lesser_of_two_even(a,b):
    if a%2 ==0 and b%2==0:
        if a>b:
            print(b)
        else: print(a)
    elif  a%2 !=0 or b%2 !=0:
        if a>b:
            print(a)
        else: print(b)  

lesser_of_two_even(4,8)

def makes_twenty(n1,n2):
    return n1+n2==20 or n1 == 20 or n2 ==20

print(makes_twenty(21,20))

def capitaliseText(text):
    result = ''
    for v,i in enumerate(text):
        if v == 0 or v==3:
            result+=  text[v].upper()
        else:
            result+= text[v]
    
    return result


print(capitaliseText('macdonald'))

def reverseString(text):
    word = text.split()
    reversed_word_list=word[::-1]
    return ' '.join(reversed_word_list)
    

print(reverseString('hello adeoye'))

#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere
def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
          
    return False

print ('result',has_33([3,2,1,3,1,3,3]))

def paper_doll(word):
    textin =''

    for char in word:
        textin += char*3
    return textin

print("triplword",paper_doll('hello'))

def blackjack(a,b,c):
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) <=31:
        return sum([a,b,c]) - 10
    else:
        return "BUST"

print(blackjack(3,20,1))

def sumAfter(arr):
    
    total = 0
    add = True

    for num in arr:
        while add:
            if num!= 6:
                total +=num
                break
            else:
                add = False
        while not add:
            if  num!=9:
                break
            else:
                add = True
                break

    return total

print(sumAfter([1,3,5]))

def spy_game(arr):
    code = [0,0,7,'x']
    for j in arr:
        if j == code[0]:
            code.pop(0)

    return len(code) == 1   

print('spy',spy_game([1,2,4,5,0,0,9,7]))      
