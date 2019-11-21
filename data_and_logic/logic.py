from data_and_logic.data import *
from model.visit import *

def sign_in():
    login = input("Podaj login: ")
    password = input("Podaj hasło: ")
    find_user = "SELECT * FROM user WHERE login = ? AND password = ?"
    c.execute(find_user, [(login), (password)])
    conn.commit()
    results = c.fetchall()
    print("")
    if results:
        for i in results:
            print("Witaj " + i[1])
            print("")
            menu()

    else:
        print("Niepoprawny użytkownik lub hasło.")
        again = input("Czy chcesz spróbować ponownie? (t/n): ")
        if again.lower() == "n":
            print("Goodbye")
        elif again.lower() == "t":
            sign_in()

def hello_new_user():
    print("Witaj nowy użytkowniku.")
    print("1. Zaloguj. ")
    print("2. Wyjdź z programu.")
    option = input("Wybierz opcję: ")
    if option == "1":
        sign_in()
    elif option == "2":
        print("Zakończono program.")
    else:
        print("Nieznana opcja.")
        hello_new_user()

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
    hello_new_user()

def start():
    print("1. Zaloguj.")
    print("2. Zarejestruj.")
    print("3. Zakończ program.")
    option = input("Wybierz opcję: ")
    if option == "1":
        sign_in()
    elif option == "2":
        register()
    elif option == "3":
        print("Zakończono.")
    else:
        print("Nieznane polecenie")


def add_new_patient():
    new_patient = Patient()
    new_patient.id = input("Podaj id pacjenta: ")
    new_patient.name = input("Podaj imię pacjenta: ")
    new_patient.last = input("Podaj nazwisko pacjenta: ")
    new_patient.age = input("Podaj wiek pacjenta: ")
    c.execute("INSERT INTO patient VALUES (:id, :name, :last, :age)",
              (new_patient.id, new_patient.name, new_patient.last, new_patient.age))
    conn.commit()
    print("Dodano.")
    print("1. Wyjście do menu.")
    option = input("Wybierz opcję: ")
    if option == "1":
        menu()
    else:
        print("Nieznane polecenie.")


def find_all_patient():
    c.execute("SELECT * FROM patient")

    print("| ID     | NAME           | LASTNAME        | AGE   |")
    for i in c.fetchall():
        print("|", i[0], " " * (5-len(str(i[0]))), "|",
              i[1], " " * (13-len(i[1])), "|",
              i[2], " " * (14-len(i[2])), "|",
              i[3], " " * (4-len(i[3])), "|")
    print("")
    print("1. Wyjście do menu.")
    option = input("Wybierz opcję: ")
    if option == "1":
        menu()
    else:
        print("Nieznane polecenie.")
        find_all_patient()


def find_patient_by_id():
    id = input("Podaj ID pacjenta: ")
    find_id = "SELECT * FROM patient WHERE id = ?"
    c.execute(find_id, [(id)])
    conn.commit()
    results = c.fetchall()
    print("| ID     | NAME           | LASTNAME        | AGE   |")
    if results:
        for i in results:
            print("|", i[0], " " * (5 - len(str(i[0]))), "|",
                  i[1], " " * (13 - len(i[1])), "|",
                  i[2], " " * (14 - len(i[2])), "|",
                  i[3], " " * (4 - len(i[3])), "|")
    print("")
    print("1. Wyjście do menu.")
    option = input("Wybierz opcję: ")
    if option == "1":
        menu()
    else:
        print("Nieznane polecenie.")
        find_patient_by_id()


def find_patient_by_last():
    last = input("Podaj nazwisko pacjenta: ")
    find_last = "SELECT * FROM patient WHERE last = ?"
    c.execute(find_last, [(last)])
    conn.commit()
    results = c.fetchall()
    print("| ID     | NAME           | LASTNAME        | AGE   |")
    if results:
        for i in results:
            print("|", i[0], " " * (5 - len(str(i[0]))), "|",
                  i[1], " " * (13 - len(i[1])), "|",
                  i[2], " " * (14 - len(i[2])), "|",
                  i[3], " " * (4 - len(i[3])), "|")
    print("")
    print("1. Wyjście do menu.")
    option = input("Wybierz opcję: ")
    if option == "1":
        menu()
    else:
        print("Nieznane polecenie.")
        find_patient_by_last()


