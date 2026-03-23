#if, elif e else

idade = int(input("Quantos anos voce tem? "))
#ou
#idade = int(idade) para converter em inteiro
print("Exemplo de comando if")

if idade >= 18:
    print("Voce é maior de idade.")
elif idade >= 12:
    print("Voce é um adolescente.")
else:
    print("Voce é menor de idade.")

mensagem = "Pode tirar a carteira de habilitação" if idade >= 18 else "Voce não pode tirar a carteira de habilitação"
print(mensagem)

"""
if idade >= 18:
    print("Voce é maior de idade.")

if idade == 19:
    print("Voce tem 19 anos")

if idade < 18:
    print("Voce é menor de idade")

if idade != 10:
    print("Voce não tem 10 anos")"""