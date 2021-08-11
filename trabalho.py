entrada = open('entrada.txt','r') # Lê uma entrada TXT que contém o total de vértices / arestas na linha 1, e nas demais: os vértices que formam cada aresta, e seu respectivo peso.

primeiraLinha = entrada.readlines(1)[0].split(' ')

totalDeVertices = int(primeiraLinha[0])
totalDeArestas = int(primeiraLinha[1])

listaDeRelacionamentos = list() # Declaramos um dicionário com a finalidade de armazenar os relacionamentos entre os vértices e também seus respectivos pesos.
relacionamentos = dict(listaDeRelacionamentos)

for linha in entrada: # Preenche o vetor de relacionamentos.
    primeiroVertice = int(linha.split()[0])
    segundoVertice = int(linha.split()[1])
    pesoAresta = int(linha.split()[2])
    # print(primeiroVertice,segundoVertice,pesoAresta)

    if primeiroVertice not in relacionamentos: # Cria uma chave que não existe ainda no vetor de relacionamentos.
        relacionamentos[primeiroVertice] = list()

    relacionamentos[primeiroVertice].append([segundoVertice, pesoAresta]) # Adiciona o relacionamento X Y e seu respectivo peso.

# print('Relacionamentos:',relacionamentos)

entrada.close()


