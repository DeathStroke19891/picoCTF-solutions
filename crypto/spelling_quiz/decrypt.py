file1 = open('study-guide.txt', 'r')

list = {}

for line in file1:
    for char in line:
        if char not in list:
            list[char]=1
        else:
            list[char] += 1

del list['\n']

res = {key: val for key, val in sorted(list.items(), key = lambda ele: ele[1], reverse = True)}
print(res)
