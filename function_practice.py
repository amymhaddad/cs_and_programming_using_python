

# def printname(first_name, last_name, reverse):
#     if reverse:
#         print(last_name + ',' + first_name)
#     else:
#         print(first_name, last_name)

# printname("Amy", "Haddad", reverse = False)

def foo(x, y = 5):
   def bar(x):
      return x + 1
   return bar(y * 2)
          
print(foo(3))

# print(fun())

# a = 'one'
# b = 'two'

# print(a)

# print(fun())


# def example_fun(x, y, **other):
#     print("x: {0}, y: {1}, keys in 'other':{2}".format(x, y, list(other.keys())))
#     other_total = 0
#     for k in other.keys():
#         other_total = other_total + other[k]
#         print(k)
#     # print("The total of values in 'other' is {0}".format(other_total))

# example_fun(2, y="1", foo=3, bar=4)



# a = 6

# def g(x):
#     def h():
#         x = 'abc'
#     x = x + 1
#     print("In g(x), x =", x)
#     h()
#     return x

# x = 3

# z = g(x)

# def is_even(i):
#     print("hi")
#     return i % 2 == 0

# is_even(3)

# def f(y):
#     y = y + 1
#     print("In f(x), x = ", y)
#     return y

# x = 3
# z = f(x)


# def func_a():
#     print('inside func_a')
# print(func_a())

# def func_b(y):
#     print("inside func_b")
#     return y
# print(5 + func_b(2))

# def func_c(z):
#     print('inside func_c')
#     return z()
# print(func_c(func_a))

# def f(y):
#     x = 1
#     x += 1
#     print(x)

# x = 5
# f(x)
# print(x)

# def g(y):
#     print(y)
#     print(y + 1)

# x = 5
# g(x)
# print(x)

# def h(y):
#     x = x + 1
#     # print('in h(x) x = ', x)
#     # return x
    

# x = 5
# h(x)
# print(x)
# print(x)

# def g(x):
#     def h():
#         x = 'abc'
#     x = x + 1
#     print("in g(x): x = ", x)

#     return x

# x = 3
# z = g(x)

# def h(x):
#     x = x + 1

# x = 5
# h(x)
# print(x)


# def h(y):
#     x = x + 1

# x = 5
# h(x)
# print(x)




# x = 5
# f(x)
# print(x)
#Here, None doesn't print out b/c I'm not printing the function itself

# def g(x):
#     def h():
#         x = 'abc'
#     x = x + 1
#     print('in g(x): x - ', x)
#     h()
#     return x

# x = 3
# z = g(x)
