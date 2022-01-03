
def element_at(my_list, idx):
    counter = 0

    if idx < 0:
        return None
    if idx > len(my_list):
        return None
    else:
        for i in my_list:
            if counter == idx:
                print(f"Element at index {idx} is {i}")
                print(f"{counter}")
                break
            counter += 1
