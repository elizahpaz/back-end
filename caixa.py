totC = 0
print("CÓDIGOS: 1; 2; 4; 5; 9")

while True:
    cod = int(input("\nCódigo do produto (0 para finalizar): "))
    if cod == 0:
        break
    qnt = int(input("Quantidade: "))
    if cod == 1:
        preço = 0.50
        totI = preço * qnt
        totC += totI 
    elif cod == 2:
        preço = 1
        totI = preço * qnt
        totC += totI 
    elif cod == 4:
        preço = 4
        totI = preço * qnt
        totC += totI 
    elif cod == 5:
        preço = 7
        totI = preço * qnt
        totC += totI 
    elif cod == 9:
        preço = 8
        totI = preço * qnt
        totC += totI 
    else:
        print ("\nCodigo inválido!")
    
print (f"\n\tTOTAL: R${totC}")
