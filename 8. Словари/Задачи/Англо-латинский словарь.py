wordbook = {}

for i in range(int(input())):
    eng, lat = input().split('-')
    lat = lat.split(',')
    for word in lat:
        wordbook[word] = wordbook.get(word, '') + eng + ','

print(len(wordbook))

for words in sorted(wordbook.keys()):
    print(f'{words} - {wordbook[words][:-1]}')
