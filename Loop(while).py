__author__ = 'jamjiang'
number=23
GuessTime=1
running=True
while running:
    guess=int(input('enter an number:'))
    if guess == number:
        print('congraulations, you guessed it.')
        print('(but u do not win any prizeds!)')
        running=Fales
    elif guess < number:
        print('no, higher')
    else:
        print('no, lower')
    print 'guest time:',GuessTime
    GuessTime+=1
else:
    print('loop finish')
print('Done')