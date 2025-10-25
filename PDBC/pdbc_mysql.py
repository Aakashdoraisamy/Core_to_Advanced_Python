import mysql.connector
import random

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Aakash@0310',
    database = 'students'
)

print('Database connected successfully......')

cursor = conn.cursor(buffered=True)

# cursor.execute('''CREATE TABLE user_details (
#     user_name VARCHAR(20),
#     mail_id VARCHAR(50),
#     mobile_no BIGINT,
#     otp INT,
#     pass VARCHAR(20)
# )''')

# print("Table created successfully!")

def register():
    user_name = input('Enter your name:')
    mail_id = input('Enter your mail id:')
    mobile_no = int(input('Enter your mobile number:'))
    otp = random.randint(1000,9999)
    u_otp = int(input(f'OTP : {otp}\nEnter OTP:'))
    if otp == u_otp: 
        u_pass = input('Enter your password:')
        if u_pass == input('Confirm Password:'):
            cursor.execute('''INSERT INTO user_details (user_name, mail_id, mobile_no, otp, user_password)
                    VALUES (%s, %s, %s, %s, %s)''',
                (user_name, mail_id, mobile_no, otp, u_pass))
            conn.commit()
        else:
            print('register failed...')
    else:
        print('OTP mismatch...')
register()


def login():
    user_name = input('Enter Your Name:')
    password = input('Enter Your Password:')


cursor.close()
conn.close()