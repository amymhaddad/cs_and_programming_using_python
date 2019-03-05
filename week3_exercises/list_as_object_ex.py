
#get absolute value to each element in given function, applyToEach
def applyToEach(L, f):
    new_list = []
    for i in range(len(L)):
        L[i] = f(L[i])
        new_list.append(L[i])
    return new_list

def abs_val(x):
    return abs(x)

testList = [1, -4, 8, -9]
print(applyToEach(testList, abs_val))


#increment each element in given function, applyToEach
def applyToEach(L, f):
    new_list = []
    for i in range(len(L)):
        L[i] = f(L[i])
       
        new_list.append(L[i])
    return new_list

def one(a):
    return a + 1

testList = [1, -4, 8, -9]
print(applyToEach(testList, one))


# #square each element in given function, applytToEach
def applyToEach(L, f):
    new_list = []
    for i in range(len(L)):
        L[i] = f(L[i])
       
        new_list.append(L[i])
    return new_list

def sq(x):
    return x ** 2

testList = [1, -4, 8, -9]
print(applyToEach(testList, sq))
