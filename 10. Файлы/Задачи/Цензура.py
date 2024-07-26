def censor_word(word):
    lenn = len(word)
    char = ''
    if lenn > 2:
        word = list(word)
        for i in range(1, lenn-1):
            word[i] = '*'
        for x in range(lenn):
            char += word[x]
        return char
    else:
        return word

def swap_words(text, censor):
    for word in censor:
        censorr = censor_word(word)
        text = text.replace(word, censorr)
    return text

lst = []

with open('input(5).txt', encoding='utf-8') as f:
    line_true = f.readline()

with open('censored.txt', encoding='utf-8') as d:
    for line in d:
        wordss = line.split()
        for words in wordss:
            lst.append(words)

print(swap_words(line_true, lst))
