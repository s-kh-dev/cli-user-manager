import json

def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

def load_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

users = load_users()

def add_user(users, username, age, city, skills):
    users[username] = {
        "age": age,
        "city": city,
        "skills": skills
    }


def show_users(users):
    if not users:
        print("Список пользователей пуст")
    else:
        for key, dat in users.items():
            print(f"Имя пользователя - {key}")

            print(f"Возраст - {dat['age']}")
            print(f"Город - {dat['city']}")
            print(f"Навыки - {' '.join(dat['skills'])}")
            print("\n" + "-" * 20)

def update_user(users, usname):
    answer = input(
        "Что вы хотите изменить? \n"
        "1 - Возраст \n"
        "2 - Город \n"
        "3 - Навыки \n"
        "0 - Отмена \n"
    )
    if answer == "1":
        age_upd = int(input("Введите возраст: "))
        users[usname]["age"] = age_upd
        print("Возраст пользователя изменен!")
    elif answer == "2":
        city_upd = input("Введите город: ")
        users[usname]["city"] = city_upd
        print("Город пользователя изменен!")
    elif answer == "3":
        skills_upd = input("Введите навыки (через пробел): ").split()
        users[usname]["skills"] = skills_upd
        print("Навыки пользователя изменены!")
    else:
        print("Неверный выбор")

def delete_user(users):
    usname = input("Введите имя пользователя: ")
    if usname in users:
        del users[usname]
        print("Пользователь удален!")
        save_users(users)
    else:
        print("Пользователь не найден!")

while True:
    answer = input(
        "1 - Добавить пользователя \n"
        "2 - Показать всех пользователей \n"
        "3 - Изменить пользователя \n"
        "4 - Удалить пользователя \n"
        "0 - Выход "
    )

    if answer == "0":
        break
    elif answer == "1":
        usname = input("Введите имя пользователя: ")

        if usname in users:
            print("Пользователь уже существует")
        else:
            usage = int(input("Введите возраст: "))
            uscity = input("Введите город: ")
            skills = input("Введите навыки (через пробел): ").split()

            add_user(users, usname, usage, uscity, skills)
            save_users(users)
            print("-" * 20)
    elif answer == "2":
        show_users(users)
    elif answer == "3":
        usname = input("Введите имя пользователя: ")
        if usname in users:
            update_user(users, usname)
            save_users(users)
        else:
            print("Пользователь не найден")

    elif answer == "4":
        delete_user(users)
