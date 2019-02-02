
#Solved problem using enumerate
# x = 'azcbobobegghakl'

# count = 0

# for i, letter in enumerate(x):
#     if x[i:i+3] == 'bob':
#         count += 1
    
# print(count)

#Solved problem using for loop
x = 'azcbobobegghakl'

x_len = len(x)
count = 0

for i in range(x_len):
    if x[i:i+3] == 'bob':
        count += 1
print(count)



   
    

        





    

