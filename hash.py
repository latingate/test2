from gs_functions import *

stored_password = hash_password('ThisIsAPassWord')

print(f'hashed password {stored_password}')
print(verify_password(stored_password, 'ThisIsAPassWord'))
print(verify_password(stored_password, 'WrongPassword'))
