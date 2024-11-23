# Генераторы

def all_variants(text):
    for j in range(1, len(text) + 1):
        for i in range(len(text) - j + 1):
             yield text[i:i + j]

a = all_variants("abc")
for i in a:
    print(i)

