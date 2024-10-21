import random

def genetic_algorithm(population, fitness_fn, mutate_fn, crossover_fn, generations=100):
    for generation in range(generations):
        population = sorted(population, key=fitness_fn, reverse=True)
        next_generation = population[:2]  # Elitism

        for _ in range(len(population) // 2 - 1):
            parents = random.sample(population[:10], 2)
            child1, child2 = crossover_fn(parents[0], parents[1])
            next_generation += [mutate_fn(child1), mutate_fn(child2)]

        population = next_generation

    return max(population, key=fitness_fn)

# Fitness function example (different problem)
def fitness_fn(individual):
    return sum(individual) + (individual.count(1) * 2)  # Favor more 1s

# Mutation function
def mutate_fn(individual):
    index = random.randint(0, len(individual) - 1)
    individual[index] = 1 - individual[index]  # Flip the bit
    return individual

# Crossover function
def crossover_fn(parent1, parent2):
    index = random.randint(1, len(parent1) - 1)
    return parent1[:index] + parent2[index:], parent2[:index] + parent1[index:]

# Different example population
population = [[random.randint(0, 1) for _ in range(10)] for _ in range(20)]
print("Optimal solution:", genetic_algorithm(population, fitness_fn, mutate_fn, crossover_fn))
