import random

words = ["PIES", "WROCŁAW", "KUCHNIA", "ZABAWA"]

for i in range(len(words)):
    word = random.choice(words)
    print(word)
    words.remove(word)

print(words)

