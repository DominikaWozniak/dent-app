import sqlite3
from model.patient import Patient
from model.user import User
from model.visit import Visit

conn = sqlite3.connect('patient_visit.db')

c = conn.cursor()

#c.execute("""CREATE TABLE patient (
            #id integer primary key,
            #name text,
            #last text,
            #age text
         #)""")

#patient = Patient(1, "Anna", "Kowalska", 28)
#patient2 = Patient(2, "Jan", "Nowak", 30)

#c.execute("INSERT INTO patient VALUES (:id, :name, :last, :age)",
#                                    (patient.id, patient.name, patient.last, patient.age))
#c.execute("INSERT INTO patient VALUES (:id, :name, :last, :age)",
#                                       (patient2.id, patient2.name, patient2.last, patient2.age))

#c.execute("""CREATE TABLE user (
            #id integer primary key,
            #name text,
            #last text,
            #login text,
            #password text
            #)""")

#user_g = User(1, "Grzegorz", "Bączek", "grzesiek", "admin1")

#c.execute("INSERT INTO user VALUES (:id, :name, :last, :login, :password)",
          #(user_g.id, user_g.name, user_g.last, user_g.login, user_g.password))

#c.execute("""CREATE TABLE visit (
            #id primary key,
            #patient_id int,
            #visit_date text,
            #description text,
            #FOREIGN KEY(patient_id) REFERENCES patient (id)

#)""")

#conn.commit()
#c.execute("SELECT * FROM patient")
#headers = ['ID', 'NAME', 'FIRSTNAME', 'AGE']
#print(headers)
#print(*c.fetchall(), sep='\n')

#c.execute("SELECT * FROM user ")
#print(c.fetchall())








