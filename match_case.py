# variaveis = caixinha com nome que guarda um valor
nome_sobrenome = "Lucas Bispo" # string
idade = 12 # int

#Calculadora simples

'''
Qual à a logica da calculadora ?

Precisa de valores (números)

1ªEtapa - Entrada: 
1.O usuário precisa digitar dois números ou mais
2. O usuário precisa falar qual operação math ele vai usar

2ªEtapa - Processamento:
Realizar operações matemáticas (+, -, * ou /)


3ªEtapa - Saída:
Exibir resultados das operações

'''
# STRING = "TEXTO
# INT = 10,11,22
# FLOAT = 10.2,10.3
# BOOLEAN = true ou false

print("+-*/=Bem vindo!! Calculadora do SENAC=/*-+")

primeiro_numero = input("Digite o primeiro número: ")
segundo_numero = input("Digite o segundo número: ")
operador = input("Digite o operador: ")

#ou poderia colocar float((input))


match operador:
    case "+": 
        print("O resultado é:", float(primeiro_numero) + float(segundo_numero))   
    case "-": 
        print("O resultado é:", float(primeiro_numero) - float(segundo_numero))  
    case "*": 
        print("O resultado é:", float(primeiro_numero) * float(segundo_numero))  
    case "/": 
        if float(segundo_numero) == 0:
            print("Erro, não podi dividir por 0")
        else:
            print("O resultado é:", float(primeiro_numero) / float(segundo_numero))  
    case _:
        print("operação invalida")