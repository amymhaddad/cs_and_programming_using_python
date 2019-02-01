import re 

s = 'boboboomobooizobobwizbobbi'


letter_b = 0
letter_o = 0
name = ''

for letter in s:
    if letter == 'b' or letter == "o":
        name += letter


t = 'bobobooobooobobbobb'

bobob = re.findall(r'bobob*', t)
bob = re.findall(r'bob*', t)







# if "bobob" in name:
#     count +=2
#     character_replacer = name.replace("bobob", "")
# # print(character_replacer)
# # if "bob" in character_replacer:
# #     count += 1
# print(count)







# for letter in name:
#     if letter == 'b':
#         letter_b += 1
#     else:
#         letter_o += 1

# print(letter_b)
# print(letter_o)
# # for letter in s:
# #     if letter_b == letter_o:
    







# letter_b = 0
# letter_o = 0
# name = ''

# for letter in s:
#     if letter == 'b' or letter == "o":
#         name += letter

# for letter in name:
#     if letter == 'b':
#         letter_b += 1
#     else:
#         letter_o += 1

# if letter_b >= 2 and letter_o >= 1:
#     if letter_b == letter_o + 1:
#         print(f"Number of times bob occurs is: {letter_o}")
#     elif len(name) == 4:
#         if letter_b == 2 and letter_o == 2:
#             print(f"Number of times bob occurs is: 1")
#     elif letter_o > letter_b:
#         print(f"Number of times bob occurs is: {letter_b - 1}")
# else:
#     print("Number of times bob occurs is: 0")