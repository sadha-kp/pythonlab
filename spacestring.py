str1 = input("enter string1: ")
str2 = input("enter string2: ")
new_str1 = str1[0] + str2[1] + str1[2:]
new_str2 = str2[0] + str1[1] + str2[2:]
str3 = new_str1 + " " + new_str2
print("resulting string: ", str3)
