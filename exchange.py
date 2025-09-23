def swap_first_last(s):
    return s if len(s) < 2 else s[-1] + s[1:-1] + s[0]
s = input("enter a  string : ")
print(swap_first_last(s))


