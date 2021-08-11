entrada = open('entradas/entrada2.txt','r') # Lê uma entrada TXT que contém o total de vértices / arestas na linha 1, e nas demais: os vértices que formam cada aresta, e seu respectivo peso.

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

    if primeiroVertice not in caminhos: # Preenche o vetor de caminhos com valores ainda desconhecidos, informando que o mesmo ainda não foi visitado.
        caminhos[primeiroVertice] = -1   
    if segundoVertice not in caminhos:
        caminhos[segundoVertice] = -1     

    relacionamentos[primeiroVertice].append([segundoVertice, pesoAresta]) # Adiciona o relacionamento X Y e seu respectivo peso.

print('Relacionamentos:',relacionamentos)
print('Caminhos:',caminhos)

for vertice in caminhos: # Percorre todos os vértices do grafo.
    if vertice == 1: # Caso o vértice seja o primeiro.
        caminhos[vertice] = 0

    if vertice in relacionamentos: # Se o vértice tem algum relacionamento com outro vértice, que ainda não tenha sido verificado.
        for verticeAdjacente in relacionamentos[vertice]: # Percorre todos os vertices adjacentes do vertice atual.
            adjacente = verticeAdjacente[0] # Captura o vértice adjacente ao mesmo.
            pesoAresta = verticeAdjacente[1] # Peso da aresta dos dois vértices.

            if caminhos[adjacente] == -1 or pesoAresta < caminhos[adjacente]: # Caso o caminho ainda não tenha sido visitado ou tenha sido encontrado um caminho menor.
                caminhos[adjacente] = caminhos[vertice] + pesoAresta # O novo caminho até esse vértice é o caminho até o verticeAdjacente + peso da aresta.

        # print('Caminhos', vertice, ':', caminhos) # Imprimindo cada execução para via de teste.

print('Menores caminhos:',caminhos)

entrada.close()