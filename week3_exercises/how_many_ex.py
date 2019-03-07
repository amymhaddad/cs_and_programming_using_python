

animals = {
    'a': ['aardvark'],
    'b': ['baboon'],
    'c': ['coati'],
    'd': ['donkey', 'dog', 'dingo'],
}

count = 0 
for anim in animals:
    len_values = len(animals[anim])
    print(len_values)
    count += len_values
return count
