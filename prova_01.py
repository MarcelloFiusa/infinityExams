while True:
    try:
        base = float(input("Digite a base do retângulo: "))
        height = float(input("Digite a altura do retângulo: "))
        break
    except ValueError:
        print("Digite um valor numérico válido!")

area = base*height
print(f"Um retângulo de Base: {base}m e Altura: {height}m tem uma área de {area}m²")