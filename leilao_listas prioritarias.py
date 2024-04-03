def leilao(vencedor):
  while True:
    print("====== Leilão =====")
    print("| [1] Fazer Lance |")
    print("| [0] Sair        |")
    print("===================")
    option = input("Escolha: ")
    option = int(option)

    if option == 1:
      name = str(input("Qual o seu nome? "))
      value = float(input("Digite o valor: "))
      vencedor.append((value, name))
      print("\n" + name + " fez uma oferta de " + str(value) + "!\n")
    elif option == 0:
      break
    else:
      print("Opção inválida!")
      
  ganhador = max(vencedor)
  print("O ganhador foi " + ganhador[1] + " com o valor de " + str(ganhador[0]) + " R$.")
    
vencedor = []

leilao(vencedor)