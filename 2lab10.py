color_list1 = input("enter colors for list1(separated by space):").split()
color_list2 = input("enter colors for list2(separated by sp[ace:").split()
result = [color for color in color_list1 if color not in color_list2]
print("colors in list1 not in list 2:",result)

