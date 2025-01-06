#%%
# ### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

quantidade = float(input("Digite a quantidade: "))
preco = float(input("Digite o preco: "))

if quantidade > 0 and preco > 0:
    print("Dados validos")
else:
    print("Dados invalidos")    
#%%

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

# - Temperaturas abaixo de 20°C devem ser classificados como 'Baixa'.
# - Temperaturas entre 20°C e 30°C devem ser classificados como 'Normal'.
# - Temperaturas acima de 30°C devem ser classificados como 'Alta'.

# Escreva um programa que leia uma temperatura e imprima a classificação correspondente.

temperatura = float(input("Digite a temperatura: "))

if temperatura < 20:
    print("Baixa")
elif 20 <= temperatura <= 30:
    print("Normal")
else:
    print("Alta")   
#%%
### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

if log['level'] == 'ERROR':
    print(log['message'])
#%%

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

idade = int(input("Digite a idade: "))
email = input("Digite o email: ")

if idade < 18 or idade > 65:
    print("Idade invalida")
elif '@' not in email:
    print("Email invalido")
else:
    print("Dados de usuario validos")   
#%%
### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

transacao = {'valor': 12000, 'hora': 20}

if transacao['valor'] > 10000 or (transacao['hora'] < 9 or transacao['hora'] > 18):
    print("Transacao suspeita")
#%%
### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto = input("Digite um texto: ").lower().split()
palavras = {}

for palavra in texto:
    if palavra not in palavras:
        palavras[palavra] = 1
    else:
        palavras[palavra] += 1

for palavra, quantidade in palavras.items():
    print(f"{palavra}: {quantidade}")

#%%
### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

numeros = [1, 2, 3, 4, 5]
minimo = min(numeros)
maximo = max(numeros)

normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]
print(normalizados)
#%%
### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando
lista = [
    {'nome': 'Alice', 'idade': 25, 'cidade': 'New York'},
    {'nome': 'Bob', 'idade': None, 'cidade': 'San Francisco'},
    {'nome': 'Charlie', 'idade': 30, 'cidade': None}    
]

for usuario in lista:
    if usuario['idade'] is None or usuario['cidade'] is None:
        continue
    print(f"Nome: {usuario['nome']}, Idade: {usuario['idade']}, Cidade: {usuario['cidade']}")

#%%
### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
pares = [x for x in numeros if x % 2 == 0]
print(pares)

#%%

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
from collections import defaultdict


vendas = [
    {'categoria': 'Eletrônico', 'quantidade': 10, 'preco': 100},
    {'categoria': 'Eletrônico', 'quantidade': 5, 'preco': 50},
    {'categoria': 'Alimentos', 'quantidade': 3, 'preco': 20},
    {'categoria': 'Alimentos', 'quantidade': 2, 'preco': 10},
    {'categoria': 'Eletrônico', 'quantidade': 8, 'preco': 80}
]
total_por_categoria = defaultdict(float)
# Calcula o total por categoria
for venda in vendas:
    categoria = venda['categoria']
    total_por_categoria[categoria] += venda['quantidade'] * venda['preco']

# Exibe o resultado
for categoria, total in total_por_categoria.items():
    print(f"{categoria}: {total}")
#%%
### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

while True:
    palavra = input("Digite uma palavra: ")
    if palavra == "sair":
        break

#%%
### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

while True:
    numero = int(input("Digite um numero: "))
    if numero >= 1 and numero <= 10:
        break

#%%
### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

import time

def simular_api_paginada(pagina_atual):
    """
    Simula o consumo de uma API paginada.
    Retorna um dicionário com os dados da página atual e a informação sobre a próxima página.
    """
    # Dados simulados (como se fossem retornados pela API)
    dados_por_pagina = {
        1: {"dados": ["item1", "item2", "item3"], "proxima_pagina": 2},
        2: {"dados": ["item4", "item5"], "proxima_pagina": 3},
        3: {"dados": ["item6", "item7", "item8", "item9"], "proxima_pagina": None},
    }
    
    # Simula a resposta da API (com um pequeno atraso para parecer mais real)
    time.sleep(1)
    return dados_por_pagina.get(pagina_atual, {"dados": [], "proxima_pagina": None})


def consumir_api_paginada():
    """
    Processa todas as páginas de dados retornadas pela API simulada até que não haja mais páginas.
    """
    pagina_atual = 1
    while pagina_atual is not None:
        # Consome a página atual
        resposta = simular_api_paginada(pagina_atual)
        dados = resposta["dados"]
        proxima_pagina = resposta["proxima_pagina"]
        
        # Processa os dados da página atual
        print(f"Processando página {pagina_atual}: {dados}")
        
        # Atualiza para a próxima página
        pagina_atual = proxima_pagina
    
    print("Todas as páginas foram processadas!")


# Executa o simulador
consumir_api_paginada()
#%%
### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
import random
import time

def tentar_conectar():
    """
    Simula a tentativa de conexão a um serviço.
    Retorna True se a conexão for bem-sucedida, False caso contrário.
    """
    # Simula sucesso ou falha aleatoriamente (70% de chance de falhar)
    return random.random() > 0.7

def reconectar(max_tentativas):
    """
    Tenta se conectar ao serviço, com um limite máximo de tentativas.
    """
    tentativa = 0

    while tentativa < max_tentativas:
        tentativa += 1
        print(f"Tentativa {tentativa} de conexão...")

        if tentar_conectar():
            print("Conexão bem-sucedida!")
            return True  # Conexão foi estabelecida com sucesso
        else:
            print("Falha na conexão. Tentando novamente...")
            time.sleep(1)  # Simula espera entre tentativas

    print("Número máximo de tentativas atingido. Não foi possível conectar.")
    return False  # Não conseguiu se conectar após todas as tentativas

# Executa o simulador de reconexão
max_tentativas = 5
resultado = reconectar(max_tentativas)

if not resultado:
    print("Por favor, verifique o serviço e tente novamente mais tarde.")

#%%

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.
def processar_lista(lista, valor_parada):
    """
    Processa itens de uma lista até encontrar o valor de parada.
    """
    for item in lista:
        if item == valor_parada:
            print(f"Valor de parada '{valor_parada}' encontrado. Interrompendo o processamento.")
            break  # Encerra o loop ao encontrar o valor de parada
        print(f"Processando: {item}")
    else:
        print("Valor de parada não encontrado. Todos os itens foram processados.")

# Exemplo de uso
lista = [10, 20, 30, 40, 50, 60]
valor_parada = 40

processar_lista(lista, valor_parada)
# %%
