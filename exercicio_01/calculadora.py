# exercicio_01/calculadora.py 
def calcular_desconto(valor: float, percentual: float) -> float: 
	# Tratamento dos cenários de exceção (Desafio Adicional) 
	if valor < 0 or percentual < 0 or percentual > 100: 
		raise ValueError("O valor original e o percentual de desconto devem ser válidos.") # Cálculo do valor com desconto 
desconto = valor * (percentual / 100) 
return valor - desconto
