import math as math

def bray_curtis_distance(sample1, sample2):
    numerator = sum(abs(a - b) for a, b in zip(sample1, sample2))
    denominator = sum(sample1 + sample2)
    return numerator / denominator
amostra_a = {
    'Bolao_cinza': [0, 0, 0, 0, 0, 0, 0, 0, 1],
    'Bola_branca': [1, 3, 1, 0, 2, 0, 4, 8, 0, 1],
    'Bola_laranja': [2, 3, 2, 3, 3, 4, 3, 1, 1, 4],
    'Bola_vermelha': [4, 2, 0, 3, 2, 2, 0, 3, 0, 0],
    'Bola_azul': [2, 1, 1, 3, 1, 1, 3, 1, 1, 4],
    'Bola_marrom': [1, 0, 4, 0, 8, 4, 7, 1, 1, 7],
    'Meia_bola_verde': [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    'Meia_bola_azul': [0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
    'Disco_branco': [3, 5, 0, 0, 1, 4, 0, 0, 4, 4],
    'Disco_verde': [1, 1, 0, 3, 0, 1, 2, 0, 1, 0],
    'Disco_rosa': [0, 0, 0, 4, 7, 0, 6, 0, 9, 2],
    'Disco_cinza': [0, 1, 1, 0, 2, 2, 2, 3, 3, 2],
    'Botao_transparente': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Botao_preto': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Botao_amarelo': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Botao_rosa': [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    'Botao_branco': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Botao_verde': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}
amostra_b = {
    'B1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'B2': [4, 2, 4, 0, 0, 2, 1, 1, 2, 7],
    'B3': [5, 2, 4, 3, 3, 1, 0, 1, 3, 1],
    'B4': [2, 2, 4, 2, 2, 1, 2, 0, 0, 3],
    'B5': [1, 3, 4, 1, 3, 1, 2, 0, 2, 3],
    'B6': [3, 1, 5, 1, 3, 0, 2, 0, 1, 3],
    'B7': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'B8': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'B9': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'B10': [0, 6, 4, 0, 4, 1, 0, 1, 1, 1]
}
media_a = {key: sum(values) / len(values) for key, values in amostra_a.items()}
media_b = {key: sum(values) / len(values) for key, values in amostra_b.items()}
riqueza_a = sum(1 for values in amostra_a.values() if any(value > 0 for value in values))
riqueza_b = sum(1 for values in amostra_b.values() if any(value > 0 for value in values))
diversidade_a = sum(-p * math.log2(p) if p > 0 else 0 for values in amostra_a.values() for p in values) / len(amostra_a)
diversidade_b = sum(-p * math.log2(p) if p > 0 else 0 for values in amostra_b.values() for p in values) / len(amostra_b)
media_total_a = sum(sum(values) for values in amostra_a.values()) / len(amostra_a.values())
media_total_b = sum(sum(values) for values in amostra_b.values()) / len(amostra_b.values())
distancia_beta = bray_curtis_distance(list(media_a.values()), list(media_b.values()))
print("Amostra A:")
print("Médias:")
print("Amostra A - Média total de indivíduos:", media_total_a)
print("Riqueza A:", riqueza_a)
print("Diversidade Alfa A:", diversidade_a)
print("\nAmostra B:")
print("Médias:")
print("Amostra B - Média total de indivíduos:", media_total_b)
print("Riqueza B:", riqueza_b)
print("Diversidade Alfa B:", diversidade_b)
print("Diversidade beta A e B:", distancia_beta)