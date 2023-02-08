#########################################
#####      Daniel Marques       #########
#####   Projeto: Deu Match!     #########
#####  Data de criação 03/02/23 #########
#########################################


listaCandidatos = [] #Listas vazias de cada um dos conceitos que serão comparados dos usuários.
e = []
t = []
p = []
s = []
cont = 0


def dadosCandidato(): #Função que o usuário cadastra os candidatos com seus respectivos conceitos.
    sair = 0
    while sair != 1:
        candidato = (input("Digite o nome do candidato: \n"))
        conceitoE = int(input("Digite a nota da entrevista desse candidato: \n"))
        conceitoT = int(input("Digite a nota do teste teórico desse candidato: \n"))
        conceitoP = int(input("Digite a nota do teste prático desse candidato: \n"))
        conceitoS = int(input("Digite a nota da avaliação de soft skills desse candidato: \n"))
        sair = int(input("Deseja cadastrar mais algum canditado? digite 1 para não e 2 para sim: \n"))

        listaCandidatos.append(candidato)
        e.append(conceitoE)
        t.append(conceitoT)
        p.append(conceitoP)
        s.append(conceitoS)
    return


def criteriocandidato():  #Função que o usuário insere os critérios e em seguida printa os candidatos correspondentes.
    print("Nesta opção você irá inserir as notas minimas desejadas para cada conceito")
    ever = int(input("Digite a nota para o conceito entrevista: \n" ))
    tver = int(input("Digite a nota para o conceito teste teórico \n" ))
    pver = int(input("Digite a nota para o conceito teste prático: \n" ))
    sver = int(input("Digite a nota para o conceito soft skills: \n" ))
    for cont in range(len(listaCandidatos)):
        if e[cont] >= ever and t[cont] >= tver and p[cont] >= pver and s[cont] >= sver:
            print(listaCandidatos[cont],(f", e{e[cont]}_t{t[cont]}_p{p[cont]}_s{s[cont]}"))
    return

def menu(): #Função que serve como menu para o código.
    opcao = 0
    while opcao != 4:
        print("-" * 50)
        print("   Deu Match candidatos!")
        print("-" * 50)
        print("1- Cadastrar candidatos")
        print("2- Consultar candidatos por nota")
        print("3- Listar todos os candidatos")
        print("4- Sair")
        try:
            opcao = int(input("\n Opção: "))
        except:
            print("\n Opcão inválida, tente novamente.")
            continue
        if (opcao == 1):
            dadosCandidato()
        elif (opcao == 2):
            criteriocandidato()
        elif (opcao == 3):
            print("\n Resultado: ", listaCandidatos, "\n")
        elif (opcao == 4):
            print("\n Aplicativo encerrado. \n")
            break
        else:
            print("\n Opcão inválida, tente novamente.")


menu()





