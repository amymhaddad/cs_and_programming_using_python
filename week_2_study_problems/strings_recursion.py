import string

LOWER_LETTERS = string.ascii_lowercase

def isPalindrome(string):
    
    def normalize_string(string):
        string = string.lower()
        ans = ''
        for letter in string:
            if letter in LOWER_LETTERS:
                ans += letter
        return ans

    def isPal(string):
        if len(string) <= 1:
            return True
        else:
            #string[0] == string[-1] does work to reduce the problem 
            return string[0] == string[-1] and isPal(string[1:-1])
    
    #this is the call for isPal
    return isPal(normalize_string(string))

print(isPalindrome('Able was I, eve I saw Elba'))