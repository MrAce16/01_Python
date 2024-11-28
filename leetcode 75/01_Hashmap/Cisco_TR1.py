# flower,flow, o/p --> flow

def longest_prefix(result):
    if not result:
        return ""
    
    prefix = result[0]

    for r in result[1:]:
        while not r.startswith(prefix):
            prefix = prefix[:-1]

            if not prefix:
                return ""
    
    return prefix


words = ["flower","flow","result"]
result = longest_prefix(words)
print(result)