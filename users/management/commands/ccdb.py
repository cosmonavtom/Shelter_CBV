from django.core.management import BaseCommand
import pyodbc
from config.settings import DATABASE, USER, PASSWORD, HOST


class Command(BaseCommand):

    def handle(self, *args, **options):
        ConnectionString = f'''DRIVER ={{ODBC Driver 17 for SQL Server}};
                                SERVER={HOST};
                                DATABASE={DATABASE};
                                UID={USER};
                                PWD={PASSWORD}'''
        try:
            conn = pyodbc.connect(ConnectionString)
        except pyodbc.ProgrammingError as ex:
            print(ex)
        else:
            conn.autocommit = True
            try:
                conn.execute(fr"CREATE DATABASE {DATABASE}")
            except pyodbc.ProgrammingError as ex:
                print(ex)
            else:
                print(f'DB {DATABASE} created')
