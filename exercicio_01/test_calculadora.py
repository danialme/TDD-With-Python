# exercicio_01/test_calculadora.py 
import pytest 
from calculadora import calcular\_desconto 

# Testes Obrigatórios 
def test_desconto_10_porcento(): 
	assert calcular_desconto(100, 10) == 90 

def test_desconto_20_porcento(): 
assert calcular_desconto(250, 20) == 200 

def test_sem_desconto(): 
	assert calcular_desconto(150, 0) == 150 

def test_desconto_100_porcento(): 
	assert calcular_desconto(80, 100) == 0 

# Desafio Adicional: Casos de Borda / Exceções 

def test_valor_negativo_lanca_excecao(): 
	with pytest.raises(ValueError): 
		calcular_desconto(-100, 10) 

def test_desconto_superior_a_100_lanca_excecao(): 
	with pytest.raises(ValueError): 
		calcular_desconto(100, 110) 

def test_desconto_negativo_lanca_excecao(): 
	with pytest.raises(ValueError): 
		calcular_desconto(100, -10)
