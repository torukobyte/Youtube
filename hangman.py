import random

def hangman():
    name = input('Enter your name: ')
    name = name.capitalize()
    print('Lets Start Playing {}!'.format(name))
    words = ['Goku','Obito','Sasuke','Naruto']
    words = [i.upper() for i in words]
    words = random.choice(words)
    guessess = ''
    loop = 10
    while loop >0:
        fail = 0
        for i in words:
            if i in guessess:
                print(i,end=' ')
            else:
                print('-',end=' ')
                fail += 1
        if fail == 0:
            print('\nYou Won!')
            break
        guess = input('\nEnter Your Guess: ')
        guess = guess.upper()
        guessess += guess
        if guess not in words:
            loop -= 1
            if loop == 0:
                print('You Lost,Word: {}'.format(words))
            else:
                print('Wrong Guess,{} round left!'.format(loop))

hangman()
