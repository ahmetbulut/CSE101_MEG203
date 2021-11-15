def print_my_list(l):
    for item in l:
        print(item)

movie_titles = ["Everest", "Avatar", "Superman", "Barbie"]

#print("The first item in the sequence", movie_titles[0])
#print("The last item in the sequence", movie_titles[-1])

#print_my_list(movie_titles[1:-1])

movie_titles[-1] = "Barbie Superstar" # updating an individual element

new_movie = 'Purge'
movie_titles.append(new_movie) # list operation example

#print_my_list(movie_titles)

new_list = list("Barbie Superstar")

#print_my_list(new_list)

#print("".join(new_list))


yet_another_one = movie_titles

yet_another_one[0] = 'BOOM!'

#print_my_list(yet_another_one)
#print_my_list(movie_titles)

l_new = list()

l_new.append(2)
l_new.append("Ahmet Bulut")
l_new.append(print_my_list)

#print_my_list(l_new)