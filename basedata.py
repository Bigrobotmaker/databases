import sqlite3
going = True
operation = 'a'
submitname = 'a'
submitscore = 0
connection = sqlite3.connect("scoreboard.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS scoreboard (name TEXT, score TEXT)")
while going == True:
    operation = input("what would you like to do? ")
    if operation == 'add':
        submitname = str(input('what is your name? '))
        submitscore = str(input('what was your score? '))
        cursor.execute('INSERT INTO scoreboard VALUES ("' + submitname + '", "' + submitscore +'")')
    if operation == 'exit':
        going = False
connection.commit()