

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
    return reversed_word_list
    

print(reverseString('hello adeoye'))
