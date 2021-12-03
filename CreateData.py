import random
from datetime import date


def generate_date():  # Генерация случайной даты
    start_date = date.today().replace(day=1, month=1).toordinal()  # Дата от которой будет выбираться случайная дата
    end_date = date.today().toordinal()  # Дата до которой будет выбраться случайная дата
    return date.fromordinal(random.randint(start_date, end_date))


def generate_fullname():  # Генерация случайного ФИО
    from lib import FullNames
    return FullNames[random.randint(1, 999)]


def generate_email(to_full_name: str = ''):  # Генерация случайного email, если в функцию передать ФИО в формате -
    # Фамилия Имя Отчество вернет email в формате вышкинской почты
    if to_full_name == '':
        return f'example{random.randint(1,1000)}@miem.hse.ru'
    else:
        from lib import Dict
        fio_array = to_full_name.split(' ')
        first = Dict.get(fio_array[1][0])
        second = Dict.get(fio_array[2][0])
        email = f'{first}{second}'
        for j in fio_array[0]:
            email += Dict.get(j)
        email += '@miem.hse.ru'
        return email


def generate_text(symbols: int = 20):  # Генерирует случайный текст длинной symbols, по умолчанию 20 символов
    from lib import Text
    return Text[:symbols]


#  Пример использования, Допустим нужны строки (id, name, email, data , text)
data = open('data.txt', 'w')
start = 1  # От какого id
end = 51  # До какого id
result: str = ""  # Итоговая строка
for i in range(start, end):
    # Генерация имени, чтобы от него же можно было сгенерировать почту
    fullname = generate_fullname()
    # Строка в формате SQL VALUES ('значение' , 'значение2')
    line = f"('{i}', '{fullname}', '{generate_email(fullname)}', '{generate_date()}', '{generate_text(35)}')"
    if i == end - 1:  # Добавляет ; в конце, для последней строчки
        result += f"{line};"
    else:
        result += f"{line},\n"  # Добавляет переход строки для всех строчек, кроме последней
data.write(result)

