print('''Qual o resultado do problema 'Qual é a raiz quadrada de 5184?
a-72
b-58
      ''')
resposta = input().lower()
score1 = (f'Muito bem!')
score2 = (f'Tente novamente!')

if resposta == "a":
    print(score1)
else:
    print(score2)