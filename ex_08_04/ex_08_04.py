filename = open(input("Enter file name: "))
lst = list()
for line in filename:
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
