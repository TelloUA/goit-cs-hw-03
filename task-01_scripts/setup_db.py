from psycopg2 import sql, OperationalError

def setup_database(conn):
    file_path = "task-01_scripts/setup_db.sql"

    with open(file_path, "r") as sql_file:
        sql_commands = sql_file.read()

    with conn.cursor() as cursor:
        cursor.execute(sql.SQL(sql_commands))
        conn.commit()
        print("Таблиці та попередні налаштування успішно створенні.")