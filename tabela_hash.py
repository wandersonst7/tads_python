letras = {
  10: "A",
  11: "B",
  12: "C",
  13: "D",
  14: "E",
  15: "F",
  16: "G",
  17: "H",
  18: "I",
  19: "J",
  20: "K",
  21: "L",
  22: "M",
  23: "N",
  24: "O",
  25: "P",
  26: "Q",
  27: "R",
  28: "S",
  29: "T",
  30: "U",
  31: "V",
  32: "W",
  33: "X",
  34: "Y",
  35: "Z",
  36: "SPACE"
}

#Definindo hashtable
HashTable = [""] * 11


#Funções
def hashing(keyvalue):
  return keyvalue % len(HashTable)


#Função insert com sondagem linear
def insert(HashTable, keyvalue, value):
  hash_key = hashing(keyvalue)
  if (HashTable[hash_key] == ""):
    HashTable[hash_key] = value
  else:
    pos = hash_key
    while (pos < len(HashTable)):
      if (HashTable[pos] == ""):
        HashTable[pos] = value
        break
      pos = pos + 1


def display_hash(HashTable):
  for i in range(len(HashTable)):
    print(i, "-->", end=" ")
    for j in HashTable[i]:
      print(j, end=" ")
    print()


def calc_keyvalue(palavra):
  ListaLetras = list(palavra)
  keyvalue = 0
  for chave, value in letras.items():
    for i in range(len(ListaLetras)):
      if (value == ListaLetras[i]):
        keyvalue = keyvalue + chave
  return keyvalue


keyvalue = []
keyvalue.append(calc_keyvalue("ROMA"))
keyvalue.append(calc_keyvalue("TADS"))
keyvalue.append(calc_keyvalue("POO"))
keyvalue.append(calc_keyvalue("HASH"))

insert(HashTable, keyvalue[0], "ROMA")
insert(HashTable, keyvalue[1], "TADS")
insert(HashTable, keyvalue[2], "POO")
insert(HashTable, keyvalue[3], "HASH")

display_hash(HashTable)
