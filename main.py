import os
from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    if not os.path.exists("key.key"):
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    return key


def load_key():
    with open("key.key", "r") as f:
        key = f.read()
    return key


def add(f):
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    new_password = f.encrypt(password.encode()).decode()
    with open("passwords.txt", "a") as file:
        file.write(f'{login}|{new_password}\n')


def view(f):
    with open("passwords.txt", "r") as file:
        for line in file:
            line.strip()
            login, password = line.split("|")
            print(f"Логин: {login} | Пароль: {f.decrypt(password.encode()).decode()}")


def main():
    write_key()
    key = load_key()
    f = Fernet(key)
    while True:
        choice = int(input("Хотите добавить новый пароль или посмотреть существующие 1. Посмотреть 2. Добавить? Нажмите 3, чтобы выйти "))
        if choice == 1:
            view(f)
        elif choice == 2:
            add(f)
        elif choice == 3:
            break
        else:
            print("Такой функции не существует")


if __name__ == "__main__":
    main()