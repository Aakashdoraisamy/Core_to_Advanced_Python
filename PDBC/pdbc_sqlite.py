import sqlite3

## step 1: connect the db file

conn = sqlite3.connect('my_database.db')

## if the db is present it will connect if not exist it will create a new db file as we mentioned name

## Step 2: Create table (if it doesn’t already exist)
 
conn.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEE
             (ID INT NOT NULL,
              NAME TEXT NOT NULL,
              AGE INT NOT NULL);''')

conn.commit()
print("Table created successfully!")

## Step 3: Insert records into EMPLOYEE table

conn.execute('''INSERT INTO EMPLOYEE (ID, NAME, AGE) VALUES (1, 'Aakash', 21)''')
conn.execute('''INSERT INTO EMPLOYEE (ID, NAME, AGE) VALUES (2, 'Rahul', 18)''')

conn.commit()
print("Records inserted successfully!")

conn.close()