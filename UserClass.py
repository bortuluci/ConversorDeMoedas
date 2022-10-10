import sqlite3
import requests
import json


conexao=sqlite3.connect('databaseusuarios.db')
cursor=conexao.cursor()


class User:
  def __init__(self,username=None,password=None,login=0):
    self.username=username
    self.password=password
    self.login=login
    
  def novoCadastro(self):
    print('\n########## CADASTRO ##########')
    username=str(input('Informe seu usuario para cadastro: '))
    password=str(input('Digite sua senha para cadastro: '))
    
    try:
      cursor.execute('INSERT INTO usuarios(username,password) VALUES (?,?)',(username,password))
      conexao.commit()
      print('Novo usuário cadastrado com sucesso!\n')
    except:
      print('Este usuário já existe')
      self.novoCadastro()
    
  def logando(self):
    print('\n########## LOGIN ##########')
    
    username_login=str(input('Username: '))
    password_login=str(input('Password: '))
    
    validacao=cursor.execute(f'SELECT username,password FROM usuarios WHERE username=? AND password=?',(username_login,password_login))
    
    i=' '
    for i in validacao:
      validacao=i
      
    if username_login == i[0] and password_login == i[1]:
      self.username=username_login
      self.password=password_login
      self.login=1 #0= Deslogado // 1= Logado
      print('Login efetuado.\n')
      logado = 0
      
    else:
      print('Erro! Login não efetuado.\n')
  
  def alterarSenha(self):
    if self.login == 1:
      print('\n########## ALTERAR SENHA ##########')
      
      senha_atual = str(input('Informe sua senha atual: '))
      
      validacao=cursor.execute(f'SELECT username,password FROM usuarios WHERE username=? AND password=?',(self.username,senha_atual))
      
      i=' '
      for i in validacao:
        validacao=i
        
      if self.username == i[0] and senha_atual == i[1]:
        senha_nova = str(input('Digite a nova senha: '))
        cursor.execute('UPDATE usuarios SET password = ? WHERE password = ? AND username = ?',(senha_nova,senha_atual,i[0]))
        self.password = senha_nova
        conexao.commit()
        print('Senha alterada com sucesso.\n')
        
      else:
        print('Erro! Dados informados não encontrados.\n')
        
    else:
      print('Você não está logado.')
  
  def excluirCadastro(self):
    if self.login == 1:
      print('\n########## EXCLUIR CADASTRO ##########')
      senha_atual=str(input('Informe sua senha atual: '))
      
      if self.password == senha_atual:
        cursor.execute(f'DELETE FROM usuarios WHERE username=? AND password=?',(self.username,senha_atual))
        conexao.commit()
        print(f'Cadastro de {self.username} foi excluído com sucesso.\n')
        self.login = 0
        self.excluirCadastro()
               
      else:
        print('Erro! A senha informada não confere.\n')
        return
        
    else:
      print('Você foi deslogado.')

  def principaisMoedas(self):
    if self.login == 1:
      print('\n########## PRINCIPAIS MOEDAS ##########\nARS - Peso Argentino\nBRL - Real Brasileiro [REFERÊNCIA]\nBTC - Bitcoin\nCAD = Dólar Canadense\nETH - Ethereum\nEUR - Euro [REFERÊNCIA]\nGBP - Libra Esterlina \nUSD - Dólar Americano [REFERÊNCIA]\n')
    else:
      print('Você não está logado.\n') 
   
  def converterMoedas(self):
    if self.login == 1: 
      moeda1=str(input('Informe a moeda: '))
      valor1=float(input('Informe o valor a ser convertido: '))
      moeda2= str(input('Informa a moeda de referência: '))
      
      
      cotacoes = requests.get(f'https://economia.awesomeapi.com.br/last/{moeda1}-{moeda2}')
      respostaApi=cotacoes.status_code #Retorna 200=OK // 404=Error
      cotacoes = cotacoes.json()
      if respostaApi == 200:
        cotacao_moeda = cotacoes[f'{moeda1.upper()}{moeda2.upper()}']['bid']
        cotacao_moeda=float(cotacao_moeda) #convertendo de string para float
        valor_final_moeda = cotacao_moeda*valor1 
        print(f'1 {moeda1.upper()} = {cotacao_moeda} {moeda2.upper()}')
        print(f'{valor1} {moeda1.upper()} = {valor_final_moeda} {moeda2.upper()}\n')   
      else:
        print('Moedas não reconhecidas.')  

  def visualizarDados(self):
    if self.login == 1:
      senha_atual = str(input('Informe sua senha atual: '))
      
      validacao=cursor.execute(f'SELECT username,password FROM usuarios WHERE username=? AND password=?',(self.username,senha_atual))
      
      i=' '
      for i in validacao:
        validacao=i

      if self.username == i[0] and senha_atual == i[1]:
        print(f'\n########## DADOS DO CADASTRO ##########\nUsername: {self.username}\nPassword: {self.password}\n')
                
      else:
        print('Erro! Dados informados não encontrados\n')
        
    else:
      print('Você não está logado.\n')
  
  def deslogar(self):
    self.login = 0 
    print('Você saiu da sua conta.\n')
    return
