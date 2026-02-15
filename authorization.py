from main import load_key
from cryptography.fernet import Fernet


def authorization(login, password, fernet):
    with open("passwords.txt", "r") as file:
        for line in file:
            log, pas = line.strip().split("|")
            pas = fernet.decrypt(pas.encode()).decode()
            if login == log and password == pas:
                print("Вы авторизованы")
                return True
            elif login == log and password != pas:
                print("Неверный пароль")
                return False
        print("Такого пользователя нет")
        return False            


def main():
    key = load_key()
    fernet = Fernet(key)
    while True:
        login = input("Логин: ")
        password = input("Пароль: ")
        if authorization(login, password, fernet):
            break


if __name__ == "__main__":
    main()