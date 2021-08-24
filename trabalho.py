import sys

if len(sys.argv) < 3:
    print("Número incorreto de argumentos. Utilize nesse formato: python trabalho.py entrada.txt saida.txt")
    sys.exit() # Encerra a execução do programa
  
entrada = open(sys.argv[1],'r') # Lê uma entrada TXT que contém o total de vértices / arestas na linha 1, e nas demais: os vértices que formam cada aresta, e seu respectivo peso.

primeiraLinha = entrada.readlines(1)[0].split(' ')

totalDeVertices = int(primeiraLinha[0])
totalDeArestas = int(primeiraLinha[1])

listaDeRelacionamentos = list() # Declaramos um dicionário com a finalidade de armazenar os relacionamentos entre os vértices e também seus respectivos pesos.
relacionamentos = dict(listaDeRelacionamentos)

listaDeMenorCaminho = list() # Declaramos um dicionário com a finalidade de armazenar o menor caminho até um certo vértice.
menorCaminho = dict(listaDeMenorCaminho)

listaDeVerticeMaisProximo = list() # Declaramos um dicionário com a finalidade de armazenar o vértice mais próximo a outro vértice.
verticeMaisProximo = dict(listaDeVerticeMaisProximo)

for linha in entrada: # Preenche o vetor de relacionamentos e inicializa o vetor de menorCaminho e verticeMaisProximo.
    primeiroVertice = int(linha.split()[0])
    segundoVertice = int(linha.split()[1])
    pesoAresta = int(linha.split()[2])

    if primeiroVertice not in relacionamentos: # Cria uma chave que não existe ainda no vetor de relacionamentos.
        relacionamentos[primeiroVertice] = list()

    relacionamentos[primeiroVertice].append([segundoVertice, pesoAresta]) # Adiciona o relacionamento X Y e seu respectivo peso.
    
    if primeiroVertice not in menorCaminho: # Preenche o vetor de menorCaminho e verticeMaisProximo com valores ainda desconhecidos, informando que o mesmo ainda não foi visitado.
        menorCaminho[primeiroVertice] = -1  
        verticeMaisProximo[primeiroVertice] = -1   
    if segundoVertice not in menorCaminho:
        menorCaminho[segundoVertice] = -1
        verticeMaisProximo[segundoVertice] = -1   

entrada.close()

# print('RELACIONAMENTOS:',relacionamentos)
# print('MENOR CAMINHO:',menorCaminho)
# print('VÉRTICE MAIS PRÓXIMO:',verticeMaisProximo)

for vertice in menorCaminho: # Percorre todos os vértices do grafo.
    if vertice == 1: # Caso o vértice seja o primeiro, a distância até ele mesmo é 0.
        menorCaminho[vertice] = 0

    if vertice in relacionamentos: # Se o vértice tem algum relacionamento com outro vértice.
        for verticeAdjacente in relacionamentos[vertice]: # Percorre todos os vértices adjacentes ao vértice atual.
            adjacente = verticeAdjacente[0] # Captura o vértice adjacente ao ao vértice atual.
            pesoAresta = verticeAdjacente[1] # Peso da aresta formada pelos dois vértices.

            if menorCaminho[adjacente] == -1 or pesoAresta < menorCaminho[adjacente]: # Caso o caminho ainda não tenha sido visitado ou tenha sido encontrado um caminho menor.
                menorCaminho[adjacente] = menorCaminho[vertice] + pesoAresta # O novo caminho de adjacente é o caminho até o vértice atual + pesoAresta.
                verticeMaisProximo[adjacente] = vertice # Informamos qual o vértice mais próximo de adjacente.

        # print('MENOR CAMINHO', vertice, '° EXECUÇÃO :', menorCaminho)
        # print('VERTICE PRÓXIMO', vertice, '° EXECUÇÃO :', verticeMaisProximo, '\n')

ultimoVertice = len(menorCaminho) # Maior valor de vértice, ou seja, o último.

arquivo = open(sys.argv[2], "w") # Escreve a saída (resposta).

linhas = list() # Inicializa o vetor de linhas, para no fim adicioná-lo ao arquivo TXT de saída.

verticesInternosNoCaminho = list()

while verticeMaisProximo[ultimoVertice] != 1: # Preenche verticesInternosNoCaminho, executando enquanto não chegar no vértice inicial, tendo em vista que partimos do vértice final.
    verticesInternosNoCaminho.append(verticeMaisProximo[ultimoVertice])
    ultimoVertice = verticeMaisProximo[ultimoVertice]

verticesInternosNoCaminho = verticesInternosNoCaminho[::-1] # Inverte os valores do vetor, para imprimir como solicitado.

linhas.append(str(len(verticesInternosNoCaminho)) + '\n') # Adiciona o total de números na primeira linha, assim como é solicitado o retorno.
print(str(len(verticesInternosNoCaminho)))

for i in range(len(verticesInternosNoCaminho)): # Adiciona os demais vértices internos do menor caminho nas demais linhas.
    linhas.append(str(verticesInternosNoCaminho[i]) + '\n')
    print(str(verticesInternosNoCaminho[i]))

arquivo.writelines(linhas) 

arquivo.close()