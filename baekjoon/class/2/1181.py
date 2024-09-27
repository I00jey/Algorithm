n = int(input())
strings = {}

for i in range(n):
    word = input()
    if len(word) in strings:
        if word in strings[len(word)]:
            continue
        else:
            strings[len(word)].append(word)
    else:
        strings[len(word)] = [word]


for j in range(max(strings)+1):
    if j in strings:
        for word in sorted(strings[j]):
            print(word)
