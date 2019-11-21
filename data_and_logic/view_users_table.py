from data_and_logic.data import *

def view_users_data():
    c.execute("SELECT * FROM user")
    print("| ID   | NAME      | LASTNAME     | LOGIN        | PASSWORD    |")
    for i in c.fetchall():
        print("|",i[0], " " * (3-len(str(i[0]))),"|",
              i[1], " " * (8-len(i[1])), "|",
              i[2], " " * (11-len(i[2])), "|",
              i[3], " " * (11-len(i[3])), "|",
              i[4], " " * (10-len(i[4])), "|")

view_users_data()