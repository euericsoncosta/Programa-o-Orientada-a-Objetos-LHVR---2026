escolha = ""
palavras = []

while escolha != "sair":
    escolha = input("Digite uma palavra (Sair para encerrar): ").lower()
    palavras.append(escolha)

for palavra in palavras:
    print(palavra)
i = 0
for palavra in palavras[:]:
    print(palavras)
    i += 1
    print(f"{i} - {palavra}")
    palavras.remove(palavra)


