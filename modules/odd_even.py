def add():
    a = ['Even','Odd']
    print(f'the entered value is : {a[int(input("enter Your Number:"))%2]}')
    


def add_num():
    a = int(input('Enter first number:')) 
    b = int(input('enter Second number:')) 
    l1 = '0' * a
    l2 = '1' * b
    print(len(f'{l1}{l2}'))
