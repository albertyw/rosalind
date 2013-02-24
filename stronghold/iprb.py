# homozygous dominant
k = 17 * 1.0
# heterozygous
m = 20 * 1.0
# homozygous recessive
n = 19 * 1.0

total = k + m + n
total_possibilities = total * 2 * (total - 1) * 2
dominant_k = k*2 * ((k-1)*2 + m*2 + n*2)
dominant_m = m * (k*2 + (m-1)*2 + n*2) + m * (k*2 + (m-1))
dominant_n = n*2 * (k*2 + m)

dominant = dominant_k + dominant_m + dominant_n

print dominant_k
print dominant_m
print dominant_n
print dominant
print total_possibilities

probability = dominant / total_possibilities

print probability
