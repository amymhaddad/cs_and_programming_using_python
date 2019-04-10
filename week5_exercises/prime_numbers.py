
def genPrimes():
      x = 1
      total_factors = []
      prime_numbers = []

      while True :
            for number in range(1, x + 1):
                  if x % number == 0:
                        total_factors.append(number) 

            if len(total_factors) == 2:
                  prime_numbers.append(x)
            
            yield prime_numbers 
            total_factors = []
            x += 1

primes = genPrimes()

print(next(primes))
print(next(primes))
print(next(primes))
print(next(primes))
print(next(primes))
print(next(primes))