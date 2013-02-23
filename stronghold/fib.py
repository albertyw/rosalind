# months
n = 34

# pairs
k = 4


population = [1, 1]
i = 2
while i < n:
    new_population = population[i-2]*k + population[-1]
    population.append(new_population)
    i += 1
    
print population
print len(population)
print population[-1]
