
aStr = 'apple'
aStr = "".join(sorted(aStr))
char = 'a'

def isIn(char, aStr):
    low = 0
    high = len(aStr) - 1
    index = (low + high) // 2
    mid_value = aStr[index]

    if char == mid_value:
        return True
    else:
        if mid_value > char:
            high = aStr.index(mid_value)
            print(high)
        elif mid_value < char:
            low = aStr.index(mid_value)
            print(low)
        index = (low + high) // 2

        
        return isIn(char, aStr[low:high])
    #i was sending in an index of 1 character aStr[index], but I need to pass in a string aStr[low:high]
x = isIn(char, aStr)
print(x)