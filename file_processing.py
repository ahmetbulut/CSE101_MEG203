# from containers.my_tuples import print_all

# demonstration of reading and writing to files.

f = open("data/names.txt", "r") # open for reading

# for line in f.readlines():
#     print(line.strip("\n"))
#wf = open("data/replica.txt", "w")

with open("data/archive/replica.txt", "w") as wf: # open for writing
    for line in f.readlines():
        wf.write(line)

# flush anything in OS buffers, make sure that file is sealed!
# wf.close()

try:
    filename = "data/namesXYZ.txt"
    fE = open(filename, "r") # does not exist
except FileNotFoundError:
    # do something more elaborate
    print("Sorry, I do not have the file named %s!" % (filename))


pi = 3.142423423489
print("The value of %.2f" % pi)
