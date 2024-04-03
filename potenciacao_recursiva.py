def potenciacao_recursiva(base, exp):
  if(exp > 1):
    return base * potenciacao_recursiva(base, exp - 1) 
  else:
    return base

print(potenciacao_recursiva(4, 2))