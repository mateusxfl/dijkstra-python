entrada = open('entrada.txt','r') # Lê uma entrada TXT que contém o total de vértices / arestas na linha 1, e nas demais: os números que representam uma aresta, e seu respectivo peso.

primeiraLinha = entrada.readlines(1)[0].split(' ')

totalDeVertices = int(primeiraLinha[0])
totalDeArestas = int(primeiraLinha[1])

verticesNaoVisitados = list() # Inicia um vetor para verificar quais vértices ja foram visitados.

for x in range(0, totalDeVertices): # Inicia todos os vértices como nãoi visitados ( -1 )
    verticesNaoVisitados.append(-1)

print(verticesNaoVisitados)

entrada.close()


