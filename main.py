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


def add(fernet):
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    new_password = fernet.encrypt(password.encode()).decode()
    with open("passwords.txt", "a") as file:
        file.write(f'{login}|{new_password}\n')


def view(fernet):
    with open("passwords.txt", "r") as file:
        for line in file:
            login, password = line.strip().split("|")
            print(f"Логин: {login} | Пароль: {fernet.decrypt(password.encode()).decode()}")


def main():
    write_key()
    key = load_key()
    fernet = Fernet(key)
    while True:
        choice = int(input("Хотите добавить новый пароль или посмотреть существующие 1. Посмотреть 2. Добавить? Нажмите 3, чтобы выйти "))
        if choice == 1:
            view(fernet)
        elif choice == 2:
            add(fernet)
        elif choice == 3:
            break
        else:
            print("Такой функции не существует")


if __name__ == "__main__":
    main()