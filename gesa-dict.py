print("\tCANTINA - GESA")
qntP = int(input("\nQnt. de produtos a venda: "))

cardapio = {}

print(f"\n\tRegistre os {qntP} produtos")
for i in range(1, qntP + 1):
    produto = input("PRODUTO: ")
    valor = float(input("PREÇO: R$"))
    cardapio[produto] = valor

print("\n---PRODUTO | PREÇO---")
for p, v in cardapio.items():
    print(f"{p.upper()}: R${v}")

subtotal = []
while True:
    preço = 0
    pedido = input("Produto: ")
    if pedido == "0":
        break
    qnt = int(input("Quantidade: "))
    for p, v in cardapio.items():
        if pedido == p:
            preço = v * qnt
            subtotal.append(preço)

total = sum(subtotal)
print(f"\n\tTOTAL: R${total}")