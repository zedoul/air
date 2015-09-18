def validate(username, password):
    #your code here
    validator = Validator()
    if "||" in password or "//" in password:
        return 'Wrong username or password!',"Should fail to login because of injected code"
    if validator.login(username, password):
        return 'Successfully Logged in!',"Should succefully login!"
    else: 
        return 'Wrong username or password!', "The password was wrong"
