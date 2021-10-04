# List indexing

my_list = ['p', 'r', 'o', 'b', 'e']

print(my_list[0])  # p

print(my_list[2])  # o

print(my_list[4]) # e

# Nested List
n_list = ["Happy", [2, 0, 1, 5]]

# Nested indexing
print(n_list[0][1])

print(n_list[1][3])

# Error! Only integer can be used for indexing
print(my_list[4.0])