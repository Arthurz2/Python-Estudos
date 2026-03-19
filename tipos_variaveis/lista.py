# Declaração

minha_lista = [1 , 2, 3, 4, 5, "rocketseat", True, False]
minha_lista_numerica = [2 , 1, 3, 4, 5]

# Exibindo a lista
print("Minha lista de exemplo", minha_lista)

minha_lista[0] = "python"
print("Minha lista de exemplo", minha_lista)

# Exibindo elemento individual
print("minha_lista[0]:", minha_lista[0])

# Slice (Fatiamento)
print("minha_lista[1:7]", minha_lista[1:7])
print("minha_lista[:6]", minha_lista[:6])
print("minha_lista[2:]", minha_lista[2:])

# Métodos de lista
# Método append(): adiciona um elemento ao final da lista
minha_lista.append(6)
print("Após appende 6:", minha_lista)

# Método index busca o indice dentro da variavel
indice = minha_lista.index(6)
print("Indice do elemento 6:", indice)

# Método insert:Insere um elemento em um índice específico
minha_lista.insert(2, 10)
print("Após o inset(2,10):", minha_lista)

# Método pop
elemento_removido = minha_lista.pop(3)
print("Elemento removido:", elemento_removido)

# Método remove
minha_lista.remove(True)
print("Após o remove(True):", minha_lista) 

# Método sort
minha_lista_numerica.sort()
print("minha_lista_numerica após aplicação do sort:", minha_lista_numerica)