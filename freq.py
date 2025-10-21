text = input("enter a string:")
char_count = {}
for char in text:
             char_count[char] = char_count.get(char,0)+1
             print("character frequencies:",char_count)
