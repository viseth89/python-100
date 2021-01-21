# i = 1
# tlist = []

# while (i < 20):
#     tlist.append(i)
#     i = i+1
#     print(tlist)


# Second Method - this is the answer from the exercise, 
# Range is a python built in function that generates a range of integers,
# Range creates a range object;
# To get a list you need to use the list() function to convert the range object into a list

my_range = range(1,21)
print(list(my_range))