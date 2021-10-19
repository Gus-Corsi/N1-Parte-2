# dicionario de alunos
Alunos = {'marco@yahoo.com.br': 'marco',
          'paulo@hotmail.com': 'paulo',
          'matheus@gmail.com': 'matheus',
          'jean@bol.com': 'jean',
          'bruna@outlook.com.br': 'bruna'
          'lucas@yahoo.com': 'lucas'}


# Mostrando a lista de alunos
def mostralist():
    print()
    for email, aluno in Alunos.items():
        print(f'Nome:', aluno.title(), '| Email: ', email)
    mostrarmenu()


# Mostrando a lista em ordem alfabetica
def mostra_alf():
    print()
    for email, aluno in sorted(Alunos.items()):
        print(f'Nome:', aluno.title(), '| Email: ', email)
    mostrarmenu()


# Excluindo um aluno
def excluiraluno():
    email = str(input("Digite o email do(a) aluno(a) que deseja excluir:\n"))
    if email in Alunos:
        del Alunos[email]
    else:
        print("Esse email não está cadastrado")
        mostrarmenu()
    mostra_alf()
    mostrarmenu()


# Criando um novo aluno
def novoaluno():
    nome = input("Digite o nome\n")
    email = input("Digite o email\n")
    Alunos[email] = nome
    mostralist()
    mostrarmenu()


# Procurar um aluno na lista
def procuraraluno():
    nome = str(input("Digite o nome do(a) aluno(a) que procura:\n"))
    if nome in Alunos.values():
        print(f"O aluno {nome} está cadastrado na lista de alunos!")
        mostrarmenu()
    else:
        print(f"\nNão encontramos nenhum(a) aluno(a) chamado {nome} na lista.")
        num = int(
            input("\nGostaria de adicioná-lo à lista? Digite 1 para sim e 0 para não."))
        if num == 1:
            novoaluno()
        else:
            mostrarmenu()


# Alterar nome de um aluno da lista
def alterarnome():
    email = str(input("Digite o email do(a) aluno(a) que procura:\n"))
    if email in Alunos:
        aluno = str(input("Qual o novo nome do(a) aluno(a)?\n"))
        Alunos.update({email: aluno})
        mostrarmenu()
    else:
        print("Esse email não está cadastrado")
        mostrarmenu()


# Funcao para mostrar o menu
def mostrarmenu():

    print("\nDigite 0 para sair")
    print("Digite 1 para cadastrar um aluno")
    print("Digite 2 para excluir um aluno")
    print("Digite 3 para exibir os alunos em ordem de cadastro")
    print("Digite 4 para exibir os alunos em ordem alfabética")
    print("Digite 5 para procurar um aluno")
    print("Digite 6 para alterar o nome de um aluno\n")
    escolha = int(input("Qual opção deseja?\n"))
    if escolha == 1:
        novoaluno()
    elif escolha == 2:
        excluiraluno()
    elif escolha == 3:
        mostralist()
    elif escolha == 4:
        mostra_alf()
    elif escolha == 5:
        procuraraluno()
    elif escolha == 6:
        alterarnome()
    elif escolha == 0:
        pass


print()
mostrarmenu()
