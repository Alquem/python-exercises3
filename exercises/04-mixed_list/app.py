mix = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

# Your code below:
def printing_value_types_of(mix_list):
    for item in mix_list:
        print(type(item))

printing_value_types_of(mix)