from data_and_logic.data import *
from model.user import User


def sign_in():
    login = input("Podaj login: ")
    password = input("Podaj hasło: ")
    find_user = "SELECT * FROM user WHERE login = ? AND password = ?"
    c.execute(find_user, [(login), (password)])
    conn.commit()
    results = c.fetchall()
    if results:
        for i in results:
            print("Witaj " + i[1])
    else:
        print("Niepoprawny użytkownik i hasło.")
        again = input("Czy chcesz spróbować ponownie? (t/n): ")
        if again.lower() == "n":
            print("Goodbye")
        elif again.lower() == "t":
            sign_in()


def register():
    new_user = User()
    new_user.id = input("Podaj numer id: ")
    new_user.name = input("Podaj imię: ")
    new_user.last = input("Podaj nazwisko: ")
    new_user.login = input("Podaj login: ")
    new_user.password = input("Podaj hasło: ")

    c.execute("INSERT INTO user VALUES (:id, :name, :last, :login, :password)",
           (new_user.id, new_user.name, new_user.last, new_user.login, new_user.password))
    conn.commit()


#sign_in()
#register()
