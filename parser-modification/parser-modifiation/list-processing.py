
def print_list(l):
    for i in l:
        if type(i) is list:
            if(len(i) > 1):
                print(i)
            print_list(i)


print_list(my_list)

