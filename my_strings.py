fruit = 'banana'

# print("the first letter", fruit[0])
# print("the last letter", fruit[-1])
#
# print("the length of the string", len(fruit))
# print("the last letter", fruit[len(fruit)-1])

print("1. while loop example!")
index = 0
while index < len(fruit):
    print("condition is true because", index, "<",len(fruit))
    print(fruit[index])
    index = index + 1

print("condition is false because", index, "is not <",len(fruit))

print("2. for loop example!")
sequence = fruit
for item in sequence:
    print(item)

#index  012345678910
name = "Ahmet Bulut"
print(name[4:7])

# name = "İnci Bulut"
# print(name)
# print(name[0])
#
# name[0] = "I"


def search(letter, sequence):
    index = 0
    length_of_sequence = len(sequence)
    found = False
    while index < length_of_sequence:
        if sequence[index] == letter:
            print("Aha, I found", letter, "at index", index)
            found = True
            break

        index = index + 1

    if not found:
        print("I could not find", letter, "in", sequence)

search("X", "Hello World!")