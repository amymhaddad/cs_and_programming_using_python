
t = (2, "one", 3)



def quotient_and_remainder(x, y):
    q = x // y
    r = x % y
    return (q, r)

# (quot, rem) = quotient_and_remainder(4, 5)
# print((quot, rem))
print(quotient_and_remainder(4, 5))


print("hello world")

# print(quotient_and_remainder(4, 5))

# def get_data(aTuple):
#     nums = ()
#     words = ()

#     for t in aTuple:
#         nums = nums + (t[0],)
#         if t[1] not in words:
#             words = words + (t[1],)
#     min_nums = min(nums)
#     max_nums = max(nums)
#     unique_words = len(words)
#     return (min_nums, max_nums, unique_words)

# small, large, words = get_data(((1, 'mine'), 
#                             (3, 'yours'),
#                             (5, 'ours'), 
#                             (7, 'mine')))

# print(words)

# x = 5
# y = 10

# (x, y) = (y, x)



# x = ('a', 'b', 'c')
# y = x[:]

# print(y)