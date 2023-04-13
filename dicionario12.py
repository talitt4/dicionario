votos = {}

while True:
    candidato = input("digite o nome do candidato (ou 'fim' para encerrar): ")
    if candidato == 'fim':
        break
    
    #verifica se o candidato ja recebeu voto antes
    if candidato in votos:
        votos[candidato] += 1
    else:
        votos[candidato] = 1
        
    # Imprime o resultado da votação
print("Resultado da votação:")
for candidato, quantidade in votos.items():
    print(candidato, "-", quantidade, "votos")
    
    print(votos)
        
        