# Declaração 
nome_completo = "Arthur Eduardo"
nomeCompleto = "Arthur Eduardo"

# Declaração de variavel em varias linhas
nome_completo_aspas = """ Gabriel 
Casemiro """

nome_completo_quebra = "Gabriel \
Casemiro "

nome = "Gabriel"
sobreNome = "Casemiro"

#Formatação
print("Nome completo (1a forma):", nome_completo)
print("Nome completo (2a forma):" + nome_completo)
print("Nome completo (3a forma):" + "Gabriel" + "Casemiro")
print("Nome completo (4a forma):" "Gabriel", "Casemiro")
print("Nome completo (5a forma):", nome_completo_aspas )
print("Nome completo (6a forma):", nome_completo_quebra )
print("Nome completo (7a forma): %s" % nome_completo)
print("Nome completo (8a forma): %s %s" % (nome, sobreNome)) # transformação de valores em string na formatação 

#Novas formas o f você coloca antes da string e {} operações , variaveis e funções
print(f"Nome completo (9a forma): {nome} {sobreNome} " ) # melhor visivelmente agradavel