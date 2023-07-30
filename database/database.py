import sqlite3

# Initialize the database (must run to crate the login.db file)
def createDatabase():
    connection = sqlite3.connect("login.db")
    cursor =connection.cursor()
    # create a table with username and password
    cursor.execute("""CREATE TABLE IF NOT EXISTS login(
        username TEXT,
        password TEXT
    )""")
    connection.commit()
    connection.close()

# add a user to the database given username and password
def addAccount(username = "", password = ""):
    connection = sqlite3.connect("login.db")
    cursor =connection.cursor()
    # insert username and password
    cursor.execute(f"INSERT INTO login VALUES ('{username}', '{password}')")
    connection.commit()
    connection.close()

# Print the database
def printDatabase():
    connection = sqlite3.connect("login.db")
    cursor =connection.cursor()
    cursor.execute("SELECT * FROM login")
    print(cursor.fetchall())


# return True if user is in the database else return False
def checkAccount(username = "", password = ""):
    connection = sqlite3.connect("login.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM login WHERE username='{username}' and password='{password}'")
    data = cursor.fetchall()
    connection.close()
    if data == []:
        return False
    return True

# return True of username is available else return False
def checkUsernameIsAvailable(username = ""):
    connection = sqlite3.connect("login.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM login WHERE username='{username}'")
    data = cursor.fetchall()
    connection.close()
    if data == []:
        return True
    return False

# Delete user when username is passed, return False if deletion failed
def deleteAccount(username = ""):
    if checkUsernameIsAvailable(username):
        return False
    connection = sqlite3.connect("login.db")
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM login WHERE username='{username}'")
    connection.commit()
    connection.close()
    return True
