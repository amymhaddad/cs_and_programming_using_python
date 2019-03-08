

animals = {
    'a': ['aardvark'],
    'b': ['baboon'],
    'c': ['coati'],
    'd': ['donkey', 'dog', 'dingo'],
}

def how_many(aDict):
    count = 0 
    for anim in animals:
        len_values = len(animals[anim])
        count += len_values
    return count

print(how_many(animals))
