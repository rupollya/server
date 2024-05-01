import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3305,
    user="root",
    password="owIbyag820022013",
)
mycursor = connection.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS memo")
mycursor.execute("USE memo")
mycursor.execute(
    "CREATE TABLE Users (user_id INT AUTO_INCREMENT PRIMARY KEY , phone_number VARCHAR(11) UNIQUE, \
                 password VARCHAR(255), name VARCHAR(50), surname VARCHAR(50), email VARCHAR(255),\
                  about_me TEXT, photo BLOB)"
)
mycursor.execute(
    "CREATE TABLE NoteTemplates (template_id INT AUTO_INCREMENT PRIMARY KEY , template_name VARCHAR(255)\
        , template_text TEXT)"
)
mycursor.execute(
    "CREATE TABLE Notes (note_id INT AUTO_INCREMENT PRIMARY KEY , user_id INT, template_id INT, \
        title VARCHAR(30), text TEXT, created_at DATETIME, FOREIGN KEY (user_id) REFERENCES Users(user_id),\
              FOREIGN KEY (template_id) REFERENCES NoteTemplates(template_id))"
)
connection.commit()
mycursor.close()
connection.close()
