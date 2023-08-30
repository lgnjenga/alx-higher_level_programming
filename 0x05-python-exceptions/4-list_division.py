#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            value = 0

            if i < len(my_list_1) and i < len(my_list_2):
                if isinstance(my_list_1[i], (int, float)):
                    if isinstance(my_list_2[i], (int, float)):
                        if my_list_2[i] != 0:
                            value = my_list_1[i] / my_list_2[i]
                        else:
                            print("division by 0")
                    else:
                        print("wrong type")
                else:
                    print("wrong type")
            else:
                print("out of range")
        except ZeroDivisionError:
            value = 0
        finally:
            result.append(value)

    return result


if __name__ == "__main__":
    my_l_1 = [10, 8, 4]
    my_l_2 = [2, 4, 4]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

    print("--")

    my_l_1 = [10, 8, 4, 4]
    my_l_2 = [2, 0, "H", 2, 7]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)
