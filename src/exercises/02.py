"""Script de exemplo 02 - Calculadora Simples."""

print("=" * 50)
print("EXERCÍCIO 02: Calculadora Simples")
print("=" * 50)
print()

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, /): ")

    print()

    if operacao == "+":
        resultado = num1 + num2
        print(f"Resultado: {num1} + {num2} = {resultado}")
    elif operacao == "-":
        resultado = num1 - num2
        print(f"Resultado: {num1} - {num2} = {resultado}")
    elif operacao == "*":
        resultado = num1 * num2
        print(f"Resultado: {num1} * {num2} = {resultado}")
    elif operacao == "/":
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado: {num1} / {num2} = {resultado}")
        else:
            print("Erro: Divisão por zero!")
    else:
        print("Operação inválida!")

    print()
    print("✓ Cálculo concluído!")

except ValueError:
    print("\n✗ Erro: Digite apenas números válidos!")
except Exception as e:
    print(f"\n✗ Erro inesperado: {e}")
