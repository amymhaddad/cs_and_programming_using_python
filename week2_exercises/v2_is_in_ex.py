
char = 'r'
aStr = 'abctz'


def isIn(char, aStr):
        low = 0
        high = len(aStr) - 1
        mid = (low + high) // 2

        if len(aStr) == 1 and char != aStr[mid]:
                return False
        elif char == aStr[mid]:
                return True        
        
        else: 
                if aStr[mid] > char:
                        high = mid
        
                else:
                        low = mid
                return isIn(char, aStr[low:high])
        
print(isIn(char, aStr))

#Think: when will string contain the letter?
#At some point we will have exhausted our options and the string will be size 1 and not = to test character. Therefore, return False

#I originaly recalled mid, but I don't need to do that because it's set as a local variable.


#Divide into 3 subproblems: 
#Test1: if char != mid and len(aStr) == 1 --->return F
#Test2: if char==aStr[mid] ---> return T
#Test2: Recursively calling a smaller problem