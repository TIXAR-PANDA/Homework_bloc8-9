# Генераторные сборки

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for (x,y) in zip(first,second ) if len(x) != len(y))
second_result = (len(first[x]) == len(second[y]) for x in range(0,len(first))
                 for y in range(0,len(second)) if x == y)
print(list(first_result))
print(list(second_result))