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
    cursor.execute("""CREATE TABLE IF NOT EXISTS daily_calories(
        username TEXT,
        calories TEXT,
        date TEXT
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

def addDailyCalories(username = "", calories = "", date = ""):
    connection = sqlite3.connect("login.db")
    cursor =connection.cursor()
    cursor.execute(f"INSERT INTO daily_calories VALUES ('{username}', '{calories}', '{date}')")
    connection.commit()
    connection.close()

def searchDailyCalories(username):
    connection = sqlite3.connect("login.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM daily_calories WHERE username=?", (username,))
    records = cursor.fetchall()
    connection.close()
    
    if not records:
        return {"message": "No daily calories found for the specified username."}
    
    # Convert the result into a list of dictionaries to represent JSON format
    daily_calories_list = []
    for record in records:
        daily_calories_list.append({
            "username": record[0],
            "calories": record[1],
            "date": record[2]
        })
    
        return {"daily_calories": daily_calories_list}