# iteration = 0
# count = 0

# while iteration < 5:
#     for letter in "hello, world":
#         count += 1
#     print("Iteration " + str(iteration) + "; count is " + str(count))
#     iteration += 1

count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        #how does it know to add 12 to count?
        count += 1
        index += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))

