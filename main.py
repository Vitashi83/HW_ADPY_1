from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    print('Start main.py')
    print(f'Текущее время: {datetime.now()}' )
    calculate_salary()
    get_employees()
    print('Stop main.py')