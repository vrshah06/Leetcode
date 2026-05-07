queries = eval(input("Enter the list of queries: "))
dictionary = eval(input("Enter the list of words in the dictionary: "))
temp = []
for query in queries:
    if query in dictionary:
        temp.append(query)
    else:
        for word in dictionary:
            if len(query) == len(word):
                count = 0
                for i in range(len(query)):
                    if query[i] != word[i]:
                        count += 1
                if count <= 2:
                    temp.append(query)
                    break
print(temp)