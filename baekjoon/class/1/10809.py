s = input()
dic = dict.fromkeys([chr(i) for i in range(ord('a'), ord('z')+1)], -1)
for idx, word in enumerate(s):
    if dic[word] == -1:
        dic[word] = idx

print(' '.join([str(i) for i in dic.values()]))