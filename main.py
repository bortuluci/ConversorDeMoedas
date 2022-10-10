from UserClass import User

usuarioApp=User()
  
logado=0 #0= deslogado // 1= logado

while logado == 0:
  cadastradoOuNao=int(input('\nVocê já é cadastrado? [1]NÃO / [2]SIM / [0]FECHAR\n'))
  if cadastradoOuNao == 1:
    usuarioApp.novoCadastro()
    
  elif cadastradoOuNao == 2:
    usuarioApp.logando()
    
    while usuarioApp.login == 1:
      menu = int(input('\n########## MENU ########## \n [1] Alterar senha. \n [2] Excluir cadastro. \n [3] Principais moedas. \n [4] Converter moedas \n [5] Visualizar dados cadastrados \n [0] Sair\n')) 
      
      if menu == 1:
        usuarioApp.alterarSenha()

      if menu == 2:
        usuarioApp.excluirCadastro()

      if menu == 3:
        usuarioApp.principaisMoedas()

      if menu == 4:
        usuarioApp.converterMoedas()

      if menu == 5:
        usuarioApp.visualizarDados()

      if menu == 0:
        usuarioApp.deslogar()
            
    else:
      break
  elif cadastradoOuNao == 0:
    break  
  
  else:
    print('Erro! Número não reconhecido.\n')
else:
  print('\n########## FIM ##########')

#Made by Khauan Bortuluci
#github.com/bortuluci
#E-mail: khauanbs@gmail.com
#SC, Brazil