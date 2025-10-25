class NotequalError(Exception):
    pass
try:
    a = 10
    b = 20
    if a!=b:
        raise NotequalError('Not Equal Error')
except NotequalError as e:
    print('error:',e)
    
# step 1 
#     create a class for custom Error
# step 2
#     inherit the properties of exception class
# step 3
#     pass

