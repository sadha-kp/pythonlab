names = input("Enter first names  separated by commas: ").split(',')
count = sum(name.lower().count('a') for name in names)
print("Occurrences of 'a':", count)
