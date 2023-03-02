"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" и обработав исключение,
придумайте как это сделать
"""
class ErrorByByte(Exception):
    def __init__(self, err):
        self.err = err




words = ['attribute', 'класс', 'функция', 'type']


for word in words:
    word_b = bytes(word, 'ascii', 'ignore')
    try:
        if word_b == b'':
            raise ErrorByByte(
                f'{word}  - невозможно записать в байтовом типе')
        print(word_b)
    except ErrorByByte as err:
        print(err)
