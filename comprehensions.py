noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
noprimes2 = [j for i in range(4,8)]
print(noprimes)
print(noprimes2)
primes = [x for x in range(2, 50) if x not in noprimes]
print(primes)
