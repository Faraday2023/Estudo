lanche = ('Hambúrguer','Suco','Pizza','Pudim', 'Batata Frita')

for comida in lanche:
    print(f'Eu vou comer {comida}')

for count in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[count]}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

# lanche.index
# lanche.count
# sorted(lanche)
#lanche = ('A', 'B', 'C')
#print(lanche[0])