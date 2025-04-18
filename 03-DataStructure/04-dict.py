my_dict = {
    "name": "navin",
    "age": 20,
    "city": "bharatpur" 
}

# get: get value of given key, if not present return None (default)
print(my_dict.get("profession", None))  # Output: None

# create views from dictionary data
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])
print(my_dict.values())  # Output: dict_values(['navin', 20, 'bharatpur'])
print(my_dict.items())  # Output: dict_items([('name', 'navin'), ('age', 20), ('city', 'bharatpur')])

# pop: remove given key data and return it, it not found: reuturn second arg passed or raise KeyError
print(my_dict.pop("profession", None))  # Output: None

# popitem: remove last key: value pair
my_dict.popitem()

# setdefault: Returns the value of the specified key. If the key does not exist: insert the key, with the specified value & return it.
print(my_dict.setdefault("gender", "male"))