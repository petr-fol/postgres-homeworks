import csv
import os
import psycopg2
from sql_scripts import *


def main():
    # Подключение к базе данных
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="north",
        user="postgres",
        password=os.getenv("passwd_postgres")
    )

    # Создание курсора
    cur = conn.cursor()

    # Выполнение SQL-запросов
    cur.execute(create_employees_table)
    cur.execute(create_customers_table)
    cur.execute(create_orders_table)

    # Функция для вставки данных в таблицу из CSV-файла
    def insert_data(table_name, csv_file):
        with open(csv_file, 'r', encoding='cp1251') as file:
            reader = csv.reader(file)
            header = next(reader)  # Пропустить заголовок
            columns = ', '.join(header)
            placeholders = ', '.join(['%s'] * len(header))
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            data = [tuple(row) for row in reader]
            cur.executemany(query, data)

    # Загрузка данных в таблицы
    insert_data('employees', 'north_data/employees_data.csv')
    insert_data('customers', 'north_data/customers_data.csv')
    insert_data('orders', 'north_data/orders_data.csv')

    # Фиксация изменений и закрытие соединения
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
