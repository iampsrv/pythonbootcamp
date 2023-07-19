# dict1 = {"name": "Alice", "age": 25}
# dict2 = {"city": "New York", "country": "USA"}
# merged_dict = {**dict1, **dict2}
# print(merged_dict)


person = {
"name": "Alice",
"age": 25,
"address": {
"street": "123 Main St",
"city": "New York",
"state": "NY"
}
}
street = person["address"]["street"]
print(street)