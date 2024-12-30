import random
from faker import Faker

def populate_test_data(conn):
    faker = Faker()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM status;")
    status_count = cursor.fetchone()[0]

    user_ids = []
    for _ in range(5):
        fullname = faker.name()
        email = faker.unique.email()
        cursor.execute(
            "INSERT INTO users (fullname, email) VALUES (%s, %s) RETURNING id;",
            (fullname, email)
        )
        user_id = cursor.fetchone()[0]
        user_ids.append(user_id)

    for user_id in user_ids:
        for _ in range(4):
            title = faker.sentence(nb_words=5)
            description = faker.text(max_nb_chars=200)
            status_id = random.randint(1, status_count)
            cursor.execute(
                """
                INSERT INTO tasks (title, description, status_id, user_id)
                VALUES (%s, %s, %s, %s);
                """,
                (title, description, status_id, user_id)
            )

    conn.commit()
    print("Тестові дані успішно додано!")

