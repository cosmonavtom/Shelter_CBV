from django.core.management import BaseCommand
import pyodbc
from config.settings import DATABASE, USER, PASSWORD, HOST


class Command(BaseCommand):

    # def handle(self, *args, **options):
    #     ConnectionString = f'''DRIVER ={{ODBC Driver 17 for SQL Server}};
    #                                     SERVER={HOST};
    #                                     DATABASE=Students;
    #                                     UID={USER};
    #                                     PWD={PASSWORD}'''
    #     try:
    #         conn = pyodbc.connect(ConnectionString)
    #     except pyodbc.ProgrammingError as ex:
    #         print(ex)
    #     else:
    #         conn.autocommit = True
    #         try:
    #             conn.execute(fr"CREATE DATABASE {DATABASE}")
    #         except pyodbc.ProgrammingError as ex:
    #             print(ex)
    #         else:
    #             print(f'DB {DATABASE} created')

    def handle(self, *args, **options):
        # Подключаемся к базе данных Students(была создана первой)
        connection_string = f'''
            DRIVER={{ODBC Driver 17 for SQL Server}};
            SERVER={HOST};
            DATABASE=Students;         
            UID={USER};
            PWD={PASSWORD}'''

        conn = None
        try:
            # Устанавливаем соединение
            conn = pyodbc.connect(connection_string)
            conn.autocommit = True  # Включаем автокоммит

            # Создаем базу данных
            conn.execute(f"CREATE DATABASE {DATABASE}")
            print(f'DB {DATABASE} created.')

        except pyodbc.ProgrammingError as ex:
            print(f"Ошибка при выполнении команды: {ex}")

        except pyodbc.Error as ex:
            print(f"Ошибка подключения: {ex}")

        finally:
            # Закрываем соединение, если оно было открыто
            if conn:
                conn.close()


