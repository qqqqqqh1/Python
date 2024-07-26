def censor_words(text, censor):
    for word in censor:
        new_word = word[0] + (len(word) - 2) * '*' + word[-1]
        text = text.replace(word, new_word)
    return text

lst = []

with open('input(5).txt', encoding='utf-8') as f:
    line_true = f.readline()

with open('censored.txt', encoding='utf-8') as d:
    for line in d:
        wordss = line.split()
        for words in wordss:
            lst.append(words)

print(censor_words(line_true, lst))
