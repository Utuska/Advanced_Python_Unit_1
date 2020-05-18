from datetime import datetime, date
from dirty_main import *
from db import people
from db import salary


now = date.today()


if __name__ == '__main__':
    print(f'Сейчас {now}')
    print(datetime.now())
    people.get_employees()
    salary.calculate_salary()
    function_1()
