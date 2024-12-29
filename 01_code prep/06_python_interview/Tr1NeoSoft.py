def bracket_balanced(string):
    str = []
    matching_bracket = {')':'(', '}':'{',']':'['}

    for char in string:
        if char in matching_bracket.values():
            str.append(char)
        elif char in matching_bracket.keys():
            if str and str[-1] == matching_bracket[char]:
                str.pop()
            else:
                return False
    
    return not str



string = ")hello (world)"
print(bracket_balanced(string))



# (hello world)
# (hello (world))
# (hello world))