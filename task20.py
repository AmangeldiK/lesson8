list_ = input('Enter number list: ')
list_ = list_.split(',')
def list_num(list_):
    for item in list_:
        if int(item) % 2 != 0:
            print(list_.count(item))
        elif int(item) % 2 == 0:
            print(list_.count(item))
    return list_num


print(list_num(list_))


