# exercicio_02/test_notas.py 
import pytest 
from notas import classificar_nota 

# Testes Obrigatórios 
def test_nota_4_reprovado(): 
	assert classificar_nota(4) == "Reprovado" 

def test_nota_5_recuperacao(): 
	assert classificar_nota(5) == "Recuperação" 

def test_nota_6_9_recuperacao(): 
	assert classificar_nota(6.9) == "Recuperação" 

def test_nota_7_aprovado(): 
	assert classificar_nota(7) == "Aprovado" 

def test_nota_10_aprovado(): 
	assert classificar_nota(10) == "Aprovado" 

# Requisito Adicional: Notas inválidas (< 0 ou > 10) 
def test_nota_menor_que_zero_lanca_excecao(): 
	with pytest.raises(ValueError): 
		classificar_nota(-1) 

def test_nota_maior_que_dez_lanca_excecao(): 
	with pytest.raises(ValueError): 
		classificar_nota(10.5)
