nameHandle = open('kids.py', 'w')

for i in range(2):
    name = input("Enter name: ")
    nameHandle.write(name + '\n')
nameHandle.close()