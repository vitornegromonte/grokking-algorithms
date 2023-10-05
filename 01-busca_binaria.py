def buscaBinaria(lista: list, item: int):
    min = 0
    max = len(lista) - 1
  
    while min <= max:
      meio = int((min + max)/ 2)
      chute = lista[meio]
      
      if chute == item:
        return meio
      elif chute > item:
        max = meio - 1
      else:
        min = meio + 1
    return None
  
lista_teste = [1,3,5,7,9]
# Case test 1
print(buscaBinaria(lista_teste, 3)) # => 1
# Case test 2
print(buscaBinaria(lista_teste, -1))

teste_cria = []
i = 1
while i <= 129:
  teste_cria.append(i)
  i += 1
  
