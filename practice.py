

a = 2
b = 3
def multi(a, b):
    if b == 1:
        return a
    else:
        return a + multi(a, b-1)
print(multi(a, b))




















# # phrase = 'i Have a pablo in my life'

# # #For iterative example, I don't have to specify word[0].title() ---> word.title() is fine. Why? Is this bc it's running through the for loop?

# # phrase_to_list = phrase.split(" ")
# # updated_phase = []

# # for word in phrase_to_list:
# #     if word[0][0].islower():
# #         updated_word = word.title()
# #     elif word[0][0].title():
# #         updated_word = word.lower()
# #     updated_phase.append(updated_word)
# #     but_first_string = " ".join(updated_phase)

# # print(but_first_string)

# # def updated_phase(phrase):
# #     if phrase == '':
# #         return ''
# #     else:
# #         phrase_to_list = phrase.split(" ")

# #         if phrase_to_list[0][0].islower():
# #             updated_word = phrase_to_list[0].title()
# #         elif phrase_to_list[0][0].title():
# #             updated_word = phrase_to_list[0].lower()

# #         joined_phrase = " ".join(phrase_to_list[1:])
# #         return updated_word + ' ' + updated_phase(joined_phrase)

# # print(updated_phase(phrase))