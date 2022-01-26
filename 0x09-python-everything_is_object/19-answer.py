#!/usr/bin/python3

"""module that contain function copy_list
it return a copy of a list"""


def copy_list(l):
    copy_list = l[:]
    return copy_list



my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)