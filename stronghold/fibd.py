total_months = 90
life_span = 19

def get_born(born, i):
    if i < 0:
        return 0
    else:
        return born[i]

population = [1, 1]
born = [1, 0]
i = 2
while i < total_months:
    born.append(population[i-1] - born[i-1])
    population.append(population[i-1] + born[i] - get_born(born, i-life_span))
    i += 1

#print 'born'
#print born
#print 'population'
#print population
#print ''

print population[-1]

