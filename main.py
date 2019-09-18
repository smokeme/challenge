def check_param(param,value):
    total = 0
    for letter in param:
         total += ord(letter)
    if ord != value:
        return False
    return True

def main_function():
    print('- Type `exit` to stop the application')
    print('- Try and find the secret key')
    while(1):
        print('- ')
        print('- Enter secret code:')
        user_input = input('> ')
        if (user_input == "exit"):
            print('- Thank you for trying!')
            exit()
        if (len(user_input) > 17):
            print('- Too long try again')
        else:
            user_input = user_input.split('-')
            if check_param("".join(user_input),1121):
                if check_param(user_input[0],377):
                    if check_param(user_input[0],225):
                        if check_param(user_input[0],519):
                            print('- Like a Boss')
            print('- Wrong code try again')


if __name__ == '__main__':
    main_function()















#hint, it should be something like this "my-secret-key"
