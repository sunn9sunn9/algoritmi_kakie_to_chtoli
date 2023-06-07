input_string = "86, 90, 27, 29, 38, 30, 40"

input_list = [int(x) for x in input_string.split(", ")]

hash_table = [None] * 7


def hash_function(x):
    return x % 7


for x in input_list:
    index = hash_function(x)
    if hash_table[index] is None:
        hash_table[index] = x
    else:
        while hash_table[index] is not None:
            index = (index + 1) % 7
        hash_table[index] = x

print(hash_table)
