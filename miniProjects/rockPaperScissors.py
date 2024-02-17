import random

userWins = 0
computerWins = 0

options = ['pedra','papel','tesoura']

print('\n\n\nVamos jogar!!!\n\n\n')

while True:
    userChoice = input('Escolha Pedra/Papel/Tesoura ou S para sair: ').lower()

    if userChoice == 's':
        break

    if userChoice not in options:
        continue
    
    randomNumber = random.randint(0, 2)
    # pedra: 0, papel: 1, tesoura: 2
    
    computerChoice = options[randomNumber]
    print(f'\nComputador escolhe {computerChoice}.\n')

    if userChoice == computerChoice:
        print('Empate!\n')
        continue

    if userChoice == 'pedra' and computerChoice == 'tesoura':
        print('Você ganhou!\n')
        userWins += 1

    elif userChoice == 'papel' and computerChoice == 'pedra':
        print('Você ganhou!\n')
        userWins += 1

    elif userChoice == 'tesoura' and computerChoice == 'papel':
        print('Você ganhou!\n')
        userWins += 1
    
    else:
        print('Você perdeu!\n')
        computerWins += 1
        
print(f'Você ganhou {userWins} pontos!\n')
print(f'O computador ganhou {computerWins} pontos!\n')
print('Até mais!\n')