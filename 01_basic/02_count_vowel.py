def count_vowel(s):
    vowels = "aeiouAEIOU"
    count = 0

    for char in s:
        if char in vowels:
            count += 1
    return count    

print(count_vowel("Hello World"))