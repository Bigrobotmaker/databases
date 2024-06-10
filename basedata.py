import sqlite3
going = True
operation = 'a'
submitname = 'a'
submitscore = 0
searcher = ''
connection = sqlite3.connect("scoreboard.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS scoreboard (name TEXT, score TEXT)")
while going == True:
    operation = input("what would you like to do? ")
    if operation == 'add':
        submitname = str(input('what is your name? '))
        submitscore = str(input('what was your score? '))
        cursor.execute('INSERT INTO scoreboard VALUES ("' + submitname + '", "' + submitscore +'")')
        connection.commit()
    if operation == 'search':
        searcher = str(input("who's score would you like to search for?"))
        cursor.execute('SELECT * FROM scoreboard\nWHERE name = "' + searcher + '"')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    if operation == 'exit':
        going = False
    else:
        print('operation not recognised')
connection.close()