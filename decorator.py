
user_details = {'name':'Bharath', "type":"admin", "password":"123"}

def get_admin_password():
    return user_details['password']

def make_secure(func):
    def secure_function():
        if user_details['type'] == 'admin':
            return func()
    return secure_function
    
get_admin_password = make_secure(get_admin_password)  
print(get_admin_password())