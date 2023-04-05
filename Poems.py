def count_vowels_and_consonants(line):
    vowels = "aeiou"
    num_vowels = 0
    num_consonants = 0
    for char in line:
        if char.isalpha():
            if char.lower() in vowels:
                num_vowels += 1
            else:
                num_consonants += 1
    return (num_vowels, num_consonants)


num_lines = int(input("How many lines will there be? "))
lines = []
vowels = 0
consonants = 0
for i in range(num_lines):
    line = input(f"Enter line {i+1}: ")
    lines.append(line)
    line_vowels, line_consonants = count_vowels_and_consonants(line)
    vowels += line_vowels
    consonants += line_consonants
    print(f"Line {i+1} has {line_vowels} vowels and {line_consonants} consonants")

print(f"\nTotal number of vowels: {vowels}")
print(f"Total number of consonants: {consonants}")
