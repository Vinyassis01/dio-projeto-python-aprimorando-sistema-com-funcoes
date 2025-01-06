# sistema simples de um banco para o desafio de codigo do bootcamp python AI Backend VIVO
def banco():
# aprimorando o nosso sistema usando funcoes como solucao ao desafio de codigo
    print('''
    **************bem vindo a nossa startapp ****************    
    digite uma opcao para realizar :
      
      ( 1 ) extrato
      ( 2 ) depositar
      ( 3 ) sacar
      ( 4 ) sair
    ''')
    global saldo
    saldo =0.0
    LIMITE = 500
    N_operacoes = 1
    # aqui criei uma lista para armazenar as operacoes embora a formatacao nao seja a mais agradavel
    l = []
   # embora nao e recomendavel usar GLOBAL para definir funcoes globais 
   # foi a solucao q encontrei para usar valores da funcao depositar na funcao saque
   # era a unica necessidade explicita do meu codigo
   # as outras poderiam ser atraves de outars variaveis,mas optei por usar da mesma variavel
    def depositar (LIMITE):
      global sd_a
      deposito = float(input("digite a quantidade q deseja depositar  : "))
      sd_a = saldo + deposito
      if deposito < LIMITE:
        dp_r =f"deposito realizado com sucesso no valor de R$:{deposito}"
        l.append(dp_r)
        print(dp_r)  
      else:
         dp_n = f"deposito nao realizado pq o valor do {deposito}\n nao pode exceder R$ :{LIMITE} "
         l.append(dp_n)
         print(dp_n)   
    def saque (LIMITE):
      global sd_a
      sd_a = saldo
      saque = float(input("digite a quantia q deseja sacar   : "))
      if saque > saldo:
          sq_n =f"saque invalido pq vc nao tem saldo vc tem : R$:{saldo}\n ou tenha ecedido o limite de R$:{LIMITE}"
          print(sq_n)
          l.append(sq_n)
      else :
          sd_a -= saque
          sq_r = f"saque realizado com sucesso no valor de R$:{saque}"
          l.append(sq_r)
    def op_invalida ():
        if opcao != "1" or "2" or "3" or "4" or "" :
           print("operacao invalida")
        elif opcao == "":
           print("operacao invalida")
        else:
            pass
    def extrato ():
      saldo_atual =f"seu saldo atual e R$:{sd_a}"
      l.append("consulta de extrato")
      l.append(saldo_atual)
      print("""
      **************extrato****************
          operacoes realizadas :
      """)
      for lista in enumerate(l):
         print("_"*50)
         print(f"    {lista}\n ")     
    while N_operacoes <= 3:
# aqui criei o laco q chama cada funcao e intera sobre cada operacao em nosso sistema   
# optei em nao converter a variavel opcao para um inteiro para fazer o trtamento de erros
# em especial no caso de o usuario nao informar a operacao "deixar o branco"
        opcao = input("qual operacao vc deseja realizar ?  : ")
        if opcao == "1":
           extrato()
           N_operacoes+=1  
        elif opcao == "2" :
           depositar(LIMITE)
           N_operacoes+=1
        elif opcao == "3":
           saque(LIMITE)
           N_operacoes+=1
        elif opcao == "4":
           print("       obrigado por escolher o nosso banco\n"+"_"*50)
           break
        else :
           op_invalida()
           N_operacoes+=1
banco()