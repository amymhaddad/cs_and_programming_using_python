

x = 'azcbobobegghakl'

count = 0

for i, letter in enumerate(x):
    if x[i:i+3] == 'bob':
        count += 1
    
print(count)


