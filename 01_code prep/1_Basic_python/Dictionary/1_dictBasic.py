chai_types = {"Masala": "spiecy", "Ginger": "zesty", "Green": "Mild"}
print(chai_types)

# 1  How to access dictionary
print(chai_types["Masala"])

print(chai_types.get("Ginger"))  # get with () brancket

# 2 update dictionary

chai_types["Green"] = "Fresh"

print(chai_types)

# 3. For loops
for chai in chai_types:
    print(chai)  # to print key
    print(chai, chai_types[chai])   # to print dict with key value pair

# 4. key value using access .items()

for key, value in chai_types.items():
    print(key, value)

# 5.  To access particular key and values

if "Masala" in chai_types:
    print("I have masala chai")
    print(len(chai_types))

# 6. Add dictionary in given dictionary

chai_types["Earl Grey"] = "Citrus"
print(chai_types)

# 7. Delete dictionary using pop

chai_types.pop("Ginger")
print(chai_types)

# 8. how to delete last items from dictionary

chai_types.popitem()
print(chai_types)

# 9. Delete key word use every where.

del chai_types["Green"]
print(chai_types)

# 10. Dictionary inside dictionary
tea_shop = {
    # chai key and other values
    "chai": {"masala": "spicy", "ginger": "Zesty"},
    "Tea": {"Green": "Mild", "Black": "strong"}
}
print(tea_shop)

# 11. print values from dict inside dict

print(tea_shop["chai"]["ginger"])

# 12. square of number print in dict

square_num = {x: x**2 for x in range(6)}
print(square_num)

# 13. clear sqare_number dict.
square_num.clear()
print(square_num)

# 14. 2 array form dictionary

keys = ["Masala", "Ginger", "Lemon"]
default_values = "Delicious"
new_dict = dict.fromkeys(keys, default_values)
print(new_dict)
