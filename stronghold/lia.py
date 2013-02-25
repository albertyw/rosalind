from math import factorial

# generation
k = 5
# number of AaBb organisms
N = 8


homozygous_dominant = 0.0
heterozygous = 1.0
homozygous_recessive = 0.0
for i in range(1,k+1):
    # AA
    homozygous_dominant_new = homozygous_dominant*0.5 + heterozygous*0.25
    # Aa
    heterozygous_new = homozygous_dominant*0.5 + heterozygous*0.5 + homozygous_recessive*0.5
    # aa
    homozygous_recessive_new = homozygous_recessive*0.5 + heterozygous*0.25
    
    homozygous_dominant = homozygous_dominant_new
    heterozygous = heterozygous_new
    homozygous_recessive = homozygous_recessive_new
    
print homozygous_dominant
print heterozygous
print homozygous_recessive
print

probability_heterozygous = heterozygous**2
print probability_heterozygous

# Take the Cumulative Binomial Distribution
def choose(a,b):
    return factorial(a) / factorial(b) / factorial(a-b)
    
probability = 0.0
for i in range(N, 2**k+1):
    probability += choose(2**k, i) * probability_heterozygous**i * (1 - probability_heterozygous)**(2**k-i)
print probability


