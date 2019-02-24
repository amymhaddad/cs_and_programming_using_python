
# #Solved problem using enumerate
# x = 'azcbobobegghakl'

# count = 0

# for i, letter in enumerate(x):
#     if x[i:i+3] == 'bob':
#         count += 1
    
# print(count)


# #Solved problem using for loop
s = 'azcbobobegghakl'

count = 0

for i in range(len(s)):
    if s[i:i+3] == 'bob':
        count += 1
print("Number of times bob occurs is: {}".format(count))


#Solved problem using while loop
# s = 'bobcbobbmjnbboobobobobkbobobobm'

# s_len = len(s)
# count = 0
# i = 0
    
# while i < s_len:
#     for i in range(s_len):
#         if s[i:i+3] == 'bob':
#             count += 1
#             i += 1
#     if i == s_len - 1:
#         break
# print("Number of times bob occurs is: {}".format(count))
