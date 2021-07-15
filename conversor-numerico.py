num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('O número {} convertido para binário é igual a {}.' .format(num, bin(num) [2:]))
elif opção == 2:
    print('O número {} convertido para octal é igual a {}.' .format(num, oct(num) [2:]))
elif opção == 3:
    print('O número {} convertido para hexadecimal é igual a {}.' .format(num, hex(num) [2:]))
else:
    print('\033[31mOpção inválida. Tente novamente.\033[m')