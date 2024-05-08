# Test data:
# sl_num = [1, 1]
# sl_num = []
# sl_num = [10, 20, 30, 40, 50]
# sl_num = [1, 1, 1, 1, 1]


sl_num = [1, 2, 3, 4, 5]
if (len(sl_num) < 2) or (len(sl_num) >= 2 and sl_num[0] == sl_num[1]):
    print(None)

else:
    dupl_items = set()
    uniq_items = []

    for x in sl_num:
        if x not in dupl_items:
            uniq_items.append(x)
            dupl_items.add(x)
    uniq_items.sort()

    print(uniq_items[-2])

