print("For utilizando lista")
lista = [1,2 ,3 ,4 , 5]
for elemento in lista:
    print(elemento)

print("For utilizando tupla")
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
    print(tupla)

pessoa = {"nome": "João", "idade":30, "cidade": "São Paulo"}
print("For utilizando dicionario - chaves")
for chave in pessoa.keys():
    print(chave)

print("For utilizando dicionario - valores")
for valor in pessoa.values():
    print(valor)


print("For utilizando dicionario - Itens")
for chave, valor in pessoa.items():
    print(f"{chave} : {valor}")


#range(): intervalo numérico
# [0,1,2,3,4,5,6,7,8,9]

print("Utilizando a função range()")

for numero in range(5):
    print("Numero:", numero)

print("Utilizando a função range() con len()")
lista = [1, 2, 3, 4, 5]
print(lista)
for indice in range(0, len(lista)):
    if indice == 3:
        lista[indice] = 5
        print(lista)
    else:
        lista[indice] = 0

# enumerate()
lista_enumerate = ["a", "b", "c", "d"]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")