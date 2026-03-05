
jogador = {}
 
for i in range(3): 
    nome = input("Digite o nome: ")
    pontuacao = input("Informe os pontoss iniciais:") 

    jogador[nome] = pontuacao

for player, pontucao in jogador.items(): 
    print(f"{player} | {pontuacao}")




    

    
