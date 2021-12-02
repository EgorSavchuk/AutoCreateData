import random
from datetime import date

start_date = date.today().replace(day=1, month=1).toordinal()
end_date = date.today().toordinal()
f = open('date.txt', 'w')
n = 50
line: str = "('13', '10', '1', '7', '2021-12-08'),"
for i in range(15, 51):
    if i == 50:
        line += f"\n('{i}', '{random.randint(1, 10)}', '{random.randint(1, 10)}', '{random.randint(1, 10)}', " \
                f"'{date.fromordinal(random.randint(start_date, end_date))}'); "
    else:
        line += f"\n('{i}', '{random.randint(1,10)}', '{random.randint(1,10)}', '{random.randint(1,10)}', " \
            f"'{date.fromordinal(random.randint(start_date, end_date))}'),"

f.write(line)