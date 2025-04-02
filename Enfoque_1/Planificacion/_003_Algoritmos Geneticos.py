import random

def genetic_algorithm(target, population_size=100, mutation_rate=0.01, generations=1000):
    def fitness(individual):
        return sum(1 for i, j in zip(individual, target) if i == j)
    
    def mutate(individual):
        return ''.join(c if random.random() > mutation_rate else random.choice('01') for c in individual)
    
    def crossover(parent1, parent2):
        point = random.randint(1, len(target) - 1)
        return parent1[:point] + parent2[point:]
    
    population = [''.join(random.choice('01') for _ in target) for _ in range(population_size)]
    
    for _ in range(generations):
        population = sorted(population, key=fitness, reverse=True)
        if fitness(population[0]) == len(target):
            return population[0]
        next_gen = [crossover(population[i], population[i+1]) for i in range(0, population_size-1, 2)]
        population = [mutate(ind) for ind in next_gen]
    
    return population[0]

# Ejemplo de uso
target = "1010101010"
print(genetic_algorithm(target))