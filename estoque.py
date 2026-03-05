#criação do divisionário estoque
estoque = {

    "camisa":50,
    "calça":150, 
    "boné":35, 
    "tênis naique":350, 
}
#Mostrar estoque atual 
print("Estoque ataul: ")
for produto, quantidade in estoque.items(): 
    print(f"{produto} : {quantidade}")
#Pedindo dados para o usuário do sistema
nome_produto = input("Informe o nome do produto vendido: ")
quantidade_vendida = int(input("\nInforma a quantidade vendida: ")) 
#Atualizar o estoque
if quantidade_vendida <= estoque[nome_produto]: 
    estoque[nome_produto] = estoque[nome_produto] - quantidade_vendida
    print("Venda Realizada")
else: 
    print("Produto não encontrado")
    #Mostrar estoque atializado
    for produto, quantidade in estoque.items(): 
        print(f"{produto} | : {quantidade}")
        #Pedindo dados para o usuário do sistema
        nome_produto = int(input("\nInforme a quantidade de venda: "))
        #Atualizar o estoque
        if nome_produto in estoque: 
            if quantidade_vendida <= estoque[nome_produto] - quantidade_vendida
            print("Venda Realizada com sucesso!!! camisa")
        else: 
            print("Produto não encontrado") 
            #Mostrar estoque atualizado 
            for produto, quantidade in estoque.items(): 
                print(f"{produto} | {quantidade}")