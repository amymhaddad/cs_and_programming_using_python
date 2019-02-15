
import string
LOWER_LETTERS = string.ascii_lowercase

# char = 'o'

# #remove exttra var's and function calls

# def isIn(char, aStr):
#     def normalize_string(aStr):
#         aStr = string.lower()
#         test_string = ''
#         for letter in aStr:
#             if letter in LOWER_LETTERS:
#                 test_string += letter
#         return test_string

#     def chara_test(aStr):
#         low = aStr[0]
#         high = aStr[-1]
#         test_mid_char = (low + high) // 2

#         # if char not in aStr:
#         #     return False
#         if char == test_mid_char:
#             return True
#         else:
#             return char in test_mid_char
             

# #char may not be in the string
# print(normalize_string('Noise!'))

aStr = 'noise'

sorted_string_as_list = sorted(aStr)
sorted_string = "".join(sorted_string_as_list)

# print(sorted_string)

new_string = ''

# while len(new_string) <= len(aStr):





low = aStr[0]
high = aStr[-1]
index_mid_char = (len(aStr)) // 2
mid_char = aStr[index_mid_char]



    
    # high = mid_char
    # low = aStr[0]
    # print("high", high)
    # print("low", low)



# if char in aStr and char == test_mid_char:
#     print("True")


# #HERE: figure out how to adjust string eval if guess is too high or low
# #Will need to add equation to account for high or low 
# #may have to add = to inequal below
# else:
#     if test_mid_char != char:
#         low = test_mid_char
#     elif test_mid_char > char:
#         high = test_mid_char
#     return 

