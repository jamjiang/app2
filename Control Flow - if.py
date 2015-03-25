__author__ = 'jamjiang'
number=23
guess =int(input('enter an number:'))
if guess == number:
    print('congraulations, you guessed it.')
    print('(but u do not win any prizeds!)')
elif guess < number:
    print('no, higher')
else:
    print('no, lower')
print('Done')