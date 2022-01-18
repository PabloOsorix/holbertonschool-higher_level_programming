#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    list_result = []
    x = 0


    for x in range(list_length):
        try:
            list_result.append(my_list_1[x] / my_list_2[x])
        except ZeroDivisionError:
            print("division by 0")
            list_result.append(0)
        except IndexError:
            print("out of range")
            list_result.append(0)
        except TypeError:
            print("wrong type")
            list_result.append(0)
        finally:
            pass
    return list_result
