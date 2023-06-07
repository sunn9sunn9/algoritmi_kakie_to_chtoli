def find_two_sum(arr: list[int], target: int):
    hash_table = {}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in hash_table:
            return [hash_table[diff], i]
        else:
            hash_table[num] = i
    return None


arr_num = [-1, 2, 3, 4, 7]
target_num = 5
result = find_two_sum(arr_num, target_num)
print(result)
