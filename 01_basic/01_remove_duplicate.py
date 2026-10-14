# Logic: Iterate through the string character by character.
#  Use a Set to track characters encountered so far. If a character is not in seen, add it to the set and push it to the result array. 
# Finally, join the array back into a string.

def remove_duplicate(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)

    return "".join(result)

print(remove_duplicate("Programme"))

