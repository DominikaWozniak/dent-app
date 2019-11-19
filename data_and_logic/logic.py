from data_and_logic.register import *
from data_and_logic.data import *

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
        print("Zakończono. ")
    else:
        print("Nieznane polecenie.")
        start()

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
    headers = ['ID', 'NAME', 'FIRSTNAME', 'AGE']
    print(headers)
    print(*c.fetchall(), sep='\n')
    print("1. Wyjście do menu.")
    option = input("Wybierz opcję: ")
    if option == "1":
        menu()
    else:
        print("Nieznane polecenie.")
        find_all_patient()


def find_patient_by_id():
    pass

def add_new_visit():
    pass

def find_all_visit():
    pass

def find_visit_by_id():
    pass



def menu():
    print("1. Dodaj pacjenta.")
    print("2. Pokaż bazę pacjentów. ")
    print("3. Znajdź pacjenta.")
    print("4. Pokaż wszystkie wizyty.")
    print("5. Znajdź wizytę.")
    print("6. Wyjdź z programu. ")

    option = input("Wybierz opcję: ")

    if option == "1":
        add_new_patient()
    elif option == "2":
        find_all_patient()
    elif option == "3":
        find_patient_by_id()
    elif option == "4":
        find_all_visit()
    elif option == "5":
        find_visit_by_id()
    elif option == "6":
        print("Wyjście z programu.")
    else:
        print("Nieznane polecenie.")
        menu()



start()
menu()