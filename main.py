import os

from ORM_db import Database
from login import login
from tables_create import tables_create

db = Database("db")
tables_create(db)

username = input("Введите ваше имя: ")
password = input("Введите ваш пароль: ")

while True:
    user = login(username, password, db)
    if user is None:
        os.system("cls||clear")
        print("Логин или пароль введён неверно, повторите попытку")
        username = input("Введите ваше имя: ")
        password = input("Введите ваш пароль: ")
        continue
    else:
        break


while True:
    os.system("cls||clear")
    user.print_commands()
    command = input("Введите команду: ")
    # user.do_command(command)
    is_continue = input("Продлжить - press Enter,  Завершить работу - exit: ")
    if is_continue == "exit":
        break
print("Работа окончена")