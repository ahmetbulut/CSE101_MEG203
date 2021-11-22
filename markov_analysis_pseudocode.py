
# Consume a dataset, and learn language models.
D = {
    'half': {"a": 1, "the": 2, "not":1},
    'a': ...
    'philosophically': ...
    'bee': ...

}

for item in Dataset.readlines():
    valid_keys = line.split([" ", ","]
    for key in valid_keys:
        if key.lower() in D:
            pass
        else:
            #insert into my ...


freqs = {"a": 1.0, "the": 2.0, "not": 1.0}
totalcount = 0.0
for K in freqs:
    totalcount = totalcount + freqs[K]

for K in freqs:
    print("The probability of %s following ... " % K, freqs[K]*1.0/totalcount)

0.2/4.0 --> 0.05
2 * 1.0 / 4 =

"half"  [0.0,1.0] 0.0-0.249 #a
                  0.250-0.499 #not
                  0.50-1.0 #the

    random.random() --> 0.689 --> look_it_up_in_ranges --> emit the corresponding word

#what does the value of totalcount represent?