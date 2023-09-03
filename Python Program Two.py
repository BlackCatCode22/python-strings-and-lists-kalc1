# Python Project Two.py
#
# Name: Kevin Alcocer
# Date: 08/30/23
# Class: CIT-95

text = "Python is an amazing programming language. It is versatile, easy to learn, and powerful."

# Lenght Calculation
calculate_lenght = len(text)
print(calculate_lenght)

# Uppercase and Lowercase Conversion
uppercase = text.upper()
lowercase = text.lower()
print(uppercase)
print(lowercase)

# Word Count
word_count = text.count("is")
print(word_count)

# Substring Extraction
subtring_extract = text[0:42]
print(subtring_extract)

# Word Replacement
original = "Python, Armadillo, Raven, Manta Ray, Giraffe, Triceratops"
print(original)
target_word = input("Choose an animal from the choices above: ")
replacement_word = input("please enter a second animal from the choices above: ")
new_sentence = original.replace(str(target_word), str(replacement_word))
print(new_sentence)

# Whitespace Removal
text_with_whitespace = "     Python is an amazing programming language. It is versatile, easy to learn, and powerful.     "
print(text_with_whitespace.strip())

# Splitting Into Sentences
text2 = "Python is an amazing programming language. It is versatile, easy to learn, and powerful"
split_text = text2.split('.')
print(split_text)

# Word Reversal
text = "Python is an amazing programming language. It is versatile, easy to learn, and powerful."
reversal = (text[::-1])
text_split = (reversal.split())
second_reversal = text_split[::-1]
print(' '.join(second_reversal))

#Character Count
text = "Python is an amazing programming language. It is versatile, easy to learn, and powerful."
character = input("Please enter a character: ")
print(text.count(character))

# Substring Count
text = "Python is an amazing programming language. It is versatile, easy to learn, and powerful."
print(text.count("is"))

# List Creation
text = "Python is an amazing programming language. It is versatile, easy to learn, and powerful."
word_list = text.split(' ')
print(word_list)

# Appending
word_list.append("Pythonic")
print(word_list)

#Insertion
word_list[0:0] = ["awesome"]
print(word_list)

# Indexing and Slicing
print(word_list[2])
sublist = word_list[5:9]
print(sublist)

# Removal
word_list.remove("amazing")
print(word_list)

# Sorting
text = "Python is an amazing programming language. It is versatile, easy to learn, and powerful. Pythonic"
lowercase_text = text.lower()
word_list =lowercase_text.split(' ')
word_list.sort()
word_list.remove("amazing")
print(word_list)

# Counting
print(word_list.count("is"))

# Joining
print(' '.join(word_list))

# Reversal
print(word_list[::-1])

# Copying
copied_list = word_list
print(copied_list)





