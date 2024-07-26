def encode(text, key):
    alpha_len = len(alpha) #26
    new_text = ''
    for char in text: # Hello
        if char.islower():
            index_char = (alpha.find(char) + key) % alpha_len
            char = alpha[index_char]
            new_text += char
        else:
            char = char.lower() # 'h'
            index_char = (alpha.find(char) + key) % alpha_len
            char = alpha[index_char]
            char = char.upper() # 'H'
            new_text += char
    return new_text

alpha = 'abcdefghijklmnopqrstuvwxyz'
i = 0

with open('input(4).txt', encoding='utf-8') as f:
    for line in f:
        print(encode(line.strip(), (i := i + 1)))


