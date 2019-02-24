

def a(x, y, z):
     if x:
         return y
     else:
         return z

a(False, 2, 3)
##Walk through answer, which is 3
#When run the program in VSC I get nothing, why?

def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(q, r):
    return a(q>r, q, r)
a(3>2, a, b)
#Why answer is "function"




count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))


greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)

print('done')

iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 



#Let's walk through why I get an assignment error with the first set of code and not the second:
#Is it bc I'm not assigning anything in the second one?
def h(y):
    x = x + 1

x = 5
h(x)
print(x)

def g(y):
    print(x)
    print(x + 1)

x = 5
g(x)
print(x)

