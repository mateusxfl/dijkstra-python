entrada = open('entrada.txt','r') # Lê uma entrada TXT que contém o total de vértices / arestas na linha 1, e nas demais: os vértices que formam cada aresta, e seu respectivo peso.

primeiraLinha = entrada.readlines(1)[0].split(' ')

totalDeVertices = int(primeiraLinha[0])
totalDeArestas = int(primeiraLinha[1])

listaDeRelacionamentos = list() # Declaramos um dicionário com a finalidade de armazenar os relacionamentos entre os vértices e também seus respectivos pesos.
relacionamentos = dict(listaDeRelacionamentos)

listaDeCaminhos = list() # Declaramos um dicionário com a finalidade de armazenar o menor caminho de um vértice até outro.
caminhos = dict(listaDeCaminhos)

for linha in entrada: # Preenche o vetor de relacionamentos e inicializa o vetor de caminhos.
    primeiroVertice = int(linha.split()[0])
    segundoVertice = int(linha.split()[1])
    pesoAresta = int(linha.split()[2])
    # print(primeiroVertice,segundoVertice,pesoAresta)

    if primeiroVertice not in relacionamentos: # Cria uma chave que não existe ainda no vetor de relacionamentos.
        relacionamentos[primeiroVertice] = list()

    if primeiroVertice not in caminhos: # Inicializa o vetor de caminhos, que informa o menor caminho até um vértice.
        caminhos[primeiroVertice] = -1   
    elif segundoVertice not in caminhos:
        caminhos[segundoVertice] = -1        

    relacionamentos[primeiroVertice].append([segundoVertice, pesoAresta]) # Adiciona o relacionamento X Y e seu respectivo peso.

# print('Relacionamentos:',relacionamentos)
# print('Caminhos:',caminhos)

entrada.close()


