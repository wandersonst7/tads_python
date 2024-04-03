CodeMorse = {
"A": 21,
"B": 1222,
"C": 1212,
"D": 122,
"E": 2,
"F": 2212,
"G": 112,
"H": 2222,
"I": 22,
"J": 2111,
"K": 121,
"L": 2122,
"M": 11,
"N": 12,
"O": 111,
"P": 2112,
"Q": 1121,
"R": 212,
"S": 222,
"T": 1,
"U": 221,
"V": 2221,
"W": 211,
"X": 1221,
"Y": 1211,
"Z": 1122,
}

# Definindo hashtable
HashTable = [[] for _ in range(11)] 

# Função Hash
def hashing(keyvalue):
  return keyvalue % len(HashTable)

# Insert ---> Encadeamento
def insert(HashTable, keyvalue, value):
  hash_key = hashing(keyvalue)
  HashTable[hash_key].append(value)

# Menu de Busca
def searchMenu():
  while True:
    print("\n====== BUSCA ======")
    print("[1] PALAVRA")
    print("[2] CÓDIGO MORSE")
    print("[3] CANCELAR BUSCA")
    optionSearch = int(input("SELECIONE: "))
    if(optionSearch == 1 or optionSearch == 2 or optionSearch == 3):
      break
    else:
      print("Opção inválida! \n")
  return optionSearch

# Busca por palavra
def searchWord():
  word = str(input("Digite a palavra: "))
  word = encrypt(word)
  answer = "A palavra não foi encontrada"
  stopSearch = 0

  for list in HashTable:
    for value in list:
      if(value == word):
        answer = "A palavra foi encontrada na posição: " + str(HashTable.index(list))
        stopSearch = 1
        break
    if(stopSearch == 1):
      break

  return answer

# Busca por Codigo Morse
def searchMorse():
  codeMorse = str(input("Digite o código (separado por espaços): "))
  answer = "O código não foi encontrado *OBS: Talvez você tenha esquecido de usar espaços"
  stopSearch = 0

  for list in HashTable:
    for code in list:
      if(code == codeMorse):
        answer = "Código encontrado na posição na posição: " + str(HashTable.index(list))
        stopSearch = 1
        break
    if(stopSearch == 1):
      break

  return answer

# Remove por palavra
def remove():
  word = str(input("Digite a palavra que deseja remover: "))
  showWord = word;
  word = encrypt(word)
  answer = "A palavra não foi encontrada"
  stopSearch = 0

  for list in HashTable:
    for value in list:
      if(value == word):
        list.pop(list.index(value))
        answer = "Palavra " + showWord + " removida com sucesso"
        stopSearch = 1
        break
    if(stopSearch == 1):
      break
      
  return answer

# Imprime HashTable
def display_hash(HashTable):
  for i in range(len(HashTable)):
    print(i, "-->", end = " ")
    for j in HashTable[i]:
      print(j, end = " --> ")
    print()

    
# Soma valores dos caracteres
def sum_value(word):
  ListLetter = list(word);
  sum = 0;

  for letter in ListLetter:
    for key, value in CodeMorse.items():
      if(letter == key):
        sum = sum + value
        break
        
  return sum

# Cripotografa uma palavra
def encrypt(word):
  ListLetter = list(word);
  varEncrypted = "";
  
  for letter in ListLetter:
    for key, value in CodeMorse.items():
      if(letter == key):
        varEncrypted = varEncrypted + str(value) + " "
        break
  
  return varEncrypted.rstrip()

# Descriptografa uma palavra através do código
def decrypt(morse):
  morse = morse.split(" ")
  ListCodes = list(morse)
  varDecrypted = ""

  for code in ListCodes:
    for key, value in CodeMorse.items():
      if(code == str(value)):
        varDecrypted = varDecrypted + key
        break
        
  return varDecrypted

# Menu Inicial
def menu():
  print("\n===== MENU =====")
  print("[1] INSERIR")
  print("[2] BUSCAR") 
  print("[3] REMOVER")
  print("[4] IMPRIMIR")
  print("[5] SAIR")
  optionMenu = int(input("ESCOLHA: "))
  return optionMenu

# Main

while True:
  OptionSelected = menu()
  # INSERIR
  if(OptionSelected == 1):
    word = str(input("Informe uma palavra: "))
    word = word.upper()
    insert(HashTable, sum_value(word), encrypt(word))
    print("Palavra inserida!")
  # BUSCAR
  elif(OptionSelected == 2):
    OptionSearch = searchMenu()
    if(OptionSearch == 1):
      result = searchWord()
      print(result)
    elif(OptionSearch == 2):
      result = searchMorse()
      print(result)
  # REMOVER
  elif(OptionSelected == 3):
    result = remove();
    print(result)
  # IMPRIMIR
  elif(OptionSelected == 4):
    display_hash(HashTable)
   # SAIR
  elif(OptionSelected == 5):
    print("Saindo ..")
    break;
  else:
    print("Opção inválida!")