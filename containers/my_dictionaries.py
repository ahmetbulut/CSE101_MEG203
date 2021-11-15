def contents(d):
    return (d.keys(), d.values())

def look_up(key):
    if key in d:
        print(d[key])
    else:
        print(key, "is not in this dictionary!")


d = {"ahmet": 90, "veli": 50, "barbie": 48, "joe": 11}


#print(d.values())
#print(d.keys())

for item in d.items():
    print(item)


# dictionary look-up
key = "ece"
#look_up(key)

#{}: empty dictionarry

l = list(d.items())
#print_my_list(l)

d_new = dict()
print(contents(d_new))

d_new["one"] = "uno"
d_new["two"] = "duo"
d_new["three"] = "tres"

print(contents(d_new))