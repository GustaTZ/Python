# Calculadora Py
while True:

    # Perguntar qual é o tipo de operação
    print("(1) Adição (2) Subtração (3) Multiplicação (4) Divisão")
    operacao = input('Qual opreração (1, 2, 3, 4)? ou \'Q\' para sair ')
    if operacao == 'Q' or operacao == 'q':
        break
        operacao = int

    elif operacao == '1' or operacao == '2' or operacao == '3' or operacao == '4':    
        # Pergunta o primeiro numero
        num1 = int(input('Digite o primeiro numero: '))

        # Pergunta o segundo numero
        num2 = int(input('Digite o segundo numero: '))

        # Calcula os numeros
        if operacao == '1':
            resultado = num1 + num2

        elif operacao == '2':
            resultado = num1 - num2

        elif operacao == '3':
            resultado = num1 * num2

        elif operacao == '4':
            resultado = num1 / num2

        else:
            print('Operação Invalida')

        # Imprimir o resultado na tela
        print(resultado)
        
        break