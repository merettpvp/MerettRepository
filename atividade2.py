def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))
imc = calcular_imc(peso, altura)
print("Seu Índice de Massa Corpórea (IMC) é:", imc)