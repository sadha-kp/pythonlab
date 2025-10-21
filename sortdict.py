d = {}
for _ in range(int(input("Number of items: "))):
    k = input("Key: ")
    v = int(input("Value: "))
    d[k] = v

print("Ascending:", dict(sorted(d.items())))
print("Descending:", dict(sorted(d.items(), reverse=True)))

