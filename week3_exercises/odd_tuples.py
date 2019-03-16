
aTup = ('I', 'am', 'a', 'test', 'tuple')

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    new_tup = ()
    for i, element in enumerate(aTup):
        if i == 0 or i % 2 == 0:
            new_tup += (element,)
    
    return new_tup


print(oddTuples(aTup))

# ('I', 'a', 'tuple')

# aTup = ('I', 'am', 'a', 'test', 'tuple')

# new_tup = ()

# def get_data(aTuple):
#     nums = ()
#     words = ()

#     for t in aTuple:
#         nums += (t[0],)
#         words += (t[1],)