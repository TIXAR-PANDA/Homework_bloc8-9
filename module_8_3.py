
# Создание исключений

class Car:
    """
Атрибут model - название автомобиля (строка).
Атрибут __vin номер автомобиля (целое число). Уровень доступа private.
Атрибут __numbers- номера автомобиля (строка).
    """
    def __init__(self, model, vin_number, numbers):
        self.model = model
        self.__vin = vin_number if self.__is_valid_vin(vin_number) else None
        self.__numbers = numbers if self.__is_valid_numbers(numbers) else None

    def __is_valid_vin(self, vin_number):
        """
        Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность.
        Возвращает True, если корректный, в других случаях выбрасывает исключение.
        Уровень доступа private.
        """
        if isinstance(vin_number, int):
            if 9999999 >= vin_number >= 1000000:
                return True
            else:
                raise IncorrectVinNumber('Неверный диапазон для vin номера', vin_number)

        else:
            raise IncorrectVinNumber('Некорректный тип vin номера', vin_number)

    def __is_valid_numbers(self, numbers):
        """
        Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность.
        Возвращает True, если корректный, в других случаях выбрасывает исключение.
        Уровень доступа private.
        """
        if isinstance(numbers, str):
            if len(numbers) == 6:
                return True
            else:
                    raise IncorrectCarNumbers('Неверная длина номера', numbers)
        else:
                raise IncorrectCarNumbers('Некорректный тип данных для номеров', numbers)




class IncorrectCarNumbers(Exception):
    """
    Класс исключений
    атрибут message - сообщение, которое будет выводиться при выбрасывании исключения
    атрибут inform - показывает номер машины
    """
    def __init__(self, message, inform):
        print('Ошибка в номере машины.->')
        self.message = message
        self.inform = inform

class IncorrectVinNumber(Exception):
    """
        Класс исключений
        атрибут message - сообщение, которое будет выводиться при выбрасывании исключения
        атрибут inform - показывает vin номер
        """
    def __init__(self, message, inform):
        print('Ошибка при указании vin номера.->')
        self.message = message
        self.inform = inform


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message,',',exc.inform )
except IncorrectCarNumbers as exc:
  print(exc.message,':',exc.inform )
else:
  print(f'Объект: {first.model} - успешно создан')

try:
  second = Car('Model2', 3000, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message,':',exc.inform )
except IncorrectCarNumbers as exc:
  print(exc.message,':',exc.inform )
else:
  print(f'Объект:{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message,':',exc.inform )
except IncorrectCarNumbers as exc:
  print(exc.message,':',exc.inform )
else:
  print(f'Объект:{third.model} успешно создан')

try:
  m4 = Car('Model4', 2020.202, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message,':',exc.inform )
except IncorrectCarNumbers as exc:
  print(exc.message,':',exc.inform )
else:
  print(f'Объект:{m4.model} успешно создан')