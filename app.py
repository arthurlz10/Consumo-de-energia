# Programa de cálculo de consumo de energia

print("Calculadora de Consumo de Energia")

# Entrada de dados
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho (em watts): "))
horas_dia = float(input("Digite o tempo médio de uso diário (em horas): "))

# Cálculo do consumo mensal (kWh)
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Cálculo de custo (opcional)
custo_kwh = 0.75
custo_estimado = consumo_mensal * custo_kwh

# Saída formatada
print("Resultado")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo_estimado:.2f}")