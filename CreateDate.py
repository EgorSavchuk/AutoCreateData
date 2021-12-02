import random
from datetime import date
start_date = date.today().replace(day=1, month=1).toordinal()  # Дата от которой будет выбираться случайная дата
end_date = date.today().toordinal()  # Дата до которой будет выбраться случайная дата
f = open('date.txt', 'w')
start = 15  # От какого id
end = 51  # До какого id
line: str = ""
for i in range(start, end):
    if i == end - 1:
        line += f"\n('{i}', '{random.randint(1, 10)}', '{random.randint(1, 10)}', '{random.randint(1, 10)}', " \
                f"'{date.fromordinal(random.randint(start_date, end_date))}'); "
    else:
        line += f"\n('{i}', '{random.randint(1,10)}', '{random.randint(1,10)}', '{random.randint(1,10)}', " \
            f"'{date.fromordinal(random.randint(start_date, end_date))}'),"

f.write(line)
