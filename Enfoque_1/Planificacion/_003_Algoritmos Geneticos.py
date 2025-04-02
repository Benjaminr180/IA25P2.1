import random

def genetic_algorithm(target, population_size=100, mutation_rate=0.01, generations=1000):
    def fitness(individual):
        return sum(1 for i, j in zip(individual, target) if i == j)
    
    def mutate(individual):
        return ''.join(c if random.random() > mutation_rate else random.choice('01') for c in individual)
    
    def crossover(parent1, parent2):
        point = random.randint(1, len(target) - 1)
        return parent1[:point] + parent2[point:]
    
    # Inicializar población aleatoria
    population = [''.join(random.choice('01') for _ in target) for _ in range(population_size)]
    
    for _ in range(generations):
        # Ordenar por mejor aptitud
        population = sorted(population, key=fitness, reverse=True)
        
        # Si el mejor individuo ya es el objetivo, terminamos
        if fitness(population[0]) == len(target):
            return population[0]
        
        # Mantener una parte de la mejor población (elitismo)
        next_gen = population[:10]  # Conservamos los mejores 10 individuos
        
        # Generar nuevos individuos por cruza
        while len(next_gen) < population_size:
            parent1, parent2 = random.sample(population[:50], 2)  # Selección de padres más aptos
            offspring = mutate(crossover(parent1, parent2))
            next_gen.append(offspring)
        
        population = next_gen  # Reemplazar la población actual
    
    return population[0]

# Ejemplo de uso
target = "1010101010"
print(genetic_algorithm(target))
