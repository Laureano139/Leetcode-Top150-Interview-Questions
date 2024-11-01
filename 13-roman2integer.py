def roman_to_integer(s: str) -> int:

    romanMapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    
    length = len(s)
    
    for i in range(length):
        currValue = romanMapping[s[i]]
        if(i + 1 < length and currValue < romanMapping[s[i+1]]):
            total -= currValue
        else:
            total += currValue
    
    print(total)
    return total

s = "III"

roman_to_integer(s)