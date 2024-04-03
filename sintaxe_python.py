#importa apenas sqrt
#from math import sqrt

#importa toda a classe math
import math

# Variáveis
# as variáveis precisam ser inicializadas
a, b = 1, 2;
print(a);
print(b);

# Valor nulo (null)
c = None;
print(c);

# Saídas
h = "Hello";
w = "World";
print("%s, %s" % (h, w))
print("VAL A = ", a, " VAL B = ", b)

# Concatenação
# converter valores numericos antes de imprimir
v = "Olá";
v1 = 10;
v2 = "Hello";
print(v + ", " + v2 + "" + str(10));

# Entrada (leitura de valores);
teclado = input("Digite alguma coisa: ");
print("o texto digitado foi: " + teclado);

# identificar tipo de dado
print(type(teclado))
verifica = type(teclado) == int;

# Numeros
# +, -, *, /, %
#potencia  == 10 ** 2;

print(max(1,2,3))
print(min(5, 4, 10))
print(abs(-1))

# String
#funções básicas
"""
len()	mostra o tamanho da string
lower()	caixa baixa
upper()	caixa alta
str()	converte em string
isalpha()	retorna False se a string contiver algum caracter que não seja letras
"""
#condicionais
expressao = True;
if expressao == True:
  print("Expressao é verdadeira")
else:
  print("Expressao é falsa")

variavelTeste = 1;

if variavelTeste == 2:
  print("O número é 2")
elif variavelTeste == 3:
  print("O número é 3")
else:
  print("O número é 1")

#Laço de Repetição
lista = ["P", "y", "t", "h", "o", "n"]

for item in lista:
  print(item)

count = 0;
while count <= 5:
  print(count)
  count+=1

#Funções
def funcao():
  return "True";

print(funcao())

valor1 = 10
valor2 = 20

def funcao2(a, b):
  return a + b

res = funcao2(valor1, valor2)
print(res)
print(math.sqrt(res))

#datas em python
from datetime import datetime
now = datetime.now();
print(now)
print(now.year)
print(now.month)
print(now.day)

#formato brasileiro
print("%s/%s/%s - %s:%s:%s" % (now.day, now.month, now.year, now.hour, now.minute, now.second))

#listas
Animais = ["Pagolin", "Elefante", "Macaco", "Gato"]
print(Animais[0])
print(Animais[1])
print(Animais[2])
print(Animais[3])
print(len(Animais))

#dicionarios
people = {
  "name" : "João",
  "age"  : "22",
  "skills"  : ["Python", "Ruby", "PHP"]
  
}

print(people["name"])
print(people["age"])
print(people["skills"])

#lambdas
def f(x):
  return x * 2

print(f(5))

g = lambda x: x * 3
print(g(5))