def custom_write(file_name, strings):
    """
    Записывает строки в файл и возвращает информацию о позициях каждой строки.

    Аргументы:
        file_name (str): Имя файла, в который будут записаны строки.
        strings (list): Список строк для записи в файл.

    Возвращает:
        dict: Словарь, где ключом является кортеж (номер строки, начальная позиция в файле), 
              а значением - сама строка.

    Пример:
        info = ['Привет', 'Hello']
        result = custom_write('example.txt', info)
        print(result)  # {(1, 0): 'Привет', (2, 13): 'Hello'}
    """
    strings_positions = {}  # Словарь для хранения позиций строк
    line_number = 0  # Номер строки

    # Открытие файла для записи
    with open(file_name, 'w') as file:
       
       # Перебор списка строк для записи
       for string in strings:
           line_number += 1
           
           # Определение текущей позиции в файле
           start_position = file.tell()
           
           # Запись строки в файл
           file.write(string + '\n')
                      
           # Сохранение номера строки, позиции и самой строки
           strings_positions[(line_number, start_position)] = string
           
    return strings_positions

# Пример использования
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

# Вызов функции и печать результата
result = custom_write('test.txt', info)

for elem in result.items():
  print(elem)
