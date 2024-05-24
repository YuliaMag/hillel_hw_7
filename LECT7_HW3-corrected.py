def second_largest(numbers):
    if len(numbers) < 2 or len(set(numbers)) == 1:
        return None

    largest = sec_largest = float('-inf')

    for num in numbers:
        if num > largest:
            sec_largest = largest
            largest = num
        elif num > sec_largest and num != largest:
            sec_largest = num

    if sec_largest == float('-inf'):
        return None
    else:
        return sec_largest


print(second_largest([1, 2, 3, 4, 4]))  # expected: 3
print(second_largest([1, 1, 1, 0, 0, 0, 2, -2, -2]))  # expected: 1
print(second_largest([3, 2, 1, 0, -1, -2, -3]))  # expected: 2
print(second_largest([2, -2]))  # expected: -2
print(second_largest([1]))  # expected: None
print(second_largest([]))  # expected: None
print(second_largest([1, 1]))  # expected: None
print(second_largest([4, 6, 1, 3, 2, 0, 2]))  # expected: 4
print(second_largest([1, 2, 3, 4, 5]))  # expected: 4
print(second_largest([5, 4, 3, 2, 1]))  # expected: 4
print(second_largest([1, 1, 1, 1, 1, 1, 1]))  # expected: None
print(second_largest([-1, -1, -1, -1, -1, -1, -1]))  # expected: None
print(second_largest([300, 1000, -4, 2, -501, 999, 0, -215, 0]))  # expected: 999
