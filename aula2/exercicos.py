# #### Inteiros (`int`)
#%%
# # 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

print(f"A soma de {n1} + {n2} = {n1 + n2}")
#%%
# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
n3 = int(input("Digite um numero: "))
print(f"O resto da divisao de {n3} por 5 = {n3 % 5}")
#%%
# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
n4 = int(input("Digite o primeiro numero: "))
n5 = int(input("Digite o segundo numero: "))
print(f"A multiplicacao de {n4} * {n5} = {n4 * n5}")

#%%
# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
n6 = int(input("Digite o primeiro numero: "))
n7 = int(input("Digite o segundo numero: "))
print(f"A divisao inteira de {n6} / {n7} = {n6 // n7}")
#%%
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
n8 = int(input("Digite um numero: "))
print(f"O quadrado de {n8} = {n8 ** 2}")

# #### Números de Ponto Flutuante (`float`)
#%%
# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
n9 = float(input("Digite o primeiro numero: "))
n10 = float(input("Digite o segundo numero: "))
print(f"A soma de {n9} + {n10} = {n9 + n10}")
#%%
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
n11 = float(input("Digite o primeiro numero: "))
n12 = float(input("Digite o segundo numero: "))
print(f"A media de {n11} e {n12} = {(n11 + n12) / 2}")
#%%
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
n13 = float(input("Digite o primeiro numero: "))
n14 = float(input("Digite o segundo numero: "))
print(f"A potencia de {n13} elevado a {n14} = {n13 ** n14}")
#%%
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"A temperatura de {celsius} Celsius equivale a {fahrenheit} Fahrenheit") 
#%%
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio = float(input("Digite o raio do circulo: "))
area = 3.14 * raio ** 2
print(f"A area do circulo de raio {raio} equivale a {area}")
# #### Strings (`str`)


#%%
# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
frase = input("Digite uma frase: ")
print(frase.upper())
#%%
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome = input("Digite o seu nome: ")
print(nome.lower())
#%%
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input("Digite uma frase: ")
print(frase.strip())
#%%
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = data.split("/")
print(f"dia: {dia}, mes: {mes}, ano: {ano}")
#%%
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")
print(string1 + string2)    

# #### Booleanos (`bool`)
#%%
# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
expressao1 = input("Digite a primeira expressao booleana: ")
expressao2 = input("Digite a segunda expressao booleana: ")
print(f"O resultado da operacao AND entre {expressao1} e {expressao2} = {expressao1 and expressao2}")   
#%%
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
expressao1 = input("Digite a primeira expressao booleana: ")
expressao2 = input("Digite a segunda expressao booleana: ")
print(f"O resultado da operacao OR entre {expressao1} e {expressao2} = {expressao1 or expressao2}")
#%%
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
expressao1 = input("Digite a primeira expressao booleana: ")    
print(f"O valor invertido de {expressao1} = {not expressao1}")
#%%
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
print(f"Os numeros {n1} e {n2} sao iguais? {n1 == n2}") 
#%%
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
print(f"Os numeros {n1} e {n2} sao diferentes? {n1 != n2}")
