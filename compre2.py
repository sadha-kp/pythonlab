# Positive numbers
numbers = input("numbers: ").split()
positive_numbers = [int(n) for n in numbers if n.isdigit() and int(n) > 0]
print(positive_numbers)

# Squares of numbers
numbers_to_square = input("numbers to square: ").split()
squares = [int(n) ** 2 for n in numbers_to_square if n.isdigit()]
print(squares)

# Vowels in a word
word = input("word: ")
vowels = [ch for ch in word if ch in 'aeiouAEIOU']
print(vowels)

# ASCII values of characters
another_word = input("another word: ")
ascii_values = [ord(ch) for ch in another_word]
print(ascii_values)

~                                                                                                                                                             
~                                                                                                                                                             
~                                                                                                                                                             
~                                                                                                                                                             
~                                
