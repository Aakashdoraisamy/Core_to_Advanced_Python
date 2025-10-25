"""
1) Register(try block)
    username
    password
    confirm password
    
    check length of username
    if 10 ask password and confirm
    
    if both password not same raise custom error
    
    exception
    
2) if no error in try block

else block
    print("register successfully")

"""
class missmatcherror(Exception):
    pass
try:
    username = input('Enter Your Username:')
    if len(username) == 10:
        password = eval(input('Enter Your Password:'))
        confirm_password = eval(input('Enter Your Password to confirm:'))
        if password != confirm_password:
            raise missmatcherror("Provide correct password....")

except Exception as e:
    print('Error:',e)
else:
    print('Register Successfully....')
    
    
    
class PasswordError(Exception):
    def __init__(self,error = 'Default Error'):
        super().__init__(error)
try:
    raise PasswordError('New Error')
    username = input('Enter Your Username:')
    if len(username) == 10:
        password = eval(input('Enter Your Password:'))
        confirm_password = eval(input('Enter Your Password to confirm:'))
        if password != confirm_password:
            raise PasswordError()

except Exception as e:
    print('Error:',e)
else:
    print('Register Successfully....')

"""
- once raise keyword executes it directly goes to except block. 
- raise keyword is similar like return keyword once the keyword executes the remaining line will not execute.
"""

    