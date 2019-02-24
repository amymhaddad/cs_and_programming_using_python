
#Update word from 'hello' to 'hheelllloo'
word = 'hello'

def double_letter(word):
    if word == '':
        return ''
    else:
        return word[0]*2 + double_letter(word[1:])

print(double_letter(word))

#Sum the numbers in a list
list = [2, 4, 6]

def sum_nums(list):
    if list == []:
        return 0
    else:
        return list[0] + sum_nums(list[1:])

print(sum_nums(list))

#Add 2 to each number in a list
#Question: is this the correct return in the base case? Originally, I tried to return 0 and that didn't work b/c can only concatenate lists, not ints.
list = [1, 2, 3, 4, 5]

def add_2(list):
    if list == []:
        return []
    else:
        return [list[0] +2] + add_2(list[1:])

print(add_2(list))


#Swap the case of the first letter in each word
string = 'the Dog is In the Park'

def swap_case_first_letter(string):
    if string == '':
        return ''
    else:
        string_as_list = string.split(' ')
        if string_as_list[0] == string_as_list[0].lower():
            updated_string = string_as_list[0].title()
        elif string_as_list[0] == string_as_list[0].title():
            updated_string = string_as_list[0].lower()
        but_first_string = " ".join(string_as_list[1:])

        return updated_string + " " + swap_case_first_letter(but_first_string)

print(swap_case_first_letter(string))


#Skip the third letter in each word in string using recursion
phrase = 'Ohio State'

def skip_third_letter(phrase):
    if phrase == '':
        return ''
    else:
        phrase_as_list = phrase.split(' ')
        new_phrase = phrase_as_list[0][:2] + phrase_as_list[0][3:]
        updated_phrase = " ".join(phrase_as_list[1:])

        return new_phrase + ' ' + skip_third_letter(updated_phrase)

print(skip_third_letter(phrase))

#Skip the third letter in each word in string using iteration
phrase = 'Ohio State'

new_string = ''
for word in phrase.split(' '):
    for i, letter in enumerate(word):
        if i != 2:
            new_string += letter
    new_string += ' '

print(new_string)

#Find even numbers in a list using recursion
list = [1, 9, 15, 16, 27, 34]

def find_even_nums(list):
    if list == []:
        return []
    else:
        even_nums = []
        if list[0] % 2 == 0:
            even_nums.append(list[0])
        
        return even_nums + find_even_nums(list[1:])

print(find_even_nums(list))


#Find even numbers in list using iteration
list = [1, 9, 15, 16, 27, 34]

even_nums = []
for num in list:
    if num % 2 == 0:
        even_nums.append(num)
print(even_nums)


#Find perfect square in list using recursion
list = [1, 2, 3, 4, 5, 6]
def perfect_sq(list):
    if list == []:
        return []
    else:
        sq = [list[0] * list[0]]
    
    return sq + perfect_sq(list[1:])

print(perfect_sq(list))

#Find perfect sq in list using iteration
list = [1, 2, 3, 4, 5, 6]

sq_nums = []
for num in list:
    sq_nums.append(num * num)
print(sq_nums)    

#Use recurion to get the first number from the list
list = [-6, -8, 0, 1, 3, 8]
len_original_list = len(list)

def find_first_num(numbers):
    if len(numbers) == 0:
        return 0
    else:
        if len(numbers) == len_original_list:
            num = numbers[0]
        else:
            num = 0
        return num + find_first_num(numbers[1:])

print(find_first_num(list))

#Use iteration to get the first number from the list
list = [-6, -8, 0, 1, 3, 8]

for num in list:
    if num == list[0]:
        print(num)


#Square even numbers or cube odd numbers in the list below using recursion 
nums = [1, 2, 3, 4, 5, 6]

def sq_or_cube_num(nums):
    if nums == []:
        return []
    else:
        if nums[0] == 1:
            new_num = nums[0]
        elif nums[0] % 2 == 0:
            new_num = nums[0] * nums[0]
        else:
            new_num = nums[0] ** 3
        return [new_num] + sq_or_cube_num(nums[1:])

print(sq_or_cube_num(nums))

#Square even numbers or cube odd numbers in the list below using iteration
nums = [1, 2, 3, 4, 5, 6]

list_new_nums = []
for num in nums:
    if num == 1:
        new_num = num
    elif num % 2 == 0:
        new_num = num * num
    else:
        new_num = num ** 3
    list_new_nums.append(new_num)
print(list_new_nums)

#Create a new string by taking the first letter of each word in phrase below
phrase = 'We live in Boston'

def abbrev_word(phrase):
    if phrase == '':
        return ''
    else:
        phrase_as_list = phrase.split(" ")
        first_letter = phrase_as_list[0][0].lower()
        but_first_string = " ".join(phrase_as_list[1:])

        return first_letter + abbrev_word(but_first_string)

print(abbrev_word(phrase))

phrase = 'We live in Boston'
new_string = ''

for word in phrase.split(" "):
    first_letter = word[0].lower()
    new_string += first_letter
print(new_string)
       








#### 
#From pairing ex
word = 'Ohio State' # ['Ohio', 'State']

new_string = ''
for word in word.split(' '):
    for letter in word:
        if letter != word[2]:
            new_string += letter
    new_string += " "
print(new_string)

new_string = ''
#Searching through the word list on the outer loop
for word in word.split(' '):
    #inner loop is focused on the letter that make up a word
    for index, letter in enumerate(word):
        if index != 2:
            new_string += letter
    new_string += " "
print(new_string)



def skip_third_letter(words):
    #Passing in a list
    if words == []:
        return ''
    new_word = words[0][0:2] + words[0][3:]
    #returning a string
    return new_word + skip_third_letter(words[1:])

word_list = 'Ohio State'.split(' ')
print(skip_third_letter(word_list))

        


