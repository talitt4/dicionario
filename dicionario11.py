agenda = ()

while True:
    nome = input("Digite o nome da pessoa: ")
    if nome == '':
        break
    
    telefone = input("digite o telefone: ")
    
    #adiciona o telefone ao dicionario
    agenda[nome] = telefone
    
    # Pesquisa um telefone na agenda
    nome_pesquisa = input("Digite o nome para pesquisar: ")
    if mome_pesquisa in agenda:
        print("Telefone de", nome_pesquisa, ":", agenda[nome_pesquisa])
    else:
        print("nome não encontrado na agenda")