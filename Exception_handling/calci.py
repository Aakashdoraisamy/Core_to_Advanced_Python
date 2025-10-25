try:
    def cal(a, b):
        while True:
            print("\nSelect the operation to perform....")
            print('1. Addition')
            print('2. Subtraction')
            print('3. Multiplication')
            print('4. Division')
            print('5. Floor Division')  
            print('6. Modulus')
            print('7. Exit')
            
            option = int(input('Enter Your Choice: '))
                
            match option:
                case 1:
                    print("Result:", a + b)
                case 2:
                    print("Result:", a - b)
                case 3:
                    print("Result:", a * b)
                case 4:
                    print("Result:", a / b)
                case 5:
                    print("Result:", a // b)
                case 6:
                    print("Result:", a % b)
                case 7:
                    print("Exiting calculator...")
                case _:
                    print('Invalid Choice.....')
                    raise ValueError('Invalid Option......')
            break  
    a = int(input("Enter Your First Number: "))
    b = int(input("Enter Your Second Number: "))
    cal(a, b)
except Exception as e:
    print("Error:", e)
