# Q1. Access key value from nested dictionary
nested_dict = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3,
            'f': 4
        }
    },
    'g': {
        'h': 5,
        'i': {
            'j': 6
        }
    },
    'k': 7
}


# Access value associated with key 'a'
print(nested_dict['a'])  # Output: 1

# Access value associated with key 'c' inside 'b'
print(nested_dict['b']['c'])  # Output: 2

# Access value associated with key 'e' inside 'd' which is inside 'b'
print(nested_dict['b']['d']['e'])  # Output: 3

# Access value associated with key 'h' inside 'g'
print(nested_dict['g']['h'])  # Output: 5

# Access value associated with key 'j' inside 'i' which is inside 'g'
print(nested_dict['g']['i']['j'])  # Output: 6

# Access value associated with key 'k'
print(nested_dict['k'])  # Output: 7


res = {"healthEvents": [{"severity": 3, "hostname": "bdd-dnac-219-13.cisco.com", "instance": "bdd-dnac-219-13.cisco.com:wireless_concurrent_clients",
                         "subDomain": "Scale Limits", "domain": "Cisco DNA Center System",
                         "description": "[DEPRECATED] Wireless concurrent client count is 0.",
                         "state": "OK", "timestamp": "1721379141016", "status": "Ok"},
                        {"severity": 3, "hostname": "bdd-dnac-219-13.cisco.com", "instance": "bdd-dnac-219-13.cisco.com:physical_ports", "subDomain": "System Scale Limits", "domain": "System",
                         "description": "Physical port count is 876.", "state": "OK", "timestamp": "1721379140994", "status": "Ok"},
                        {"severity": 2, "hostname": "bdd-dnac-219-13.cisco.com", "instance": "bdd-dnac-219-13.cisco.com:physical_ports",
                         "subDomain": "Scale Limits", "domain": "Cisco DNA Center System", "description": "[DEPRECATED] Physical port count is 876.", "state": "OK", "timestamp": "1721379140994", "status": "Ok"}],
       "hostname": "bdd-dnac-219-13.cisco.com", "version": "1", "cimcaddress": ["Cimc is not configured, please configure it from Settings->System Health Page."]}
for data in res["healthEvents"]:
    print[data["instance"]]
