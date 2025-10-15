a = list(map(int, input("Enter first list (space separated): ").split()))
b = list(map(int, input("Enter second list (space separated) : ").split()))

print("Same length:" , len(a) == len(b))
print("Same sum:" , sum(a) == sum(b))
print("Common values:" , bool(set(a) & set(b)))


