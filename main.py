from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

dt = datetime.today().strftime('%d/%m/%Y')


if __name__ == '__main__':
    calculate_salary('Пользователь')
    get_employees('Пользователь')
    print(f'Сегодня {dt}')