def add_new_visit():
    new_visit = Visit()
    new_visit.id = input("Podaj id wizyty: ")
    new_visit.patient = input("Podaj id pacjenta: ")
    new_visit.date = input("Podaj datę: dd-mm-rrrr: ")
    new_visit.description = input("Podaj opis wizyty: ")

    c.execute("INSERT INTO visit VALUES (:id, :patient_id, :date, :description)",
              (new_visit.id, new_visit.patient, new_visit.date, new_visit.description))
    conn.commit()
    print("Dodano.")
    print("1. Wyjście do menu.")
    option = input("Wybierz opcję: ")
    if option == "1":
        menu()
    else:
        print("Nieznane polecenie.")


def find_all_visit():
    c.execute("SELECT * FROM visit")
    print("| ID   | PATIENT ID   | VISIT DATE   | DESCRIPTION                                |")
    for i in c.fetchall():
        print("|", i[0], " " * (3-len(i[0])), "| ", i[1], " " * (10-len(str(i[1]))), "|",
              i[2], " " * (11-len(i[2])), "|", i[3], " " * (41-len(i[3])), "|")
    print("")
    print("1. Wyjście do menu.")
    option = input("Wybierz opcję: ")
    if option == "1":
        menu()
    else:
        print("Nieznane polecenie.")
        find_all_visit()


def find_visit_by_id():
    id = input("Podaj ID wizyty: ")
    find_id = "SELECT * FROM visit WHERE id = ?"
    c.execute(find_id, [(id)])
    conn.commit()
    result = c.fetchall()
    print("| ID   | PATIENT ID   | VISIT DATE   | DESCRIPTION                                |")
    if result:
        for i in result:
            print("|", i[0], " " * (3 - len(i[0])), "| ", i[1], " " * (10 - len(str(i[1]))), "|",
                  i[2], " " * (11 - len(i[2])), "|", i[3], " " * (41 - len(i[3])), "|")
    print("")
    print("1. Wyjście do menu.")
    option = input("Wybierz opcję: ")
    if option == "1":
        menu()
    else:
        print("Nieznane polecenie.")
        find_visit_by_id()


def choose_option_find_patient():
    print("1. Znajdź pacjenta po nr ID. ")
    print("2. Znajdź pacjenta po nazwisku. ")
    print("")
    option = input("Wybierz opcję: ")
    if option == "1":
        find_patient_by_id()
    elif option == "2":
        find_patient_by_last()
    else:
        print("Nieznane polecenie. ")
        choose_option_find_patient()

def delete_patient_by_id():
    id = input("Podaj id pacjenta: ")
    delete_id = "DELETE FROM patient WHERE id = ?"
    c.execute(delete_id, [id])
    conn.commit()
    print("Usunięto. ")
    print("1. Powrót do menu.")
    print("")
    option = input("Wybierz opcję: ")
    if option == "1":
        menu()
    else:
        print("Nieznane polecenie.")


def delete_visit_by_id():
    id = input("Podaj id wizyty: ")
    delete_id = "DELETE FROM visit WHERE id = ?"
    c.execute(delete_id, [id])
    conn.commit()
    print("Usunięto. ")
    print("1. Powrót do menu.")
    print("")
    option = input("Wybierz opcję: ")
    if option == "1":
        menu()
    else:
        print("Nieznane polecenie.")

def admin_panel():
    print("1. Usuń pacjenta z bazy.")
    print("2. Usuń wizytę.")
    print("")
    option = input("Wybierz opcję: ")
    if option == "1":
        delete_patient_by_id()
    elif option == "2":
        delete_visit_by_id()
    else:
        print("")
        print("Nieznane polecenie.")


def menu():
    print("0. Admin panel.")
    print("1. Dodaj pacjenta.")
    print("2. Dodaj wizytę.")
    print("3. Pokaż bazę pacjentów.")
    print("4. Znajdź pacjenta.")
    print("5. Pokaż wszystkie wizyty.")
    print("6. Znajdź wizytę.")
    print("7. Wyjdź z programu. ")
    print("")

    option = input("Wybierz opcję: ")

    if option == "1":
        add_new_patient()
    elif option == "2":
        add_new_visit()
    elif option == "3":
        find_all_patient()
    elif option == "4":
        choose_option_find_patient()
    elif option == "5":
        find_all_visit()
    elif option == "6":
        find_visit_by_id()
    elif option == "7":
        print("Koniec programu.")
    elif option == "0":
        admin_panel()
    else:
        print("Nieznane polecenie.")




start()
#find_patient_by_id()
#find_patient_by_last()
#find_all_visit()
#find_all_patient()
#find_visit_by_id()

