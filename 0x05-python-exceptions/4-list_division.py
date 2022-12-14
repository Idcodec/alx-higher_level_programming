#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    for i in range(0, list_length):
        try:
            div_list.append(my_list_1[i] / my_list_2[i])
        except IndexError:
            div_list.append(0)
            print("out of range")
            continue
        except ZeroDivisionError:
            div_list.append(0)
            print("division by 0")
            continue
        except TypeError:
            div_list.append(0)
            print("wrong type")
            continue
        finally:
            pass

    return div_list
