bal = int(input('Enter your Balance:'))
while True:
    option = int(input('1. Withdraw\n2. Deposit\n3. Check Balance\n4. Exit\nEnter your option:'))
    match option:
        case 1:
            amt = int(input('Enter Amount:'))
            if 0<=amt<=bal:
                bal-=amt
                print(f'Your Balance after withdraw is {bal}')
                break
            else:
                print('Insufficient Balance')
        case 2:
            amt = int(input('Enter Amount:'))
            if 0<=amt<=5000:
                bal+=amt
                print(f'Your Balance after Deposit is {bal}')
                break
            else:
                print('Deposit limit exceeded')
        case 3:
            print(f'Your Balance is {bal}')
            break
        case _:
            print('Invalid Option')