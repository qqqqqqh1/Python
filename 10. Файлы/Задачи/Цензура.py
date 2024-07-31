def censor_words(text, censor):
    for word in censor:
        new_word = word[0] + (len(word) - 2) * '*' + word[-1]
        text = text.replace(word, new_word)
    return text


line_true = open('input(5).txt', encoding='utf-8').read()
lst = open('censored.txt', encoding='utf-8').readlines()
print(censor_words(line_true, lst))
