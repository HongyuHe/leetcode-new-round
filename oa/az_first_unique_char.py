"""
[Forests OA]
Given a string `s` consisting lowercase English letters, 
return the index of the first occurrences of a unique character in the string using 1-based indexing. 
If the string doesn't contain any unique character, return -1.

For example, `s='hackthegame' where the unique characters are `[c, t, g, m]`. 
The character `c` occurs first at index 3. Therefore, the program should return 3.
Another example is `s='falafal'`, answer: -1
Another example is `s='statistics'`, answer: 3
"""

def first_unique_char(s):
    char_count = {}

    for i, char in enumerate(s):
        if char in char_count:
            char_count[char] = -1  # Mark as non-unique
        else:
            char_count[char] = i + 1  # 1-based index

    first_unique_index = float('inf')

    for char, index in char_count.items():
        if index != -1 and index < first_unique_index:
            first_unique_index = index

    return -1 if first_unique_index == float('inf') else first_unique_index

# Test cases:
s1 = 'hackthegame'
s2 = 'falafal'
s3 = 'statistics'

result1 = first_unique_char(s1)
result2 = first_unique_char(s2)
result3 = first_unique_char(s3)

print(result1)  # Output: 3
print(result2)  # Output: -1
print(result3)  # Output: 3
