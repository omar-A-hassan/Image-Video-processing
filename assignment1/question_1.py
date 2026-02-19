string = str(input("Enter a string: ")).lower()
vowels = 0

for char in string:

    if char in 'aeiou':
        vowels += 1
        print(f"vowel found {char}")


print(f"Number of vowels is: {vowels}")