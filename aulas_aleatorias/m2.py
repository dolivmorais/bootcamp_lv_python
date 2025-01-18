#%%
#decisão
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

if n1 > n2:
    print(f"{n1} e maior que {n2}")
elif n2 > n1:
    print(f"{n2} e maior que {n1}")

#%%
letra = input("Digite uma letra: ")
lista = ["a", "e", "i", "o", "u"]

if letra in lista:
    print(f"{letra} e uma vogal")
else:
    print(f"{letra} e uma consoante")
#%%
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
print(f"A media das notas {nota1} e {nota2} = {media}")

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")  
#%%
salario = float(input("Digite o salario: "))
aumento = 0

if salario <= 280:
    aumento = salario * 0.2
elif salario > 280 and salario <= 700:
    aumento = salario * 0.15
elif salario > 700 and salario <= 1500:
    aumento = salario * 0.1
else:
    aumento = salario * 0.05

print(f"O salario de {salario} recebeu um aumento de {aumento}")
#%%
#repetição
for i in range(1, 11):
    print(f"Tabuada do {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()  # Pula uma linha
#%%
# escolha a tabulada
tabuada = int(input("Digite a tabuada desejada: "))

for i in range(1, 11):
    print(f"{tabuada} x {i} = {tabuada * i}")
#%%
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

for i in range(n1, n2 + 1):
    print(i)
#%%
nota1 = float(input("Digite a primeira nota: "))

while nota1 < 0 or nota1 > 10:
    print("Nota invalida")
    nota1 = float(input("Digite a primeira nota: "))    
else:
        print("Nota valida")
# %%
for i in range(1, 11):
    print(f"Tabuada do {i}:")
# %%
#dicionario
dicionario = {"chave1": "valor1", "chave2": "valor2"}
print(dicionario)
print(dicionario["chave1"])
print(dicionario["chave2"])

# %%
#Listas
alunos = ["joao", "maria", "pedro"]
for i in alunos:#alunos[1:]:
    print(i)
# %%
len(alunos)
# %%
alunos = ["joao", "maria", "pedro"]
alunos.append("jose")
print(alunos)

# %%
help(list)
# %%
#tuplas
tupla = ("joao", "maria", "pedro")
print(tupla[2])
# %%
tupla = ("joao", "maria", "pedro")
print(tupla[1])

# %%
tupla = ("joao", "maria", "pedro")
print(tupla[0:2])
# %%
tupla = ("joao", "maria", "pedro")
print(tupla[1:])

# %%
for i in tupla[1:]:
    print(i)
# %%
#string
frase = "Ola mundo"
for i in frase:
    print(i)

# %%
