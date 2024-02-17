import random


topRange = input('Digite um número: ')

if topRange.isdigit():
    topRange = int(topRange)

    if topRange <=0 :
        print('Por favor, digite um número maior que 0: ')
        quit()
else:
    print('Por favo, digite um número da próxima vez\n')
    quit()

randomNumber = random.randint(0, topRange)

while True:
    userGuess = input(f'Tente adivinhar um número de 1 a {topRange}: \n')
    print(randomNumber)

    if userGuess.isdigit():
        userGuess = int(userGuess)

    else:
        print('Por favo, digite um número da próxima vez\n')
        continue

    if userGuess == randomNumber:
        print('Você conseguiu!\n')
        break
    else:
        print ('Você errou!\n')