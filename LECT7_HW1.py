# def lst2dict():
#     lst = input("Enter the list: ")
#     lst1 = lst[::2]
#     lst2 = lst[1::2]
#     zip_ = zip(lst1, lst2)
#     return dict(zip_)
#
#
# answ = lst2dict()
# print(answ)

def lst2dict(lst):
    lst1 = lst[::2]
    lst2 = lst[1::2]
    zip_ = zip(lst1, lst2)
    return dict(zip_)


lst = input("Enter the list: ")
lst2dict(lst)
print(lst2dict(lst))




