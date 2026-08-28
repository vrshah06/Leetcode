s = input("Enter a string: ")
hash_map = {}
for char in s:
    if char in hash_map:
        hash_map[char] += 1
    else:
        hash_map[char] = 1
print("Character frequencies:", hash_map)
hash_map = list(hash_map.items())
hash_map.sort(key=lambda x: (-x[1], x[0]))
result = []
for char, freq in hash_map:
    if freq > 0:
        result.append(char)
print("Characters sorted by frequency:", result)