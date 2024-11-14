# Итераторы

class StepValueError(ValueError):
    pass
class Iterator:
    """
     Атрибуты объекта:
     start - целое число, с которого начинается итерация.
     stop - целое число, на котором заканчивается итерация.
     step - шаг, с которым совершается итерация.
     pointer - указывает на текущее число в итерации (изначально start).
     """
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
         self.pointer = self.start
         return self

    def __next__(self):
        value = self.pointer
        if (self.step < 0  and self.pointer < self.stop) or (self.step > 0 and self.pointer > self.stop):
            raise StopIteration()
        self.pointer += self.step
        return  value


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')
print()
iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(20, 1)
# В iter5 start > stop. а step по умолчанию == 1, ->
# -> результатов нет


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()