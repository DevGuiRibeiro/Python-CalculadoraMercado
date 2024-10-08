precos = {
    'maçã': 3.00,
    'banana': 5.00,
    'uva': 10.00,
    'limão': 15.00,
    'laranja': 20.00
}


qtde = int(input('Digite a quantidade de produtos: '))

def calcular_total(compra):
    total = 0
    for produto, quantidade in compra.items():
        total += precos[produto] * quantidade
    return total

compra = {}
for i in range(qtde):
    produto = input(f"Digite o nome do produto {i + 1}: ").lower()
    if produto in precos:
        quantidade = int(input(f"Digite a quantidade do produto {produto}: "))
        compra[produto] = quantidade
    else:
        print(f"Produto {produto} não encontrado. Tente novamente.")


total = calcular_total(compra)
print(f"Total da compra: R$ {total:.2f}")