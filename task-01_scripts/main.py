# import psycopg2
from setup_db import setup_database
from seed import populate_test_data
from tasks import make_queries
from psycopg2 import connect, sql, OperationalError

def main_logic():

    DATABASE_CONFIG = {
        "dbname": "rest_app",
        "user": "postgres",
        "password": "567234",
        "host": "localhost",
        "port": "5432",
    }

    try:
        connection = connect(**DATABASE_CONFIG)
        setup_database(connection)
        populate_test_data(connection)
        make_queries(connection, "task-01_scripts/tasks.sql")
    except OperationalError as e:
        print(f"Помилка підключення до бази даних: {e}")
        exit(1)
    except Exception as e:
        print(f"Виникла помилка: {e}")
        exit(1)
    
if __name__ == "__main__":
    main_logic()
