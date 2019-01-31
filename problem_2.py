# s = 'azcbobobegghakl'

# count = 0
# name = ''

# for letter in s:
#     if letter == 'b' or letter == "o":
#         name += letter
    

x = 'bobobob'
bob = ''

# for letter in x[0:3]:
#     bob += letter

# print(bob)

count = 0
for letter in x:
    if letter == 'b':
        count += 1
if count % 2 != 0:
    count -= 1
# else:
#     if count % 2 == 0:
#         print(count)

print(count)



        
        
##Need to re-use middle term IF there's an odd number of b's 
        
            
