import arm  # only if you have arm.py in the same folder

a = int(input("Enter start: "))
b = int(input("Enter end: "))

for i in range(a, b + 1):
    if arm.check (i):
        print(i)

