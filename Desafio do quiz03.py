print('''  Quantos gols o flamengo vai fazer na Copa do Brasil?  
a - 1
b - 2
c - 3
''')
resposta = input().lower()

if resposta == "a":
    print(" Vai para os pênaltis! ")
elif resposta == "b":
    print("  Resultado milagroso!  ")
elif resposta == "c":
    print("  Goleada maravilhosa!  ")
else:
    print("  Você escolhe resultado diferente de a,b ou c!  ")
