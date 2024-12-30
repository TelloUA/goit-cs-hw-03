import shlex
from pymongo import MongoClient
from bson.objectid import ObjectId

MONGO_URI = "mongodb://root:example@localhost:27017/"

def check_db():
    try:
        client = MongoClient(MONGO_URI)
        client.admin.command('ping')
        print("Підключено до MongoDB!")
    except Exception as e:
        print(f"Помилка підключення до MongoDB: {e}")
        exit(1)

    return client

def create_cat(collection, name, age, *features):
    document = {"name": name, "age": age, "features": features}
    collection.insert_one(document)
    print(f"Кіт {name} доданий!")

def read_all_cats(collection):
    cats = collection.find()
    for cat in cats:
        print(cat)

def read_cat_by_name(collection, name):
    cat = collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print(f"Кота з ім'ям {name} не знайдено.")

def update_cat_age(collection, name, new_age):
    result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
    if result.modified_count > 0:
        print(f"Вік кота {name} оновлено до {new_age}.")
    else:
        print(f"Кота з ім'ям {name} не знайдено.")

def add_feature_to_cat(collection, name, *feature):
    result = collection.update_one({"name": name}, {"$push": {"features": feature}})
    if result.modified_count > 0:
        print(f"До кота {name} додано характеристику: {feature}.")
    else:
        print(f"Кота з ім'ям {name} не знайдено.")

def delete_cat_by_name(collection, name):
    result = collection.delete_one({"name": name})
    if result.deleted_count > 0:
        print(f"Кіт {name} видалений.")
    else:
        print(f"Кота з ім'ям {name} не знайдено.")

def delete_all_cats(collection):
    result = collection.delete_many({})
    print(f"Видалено {result.deleted_count} записів.")

def main():
    client = check_db()
    db = client.book
    collection = db.cats

    while True:
        try:
            choice = input("Введіть функцію та параметри, або 'exit': ")
            if choice.strip().lower() == "exit":
                print("Вихід.")
                break

            parts = shlex.split(choice)
            func_name = parts[0]
            args = parts[1:]

            func = globals().get(func_name)
            if func and callable(func):
                func(collection, *args)
            else:
                print(f"Функція '{func_name}' не знайдена.")
        except TypeError as e:
            print(f"Помилка: {e}")
        except Exception as e:
            print(f"Невідома помилка: {e}")


if __name__ == "__main__":
    main()