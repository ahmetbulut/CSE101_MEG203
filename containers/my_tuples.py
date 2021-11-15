
# function def with gather operator
def print_all(*args):
    for i in range(len(args)):
        print(args[i])

arguments = (1, 2, "Hello World", 2.50)
indices = [0,1,2,3]
others = 'WXYZ'

#scatter operator
#print_all(*arguments)

for item in zip(arguments, indices, others):
    print(item)



