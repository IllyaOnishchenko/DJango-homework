import sqlite3

conn = sqlite3.connect('db.sqlite')
c = conn.cursor()
maxsalary = 25000
maxs = maxsalary

def adduser(name, surname, salary):
    c.execute("insert into users (name, surname, salary) values ('%s', '%s', '%s')" %(name, surname, salary))
    conn.commit()


name = input("Enter user name: ")
surname = input("Enter user surname: ")
salary = input("Enter user salary: ")
while float(salary) > maxs:
    salary = input("Enter smaller salary >25000 :")
adduser(name, surname, salary)

print("Users list: \n")
c.execute('select * from users')
ulist = c.fetchone()

while ulist is not None:
    print("id: "+str(ulist[0]) + " Name: "+str(ulist[1]) + " Surname: "+str(ulist[2])+ " Salary: "+str(ulist[3]))
    ulist = c.fetchone()

c.close()
conn.close()
'''
c.execute("""
CREATE TABLE users(
id INTEGER AUTO_INCREMENT,
name varchar(255),
surname varchar (255),
salary int NOT NULL,
PRIMARY KEY(id))
""");
'''