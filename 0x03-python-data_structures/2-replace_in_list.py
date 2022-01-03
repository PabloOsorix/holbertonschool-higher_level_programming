def replace_in_list(my_list, idx, element):
    counter = 0

    if 0 < idx < len(my_list):
        for i in range(len(my_list)):
            if counter == idx:
                my_list[i] = element
            counter += 1
        return my_list
    else:
        return my_list
