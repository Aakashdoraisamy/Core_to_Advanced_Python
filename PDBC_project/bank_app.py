import sqlite3
import random

# Connect to your existing database

conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()

def get_cities():
    """Fetch unique city names from SBI_IFSC"""
    cursor.execute("SELECT DISTINCT CITY_NAME FROM SBI_IFSC;")
    return [row[0] for row in cursor.fetchall()]

def get_branches(city):
    """Fetch branch names for the selected city"""
    cursor.execute("SELECT BRANCH_NAME FROM SBI_IFSC WHERE CITY_NAME = ?;", (city,))
    return [row[0] for row in cursor.fetchall()]

def get_branch_details(branch_name):
    """Fetch IFSC and bank name for the branch"""
    cursor.execute("SELECT ifsc_code, BANK_NAME, CITY_NAME FROM SBI_IFSC WHERE BRANCH_NAME = ?;", (branch_name,))
    return cursor.fetchone()

def register_user():
    print("\n========== REGISTER PAGE ==========")
    full_name = input("Enter your full name : ").strip()
    username = input("Enter username : ").strip()

    # Username check
    cursor.execute("SELECT username FROM AccountDetails WHERE username = ?;", (username,))
    if cursor.fetchone():
        print("Username already exists! Try another.")
        return

    # Choose city
    print("\nSelect City:")
    cities = get_cities()
    for i, city in enumerate(cities, start=1):
        print(f"{i}. {city}")
    try:
        city_choice = int(input("Enter your option : "))
        city_selected = cities[city_choice - 1]
    except (ValueError, IndexError):
        print("Invalid city selection!")
        return

    # Choose branch
    print("\nSelect Branch:")
    branches = get_branches(city_selected)
    for i, branch in enumerate(branches, start=1):
        print(f"{i}. {branch}")
    try:
        branch_choice = int(input("Enter Option : "))
        branch_selected = branches[branch_choice - 1]
    except (ValueError, IndexError):
        print("Invalid branch selection!")
        return

    # Get IFSC, Bank name, city
    branch_info = get_branch_details(branch_selected)
    if not branch_info:
        print("Branch not found in database.")
        return
    ifsc_code, bank_name, city_name = branch_info
    print(f"\nSelected Branch Code: {ifsc_code}")
    print(f"Branch Name: {branch_selected}")

    # OTP verification step
    otp = random.randint(1000, 9999)
    print(f"\n(For demo) Your OTP is: {otp}")
    u_otp = input("Enter OTP to verify: ")

    if str(otp) != u_otp:
        print("OTP mismatch... Registration failed!")
        return

    # Password validation
    password = input("Enter your password : ")
    confirm = input("Confirm Password : ")

    if password != confirm:
        print("Passwords do not match! Registration failed.")
        return

    # Generate account number & balance
    acc_no = random.randint(100000000000, 999999999999)
    balance = 0

    # Insert new user into AccountDetails
    cursor.execute("""
        INSERT INTO AccountDetails 
        (username, password, branchname, bankname, branchcode, city_name, account_number, bank_balance, full_name)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, (username, password, branch_selected, bank_name, ifsc_code, city_name, acc_no, balance, full_name))
    conn.commit()

    print("\n Registration Successful!")
    print(f"Welcome {full_name}, your account number is {acc_no}\n")

def login_user():
    print("\n========== LOGIN PAGE ==========")
    username = input("Enter username : ").strip()
    password = input("Enter password : ").strip()

    cursor.execute("SELECT * FROM AccountDetails WHERE username = ? AND password = ?;", (username, password))
    user = cursor.fetchone()

    if user:
        print(f"\n Login Successful! Welcome {user[-1]}")
        print(f"City: {user[6]} | Branch: {user[3]} | IFSC: {user[5]}")
        print(f"Account No: {user[7]} | Balance: ₹{user[8]}")
    else:
        print("Invalid username or password!")

def main():
    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Enter your option : ")

        if choice == "1":
            login_user()
        elif choice == "2":
            register_user()
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
