res = {"healthEvents": [{"severity": 3, "hostname": "bdd-dnac-219-13.cisco.com", "instance": "bdd-dnac-219-13.cisco.com:wireless_concurrent_clients", "subDomain": "Scale Limits", "domain": "Cisco DNA Center System", 
                         "description": "[DEPRECATED] Wireless concurrent client count is 0.", "state": "OK", "timestamp": "1721379141016", "status": "Ok"}, {"severity": 3, "hostname": "bdd-dnac-219-13.cisco.com", "instance": "bdd-dnac-219-13.cisco.com:physical_ports", "subDomain": "System Scale Limits", "domain": "System", "description": "Physical port count is 876.",
                                                                                                                                                                                                                                                                                                                                                             "state": "OK", "timestamp": "1721379140994", "status": "Ok"}, {"severity": 2, "hostname": "bdd-dnac-219-13.cisco.com", "instance": "bdd-dnac-219-13.cisco.com:physical_ports", "subDomain": "Scale Limits", "domain": "Cisco DNA Center System", "description": "[DEPRECATED] Physical port count is 876.", "state": "OK", "timestamp": "1721379140994", "status": "Ok"}], "hostname": "bdd-dnac-219-13.cisco.com", "version": "1", "cimcaddress": ["Cimc is not configured, please configure it from Settings->System Health Page."]}


# for data in res["healthEvents"]:
#     print(data["hostname"])

for data in res["healthEvents"]:
    if data["severity"] == 2:
        print(data["status"])


# Q2. How to import Api post in python

# Q3.

# dict1 = {}
# dict1["Ram"] = 2
# dict1["shyam"] = 3
# dict1["ankbar"] = 5
# dict1["ganesh"] = 2
# dict3 = print(dict1)
# for x in dict3.values():
#     print(x)

# Original dictionary
dict1 = {
    "Ram": 2,
    "shyam": 3,
    "ankbar": 5,
    "ganesh": 2
}

# Dictionary to track occurrences of each value
value_dict = {}

# Populate value_dict with values as keys and lists of corresponding original keys as values
for key, value in dict1.items():
    if value not in value_dict:
        value_dict[value] = [key]
    else:
        value_dict[value].append(key)
print(value_dict)

# Find duplicate values
duplicates = {value: keys for value,
              keys in value_dict.items() if len(keys) > 1}

# Print the results
print("Duplicate values and their keys:")
for value, keys in duplicates.items():
    print(f"Value {value} is found for keys: {keys}")


# Q4 parent of child class
