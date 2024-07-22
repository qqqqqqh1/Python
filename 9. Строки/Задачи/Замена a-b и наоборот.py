old_str = input()
count = 0
new_str = ''

letters = {
    'a': 'b',
    'A': 'B',
    'b': 'a',
    'B': 'A'
}

for letter in old_str:
    if letter in letters:
        new_str += letters[letter]
        count += 1
    else:
        new_str += letter

print(new_str)
print(count)
