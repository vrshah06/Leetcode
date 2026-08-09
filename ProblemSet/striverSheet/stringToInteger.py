string = input("Enter a string: ")
result = ""
string = string.lstrip()
if string[0] == '-' or string[0] == '+':
    result += string[0]

for i in range(len(string)):
    if ((string[i] == " " or string[i] == "0") and (result == "" or result == "-" or result == "+")):
        continue
    if string[i].isdigit():
        result += string[i]
    if string[i].isalpha():
        break
    if string[i]=="-" or string[i]=="+":
        if i != 0:
            break
if result == "":
    result = "0"
print(int(result))