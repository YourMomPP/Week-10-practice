import mysql.connector

# 1. 2022113ho - Ho Areykal
# 2. 2022167chun - Chun Phallamonunhh
# 3. 2022128sophal - Sophal Kalyanchheny

# TODO:
# host can be 'localhost' or '127.0.0.1'
# if you are using mamp, password is root
# and port is 8889
# use cat_db as database.
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cat_db",
    port="3306"
)


cursor = mydb.cursor()


def register_cat(cat_info):
    '''
    TODO:
    cat_info is in a form of list ex: ["rose", "f", "Siberian", "2020-03-08", "smart one"], that register_cat function will insert the provided
    list to cats table as an insert record.
    '''
    sql = "INSERT INTO cats (name, gender, breed, dob, description) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, cat_info)
    mydb.commit()
    print("Registered successfully!")

test_data = ["rose", "f", "Siberian", "2020-03-08", "smart one"]
# register_cat(test_data)

def get_cats():
    sql = "SELECT * FROM cats"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result
    
# print(get_cats())

def get_cat(id):
    '''
    TODO:
    this function will get a single cat data from cat table base on the id parameter
    '''
    sql = f"SELECT * FROM cats WHERE id = '{id}'"
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

# print(get_cat(1))

def update_cat(cat_info):
    '''
    TODO:
    cat_info is in a form of list ex: [1,"rose", "f", "Siberian", "2020-03-08", "smart one"], 
    that update_cat function will use as 
    an update record for specific cat information where equal to cat_info[0]
    '''
    id, name, gender, breed, dob, description = cat_info
    sql = f"UPDATE cats SET name = '{name}', gender = '{gender}', breed = '{breed}', dob = '{dob}', description = '{description}' WHERE id = '{id}'"
    cursor.execute(sql)
    print("Updated successfully!")


def remove_cat(id):
    '''
    TODO:
    this function will remove record from cat table base on id parameter.
    '''
    sql = f"DELETE FROM cats WHERE id = '{id}'"
    cursor.execute(sql)
    mydb.commit()
    print("Removed successfully!")

# remove_cat(8)