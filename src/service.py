import math

class Service:
    def __init__(self):
        self.available_numbers = []
        self.all_primes = self.all_primes()

    def extract(self, a, b, c):
        allnums = [i for i in range(0,51)]
        self.available_numbers = list(set(allnums) - set(a + b + c))

    def all_primes(self):
        primes = [2]
        for num in range(3,50,2):
            if all(num%i!=0 for i in range(3,int(math.sqrt(num))+1, 2)):
                primes.append(num)
        return primes

    def largest_prime(self):
        available_primes = set(self.available_numbers).intersection(set(self.all_primes))
        return max(list(available_primes)) if bool(available_primes) else 0
