import re
regex = '^[az0-9]+[@]\w+[az0-9]+[.]+\w{2,3}$'
email = ''

def checker(email):
    choice = 'T'
    while choice=='T' or choice=='t':
        email = input('enter e-mail address: ')
        if(re.search(regex,email)):
            print('E-mail address is valid.')
        else:
            print('Invalid e-mail address')

        print('\n\nYou want to try again?')
        choice=input(str)

if __name__ == '__main__':
    checker(email)

    #not working