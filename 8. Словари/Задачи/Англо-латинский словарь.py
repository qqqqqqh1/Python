wordbook = {}

for i in range(int(input())):
    eng, lat = input().split(' - ')
    lat = lat.split(', ')
    for word in lat:
        wordbook[word] = [eng] if word not in wordbook else wordbook[word].append(eng)

print(len(wordbook))

for words in sorted(wordbook.keys()):
    print(f"{words} - {', '.join(wordbook[words])}")
