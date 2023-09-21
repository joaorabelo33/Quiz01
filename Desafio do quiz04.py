print('''Qual o resultado do problema 'Qual é a raiz quadrada de 5184?
a-42
b-58
c-72
      ''')
resposta = input()
score = 0
pontuacao = score + 1

if resposta == "a":
    print("Resposta errada! Sua pontuação é.",score)
elif resposta == "b":
    print("Resposta errada! Sua pontuação é.",score)
elif resposta == "c":
    print("Resposta certa! Sua pontuação é.",pontuacao)
else:
    print("  Você escolhe resultado diferente de a,b ou c!  ")
