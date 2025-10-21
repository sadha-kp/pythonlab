
nums = input("Enter numbers separated by spaces: ").split()
odd_nums = [int(n) for n in nums if int(n) % 2 != 0]
print("List after removing even numbers:", odd_nums)

