import sqlite3
connection = sqlite3.connect("scoreboard.db")
print(connection.total_changes)
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS scoreboard (Name TEXT, score INTEGER)")
cursor.execute("INSERT INTO scoreboard VALUES ('bob', 10000)")
cursor.execute("INSERT INTO scoreboard VALUES ('jimmy', 99999)")
cursor.execute("INSERT INTO scoreboard VALUES ('eve', 50000)")
connection.commit()