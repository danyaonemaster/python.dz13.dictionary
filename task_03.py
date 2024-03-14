def to_list(in_dict: dict) -> list:
    dictlist = []
    for key, val in in_dict.items():
        temp = [key, val]
        dictlist.append(temp)
    print("list view: ", dictlist)


def combine_dict(base: dict, new: dict):
    base.update(new)
    print("combined dict: ", base)
    to_list(base)


# create dict
dict1 = {"type": "A", "class": "High", "Price": 1000, "Level": 5, "Room": 25, "Fee": "Yes"}
dict2 = dict(type="A", class_="High", Price=1000, Level=5, Room=25, Fee="Yes")
dict3 = dict(zip(["type", "class", "Price", "Level", "Room", "Fee"], ["A", "High", 1000, 5, 25, "Yes"]))
print("initial dicts: ", dict1, dict2, dict3)

# update dict
dict1["Discount"] = 0.2
dict1["Price"] = 1500
print("updated dict:", dict1)

# remove value by key
dict1.pop("Fee")
print("the dict without a 'Fee' key", dict1)

# combine dict with new values and print the result
combine_dict(dict1, {"type": "A", "class": "Middle", "Price": 700, "Level": 2, "Room": 10, "Discount": 0.1})
combine_dict(dict1, {"type": "B", "class": "High", "Price": 1200, "Level": 7, "Room": 38, "Discount": 0})
combine_dict(dict1, {"type": "B", "class": "High", "Price": 1200, "Level": 8, "Room": 39, "Discount": 0.2})
combine_dict(dict1, {"type": "C", "class": "Low", "Price": 600, "Level": 3, "Room": 16, "Discount": 0.3})
