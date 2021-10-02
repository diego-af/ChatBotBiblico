import os

def processar_resposta(resposta, nome):
  if resposta == '1':
    print(f'{os.linesep} {nome}, O fim principal do homem é glorificar a Deus e alegrar-se nele para sempre{os.linesep}Rm 11:36;1Co 10:31; Is 43:7{os.linesep} ')
  elif resposta == '2':
       print(f'{os.linesep}{nome},A princpal coisa que as Escrituras nos enisnam é o que o homem deve crê acerca de Deus, bem como o dever que Deus requer do homem{os.linesep}Jo 5:29; Jo 20:31; Sl 119:105 {os.linesep} ')
  elif resposta == '3':
       print(f'{os.linesep}{nome},Deus é Espirito, infito, etermo e imutavel em seu ser,sabedoria, poder,satidade, justiça, bondade e verdade{os.linesep} Jo 4:24; Sl 90:2; Rm 11:33{os.linesep} ')
  elif resposta == '4':
       print(f'{os.linesep} {nome},Não. Há um só Deus, o Deus vivo e verdadeiro{os.linesep} Dt 6:4; 1Co 8:4; Jr 10:10; Jo 17:3 {os.linesep} ')
  else:
    print('Digite 1, 2 ,3 ou 4')  



def start():
  nome = input('\n Digite seu nome: ')
  print(f'Ola {nome} ! Seja bem vindo, eu sou o Calvininho, vamos lá ?')

  

  while True:
    resposta = input(f'O que gostaria de saber hoje sobre o Breve catecismo de Westminster ? hoje você tem essas opções{os.linesep} [1]- Qual o fim princiapal do homem ?{os.linesep}[2]-Qual a principal coisa que as Escrituras nos ensinam?{os.linesep}[3]- O que é Deus?{os.linesep}[4] Há mais de um Deus?{os.linesep}')

    processar_resposta(resposta, nome)


if __name__ =='__main__':
  start()


