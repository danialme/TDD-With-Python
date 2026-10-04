# exercicio_02/notas.py
def classificar_nota(nota: float) -> str: 
	if nota < 0 or nota > 10: 
		raise ValueError("Nota inválida.") 
	if nota <= 4.9: return "Reprovado" elif nota <= 6.9: 
		return "Recuperação" 
	else: 
		return "Aprovado"
