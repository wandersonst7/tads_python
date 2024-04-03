class No:
  def __init__(self, valor, ante, prox):
    self.ante = ante
    self.prox = prox
    self.valor = valor

def imprimeLista(no):
  while no:
    print(no.valor)
    no = no.prox
    
def TamList(no):
  i = 0
  while no:
    i+=1
    no = no.prox
  return i;

def pesquisa(no, valor):
  res = 0
  while no:
    if(valor == no.valor):
      res = True
      break
    else:
      res = False
    no = no.prox
  return res

def sobrescrever(no, valor, indice):
  cont = 0
  while no:
    if(cont == indice):
      no.valor = valor
      break
    no = no.prox
    cont+=1
    
def ordemReversa(no):
  while no:
    no = no.prox
    if(no.prox == None):
      while no:
        print(no.valor)
        no = no.ante
        if(no == None):
          break
      break
    
no1 = No(1, None, None)
no2 = No(35, no1, None)
no3 = No(88, no2, None)
no2 = No(35, no1, no3)
no1 = No(1, None, no2)

print("Valores iniciais:")
imprimeLista(no1)
print("-----------------\n")


print("Tamanho: ")
print(str(TamList(no1)))


print("\nPesquisa:")
if(pesquisa(no1,35)):
  print("Elemento encontrado!")
else:
  print("Elemento não encontrado!");
  
sobrescrever(no1, 10, 2)

print("\nValores depois de sobrescrever:")
imprimeLista(no1)
print("-----------------")

print("\nOrdem reversa: ")
ordemReversa(no1)
