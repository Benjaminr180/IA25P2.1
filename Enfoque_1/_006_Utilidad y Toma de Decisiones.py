def expected_utility(outcomes, probabilities):
    return sum(o * p for o, p in zip(outcomes, probabilities))
# Ejemplo de uso
outcomes = [100, 200, 300]
probabilities = [0.2, 0.5, 0.3]
print(expected_utility(outcomes, probabilities))  # Salida esperada: 220.0