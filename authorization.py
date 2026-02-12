from main import load_key
from cryptography.fernet import Fernet


def authorization(login, password, f):
    with open("passwords.txt", "r") as file:
        for line in file:
            line.strip()
            log, pas = line.split("|")
            pas = f.decrypt(pas.encode()).decode()
            if login == log and password == pas:
                print("Вы авторизованы")
                return True
        print("Такого пользователя нет")
        return False            


def main():
    key = load_key()
    f = Fernet(key)
    while True:
        login = input("Логин: ")
        password = input("Пароль: ")
        if authorization(login, password, f):
            break


if __name__ == "__main__":
    main()