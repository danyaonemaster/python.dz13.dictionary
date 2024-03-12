dict_01_01 = {"type": "A", "class": "High",
              "Price": 1000, "Level": 5,
              "Room": 25, "Fee": "Yes"}
my_dict_01_01 = dict(type="A", class_="High", Price=1000,
                     Level=5, Room=25, Fee="Yes")
dict_01_03 = dict({"type": "A", "class": "High", "Price": 1000,
                   "Level": 5, "Room": 25, "Fee": "Yes"})
dict_02 = dict_01_01.copy()
dict_03 = dict_01_01.copy()
dict_04 = dict_01_01.copy()
dict_05 = dict_01_01.copy()

dict_01_01["Discount"], dict_01_01["Price"] = 0.2, 1500
dict_02.update({"type": "A", "class": "Middle", "Price": 700,
                "Level": 2, "Room": 10, "Discount": 0.1})
dict_03.update({"type": "B", "class": "High", "Price": 1200,
                "Level": 7, "Room": 38, "Discount": 0})
dict_04.update({"type": "B", "class": "High", "Price": 1200,
                "Level": 8, "Room": 39, "Discount": 0.2})
dict_05.update({"type": "C", "class": "Low", "Price": 600,
                "Level": 3, "Room": 16, "Discount": 0.3})

print(dict_01_01)
print(dict_01_01)
print(dict_02)
print(dict_03)
print(dict_04)
print(dict_05)
