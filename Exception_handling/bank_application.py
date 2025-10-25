class Mismatcherror(Exception):
    pass

try:
    bal = int(input('Enter your Balance:'))
    while True:
        option = int(input('1. Withdraw\n2. Deposit\n3. Check Balance\n4. Exit\nEnter your option:'))
        match option:
            case 1:
                try:
                    amt = int(input('Enter Amount:'))
                    if 0<=amt<=bal:
                        bal-=amt
                        print(f'Your Balance after withdraw is {bal}')
                    else:
                        raise Mismatcherror('Insufficient Balance')
                        
                except Exception as e:
                    print("Error:",e)
                    
            case 2:
                try:
                    amt = int(input('Enter Amount:'))
                    if 0<=amt<=5000:
                        bal+=amt
                        print(f'Your Balance after Deposit is {bal}')
                    else:
                        raise Mismatcherror('Deposit limit exceeded')
                except Exception as e:    
                    print("Error:",e)
                    
            case 3:
                print(f'Your Balance is {bal}')
            
            case _:
                print('Invalid Option')
                continue
        break
                
except ValueError as e:
    print('Error:',e)