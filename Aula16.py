lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'
print(lanche[2])
print(lanche[:2])
print(lanche[-2])
print(lanche[-2:])

#Tuplas são imutaveis

for comida in lanche:
    print(f'Eu vou comer {comida}')

# for cont in range(0, len(lanche)):
#     print(lanche[cont])

# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.count(5))
print(c.index(2))
del(c)
