text = input("Enter the string: ")
freq = [0] * 26
for char in text:
    freq[ord(char) - ord('a')] += 1
print(min(freq[ord('b') - ord('a')], freq[ord('a') - ord('a')], freq[ord('l') - ord('a')] // 2, freq[ord('o') - ord('a')] // 2, freq[ord('n') - ord('a')]))