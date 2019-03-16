
# word = 'hello'

# def cap(word):
#     if len(word) == 0:
#     # as an alternative: if word == "":
#         return word
#     else:
#         return word[0].title() + cap(word[1:])

# print(cap(word))


# nums = [2, 4, 6]

# def sq_num(nums):
#     if nums == []:
#         return []
#     else:
#         return [nums[0] * nums[0]] + sq_num(nums[1:])

# print(sq_num(nums))

# nums = [1, 2, 3, 4, 5]
# def add_2(nums):
#     if nums == []:
#         return []
#     else:
#         return [nums[0] + 2] + add_2(nums[1:])

# print(add_2(nums))

# def cap(word):
#     if word == '':
#         return ''
#     else:
#         return word[0].title() + cap(word[1:])

# def cap(word):
#     new_word = ''
#     for letter in word:
#         new_word += letter.title()
#     return new_word

# print(cap(word))


# nums = [2, 4, 6]

# def total(nums):
#     if nums == []:
#         return 0
#     else:
#         return nums[0] + total(nums[1:])
# print(total(nums))

# def total(nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total
# print(total(nums))


nums = [2, 4, 6]
def quad_nums(nums):
    if nums == []:
        return 0
    else:
        return nums[0] * 4 + quad_nums(nums[1:])

print(quad_nums(nums))



string = 'i Have a pablo in my life'

def swap_first_letter(string):
    #want to catch base case early -- before i split the string into a list and make the program more complex
    if string == "":
        return ""

    string_in_list = string.split(" ")
    
    if string_in_list[0][0].islower():
        #Use .title() or .capitalize() b/c only changing first element, but want to keep the rest
        updated_string = string_in_list[0].title()
    elif string_in_list[0][0].isupper():
        updated_string = string_in_list[0].lower() 

    #use var called 'but_first_string' to indicate that you want everthing but the first item
    but_first_string = " ".join(string_in_list[1:])
    return updated_string + ' ' + swap_first_letter(but_first_string)

print(swap_first_letter(string))













# nums = [1, 2, 3, 4, 5]

# def add_2(nums):
#     if nums == []:
#         #base case also needs to be inside a list b/c the list is now empty and looks like this: [3, 4, 5, 6, 7] + []
#         return []
#     else:
#         return [nums[0]+2] + add_2(nums[1:])

# print(add_2(nums))


