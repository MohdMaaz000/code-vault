from collections import OrderedDict

n = int(input())
word_count = OrderedDict()

for _ in range(n):
    word = input().strip()
    word_count[word] = word_count.get(word, 0) + 1

print(len(word_count))
print(*word_count.values())
