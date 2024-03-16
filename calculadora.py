import os

#2 Funções simples, porém necessárias.

def menu():
    print('-------------------------------')
    print('0 : Soma')
    print('1 : Subtração')
    print('2 : Multiplicação')
    print('3 : Divisão')
    print('4 : Exponenciação')
    print('5 : Encerrar')
    print('-------------------------------')

    opcao = int(input('Escolha a operação que deseja realizar:'))
    return opcao
   

def limpar_tela():
    os.system('cls' if os.name=='nt' else 'clear')

#Aqui eu fiz um definição de função para tornar uma variavel "local" em "global".

var_tela = limpar_tela()
var_menu = menu()

#Essa parte do codigo realiza ás operações da calculadora.

while True:

    match var_menu:
        case 0:
            n1 = float(input('Escolha o primeiro número: '))
            n2= float(input('Escolha o segundo número: '))
            soma = n1 + n2

            print(f'O resultado da sua soma é: {soma}')
            final = str(input('Deseja fazer outra operação?(Sim ou Não) '))

            if final == 'Sim':
                limpar_tela()
                var_menu = menu()
            elif final == 'Não':
                limpar_tela()
                break

        case 1:
            nu1 = float(input('Escolha o primeiro número: '))
            nu2 = float(input('Escolha o segundo número:'))
            subtracao = nu1 - nu2

            print(f'O resultado da sua subtração é: {subtracao}')
            final = str(input('Deseja fazer outra operação?(Sim ou Não) '))

            if final == 'Sim':
                limpar_tela()
                var_menu = menu()
            elif final == 'Não':
                limpar_tela()
                break

        case 2:
            num1 = float(input('Escolha o primeiro número: '))
            num2 = float(input('Escolha o segundo número:'))
            multiplicacao = num1 * num2

            print(f'O resultado da sua multiplicação é: {multiplicacao}')
            final = str(input('Deseja fazer outra operação?(Sim ou Não) '))

            if final == 'Sim':
                limpar_tela()
                var_menu = menu()
            elif final == 'Não':
                limpar_tela()
                break

        case 3:
            nume1 = float(input('Escolha o primeiro número: '))
            nume2= float(input('Escolha o segundo número: '))
            divisao = nume1 / nume2
                
            print(f'O resultado da sua divisão é: {divisao}')
            final = str(input('Deseja fazer outra operação?(Sim ou Não) '))

            if final == 'Sim':
                limpar_tela()
                var_menu = menu()
            elif final == 'Não':
                limpar_tela()
                break

        case 4:
            numero1 = float(input('Escolha o primeiro número: '))
            numero2 = float(input('Escolha o segundo número: '))
            exponenciacao = numero1 ** numero2

            print(f'O resultado da sua exponenciação é: {exponenciacao}')
            final = str(input('Deseja fazer outra operação?(Sim ou Não) '))

            if final == 'Sim':
                limpar_tela()
                var_menu = menu()
            elif final == 'Não':
                limpar_tela()
                break    
        
        case 5:
            break
        
        case _:
            print('-------------------------------')
            print("Tecla invalida. Pressione numeros de 1 à 5 ou 0.")
            
            var_menu = menu()