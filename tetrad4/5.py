import hashlib
import json

json_data = '{"name": "John Doe", "age": 30, "city": "New York"}'

data_dict = json.loads(json_data)

hash_table = {}

for key in data_dict.keys():
    hash_value = hashlib.sha256(key.encode()).hexdigest()

    hash_table[hash_value] = data_dict[key]

print(hash_table)
