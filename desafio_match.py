'''
Atividade: Central de Atendimento Interativa | Dia 03/02
 
Objetivo:
Utilizar a estrutura match case para simular um menu de atendimento onde o usuário escolhe uma opção e o sistema retorna uma mensagem correspondente.
 
Enunciado:
 
Você foi contratado para criar um menu interativo de atendimento para uma empresa fictícia. O sistema deve exibir as opções abaixo e, de acordo com o número digitado, apresentar uma resposta:

Opções do menu:

[1] Falar com atendente
[2] Segunda via de boleto
[3] Cancelar serviço
[4] Informações sobre planos
[5] Sair
 
O que o programa deve fazer:
Mostrar o menu acima.
Receber a opção digitada pelo usuário.
Utilizar match case para responder com base na opção.
Exibir uma mensagem apropriada para cada caso.
Caso digite algo inválido, exibir: "Opção inválida, tente novamente!"
Critérios para o desafio estar completo:
Testar diferentes entradas para verificar todas as respostas.
Enviar o link do repositório com o Código

'''
print("Bem vindo ao atendimento WEB da Paraty, sou Lucas!!")
print("O que voê deseja fazer agora?")
print("[1] Falar com atendente\n[2] Segunda via de boleto \n[3] Cancelar serviço \n[4] Informações sobre planos \n[5] Sair")
print("coloque o número refente a opção desejada:")

opcao_usuario = int(input("Qual atendimento deseja?"))
opcao1 = "Falar com atendente"
opcao2 = "Segunda via de boleto"
opcao3 = "Cancelar serviço"
opcao4 = "Informações sobre planos"
opcao5 =  "Sair"

match opcao_usuario:
    case 1:
        print("Você quer:", opcao1)
    case 2:
        print("Você quer:", opcao2)
    case 3:
        print("Você quer:", opcao3)
    case 4:
        print("Você quer:", opcao4)
    case 5:
        print("Você quer:", opcao5)
    case _:
        print("Opção inválida, tente novamente!")