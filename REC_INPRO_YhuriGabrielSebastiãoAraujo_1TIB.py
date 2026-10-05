import random
def calcular_area_circulo(raio):
    return 3.14 * raio ** 2
def calcular_circunferencia(raio):
    return 2 * 3.14 * raio
while True:
    raio = float(input("Digite o raio da mesa ou 0 para encerrar: "))
    if raio == 0:
        break
    if raio > 0:
        area = calcular_area_circulo(raio)
        circunferencia = calcular_circunferencia(raio)
        if area > 3.5:
            classificacao = "Mesa grande"
            preco = 320.00
        else:
            classificacao = "Mesa pequena"
            preco = 195.00
        numero_sorteado = random.randint(1, 10)
        print(f"Raio: {raio:.2f} m")
        print(f"Área: {area:.2f} m²")
        print(f"Circunferência: {circunferencia:.2f} m")
        print(f"Classificação: {classificacao}")
        print(f"Preço: R$ {preco:.2f}")
        if numero_sorteado == 7:
            print("Acabamento de borda grátis!")
        print("-" * 30)
