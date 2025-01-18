"""Desafio 1: Contando Ocorrências (Básico)
Dado uma lista de palavras, conte quantas vezes cada palavra aparece na lista e armazene os resultados em um dicionário.

Entrada:
palavras = ["python", "java", "python", "c", "java", "java", "python"]

Saída esperada:
{"python": 3, "java": 3, "c": 1}

palavras = ["python", "java", "python", "c", "java", "java", "python"]

ocorrecia = {} # inicializa o dicionário

for palavra in palavras: # percorre a lista
    if palavra not in ocorrecia: # verifica se a palavra nao esta no dicionario
        ocorrecia[palavra] = 1 # inicializa com 1
    else:
        ocorrecia[palavra] += 1 # adiciona 1

print(ocorrecia)

------------------
Desafio 2: Invertendo o Dicionário (Intermediário)
Crie uma função que inverta as chaves e valores de um dicionário. Suponha que os valores sejam únicos.
Entrada:
dicionario = {"a": 1, "b": 2, "c": 3}
Saída esperada:
{1: "a", 2: "b", 3: "c"}

------------------
dicionario = {"a": 1, "b": 2, "c": 3} # inicializa o dicionário

def invertir_dicionario(dicionario): # cria a funcao
    invertido = {} # inicializa o dicionario
    for chave, valor in dicionario.items(): # percorre o dicionario
        invertido[valor] = chave # inverte
    return invertido # retorna

print(invertir_dicionario(dicionario))

----------------------

Desafio 3: Mesclando Dicionários (Intermediário)
Escreva uma função que combine dois dicionários. Se houver chaves repetidas, some os valores correspondentes.
Entrada:
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 15, "c": 25, "d": 35}
Saída esperada:
{"a": 10, "b": 35, "c": 55, "d": 35}
----------------

dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 15, "c": 25, "d": 35}

def mesclar_dicionarios(dict1, dict2): # cria a funcao
    mesclado = dict1.copy() # copia o dicionario
    for chave, valor in dict2.items(): # percorre o dicionario
        if chave in mesclado: # verifica se a chave esta no dicionario
            mesclado[chave] += valor # soma o valor
        else:
            mesclado[chave] = valor # adiciona o valor
    return mesclado # retorna

print(mesclar_dicionarios(dict1, dict2))
----------------

Desafio 4: Ordenando por Valor (Avançado)
Dado um dicionário, ordene-o pelo valor em ordem decrescente e retorne uma lista de tuplas.

Entrada:
dicionario = {"a": 5, "b": 2, "c": 9, "d": 1}
Saída esperada:

[("c", 9), ("a", 5), ("b", 2), ("d", 1)]

dicionario = {"a": 5, "b": 2, "c": 9, "d": 1}

def ordenar_dicionario(dicionario): # cria a funcao
    ordenado = sorted(dicionario.items(), key=lambda x: x[1], reverse=True) # ordena o dicionario
    return ordenado # retorna   

print(ordenar_dicionario(dicionario))
"""
dados = {
    "a": {
        "nome": "Diego",
        "idade": 30,
        "cidade": "São Paulo"
    },
    "b": {
        "nome": "Maria",
        "idade": 25,
        "cidade": "Rio de Janeiro"
    },
    "c": {
        "nome": "João",
        "idade": 35,
        "cidade": "Belo Horizonte"
    }
}
"""
Desafio 1: Acessando Dados (Básico)
Acesse e exiba:

A cidade onde Diego mora.
A idade de Maria.

Saída esperada:
São Paulo
25
print(dados["a"]["cidade"])
print(dados["b"]["idade"])
------------

Desafio 2: Adicionando uma Nova Pessoa (Básico)
Adicione uma nova pessoa ao dicionário com os seguintes dados:

Nome: Ana
Idade: 28
Cidade: Curitiba

dados["d"] = {
    "nome": "Ana",
    "idade": 28,
    "cidade": "Curitiba"
}   

for i in dados:
    print(dados[i])
    
"""





