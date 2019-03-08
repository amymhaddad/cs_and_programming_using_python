
animals = { 
    'a': ['aardvark'], 
    'b': ['baboon', 'coati', 'coati', 'coati', 'coati'], 
    'c': ['coati', 'coati', 'coati', 'coati'],
    }

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

aDict = {
    'a': [], 
    'b': [1, 7, 5, 4, 3, 18, 10, 0],
    }


def biggest(aDict):
    list_of_value_lengths = [len(val) for val in aDict.values()]
    max_val_length = max(list_of_value_lengths)
    
    no_values_counter = 0
    many_values = []
    for letter in aDict.keys():
        if max_val_length == 0:
            return None
        else:
            if len(aDict[letter]) == max_val_length:
                many_values.append(letter)
    return many_values[0]

print(biggest(aDict))
