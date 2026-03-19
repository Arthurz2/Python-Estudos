# Criando um dicionario de exemplo

pessoa = {"nome": "João", "idade": 30, "cidade": "Contagem"}

print("Meu dicionário de exemplo:", pessoa)

# Acessando valores por chaves
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

pessoa["sobrenome"] = "Silva"
print("Sobrenome:", pessoa["sobrenome"])

pessoa["idade"] = 31
print("Idade:", pessoa["idade"])

# Removendo um par chave valor
del pessoa["sobrenome"]
print("Meu dicionário de exemplo:", pessoa)

# Métodos: keys(), vales(), items()

chaves = list(pessoa.keys())
print("Chaves do dicionário", chaves)
print("Primeira chave", chaves[0])

# values
valores = list(pessoa.values())
print("valores do dicionário", valores)

# Métodos items
itens = list(pessoa.items())
print("Pares chave-valor do dicionário", itens)
print("Primeiro valor: %s = %s" % (itens[0][0], itens[0][1]))