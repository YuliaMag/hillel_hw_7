def second_largest(sl_num):
    if (len(sl_num) < 2) or (len(sl_num) >= 2 and all(i == sl_num[0] for i in sl_num)):
        return None

    else:
        dupl_items = set()
        uniq_items = []

        for x in sl_num:
            if x not in dupl_items:
                uniq_items.append(x)
                dupl_items.add(x)
        uniq_items.sort()

        return uniq_items[-2]


print(second_largest([1, 2, 3, 4, 4])) # expected: 3
print(second_largest([1, 1, 1, 0, 0, 0, 2, -2, -2])) # expected: 1
print(second_largest([3, 2, 1, 0, -1, -2, -3])) # expected: 2
print(second_largest([2, -2])) # expected: -2
print(second_largest([1])) # expected: None
print(second_largest([])) # expected: None
print(second_largest([1, 1])) # expected: None
print(second_largest([4, 6, 1, 3, 2, 0, 2])) # expected: 4
print(second_largest([1, 2, 3, 4, 5])) # expected: 4
print(second_largest([5, 4, 3, 2, 1])) # expected: 4
print(second_largest([1, 1, 1, 1, 1, 1, 1])) # expected: None
print(second_largest([-1, -1, -1, -1, -1, -1, -1])) # expected: None
print(second_largest([300, 1000, -4, 2, -501, 999, 0, -215, 0])) # expected: 999

