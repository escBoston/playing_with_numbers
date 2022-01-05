import pytest
import random
import math
from importlib.machinery import SourceFileLoader

service = SourceFileLoader('service', '../service.py').load_module()

def generate_randarr():
    return [random.randint(0,50) for i in range(15)]

def avail_nums(a, b, c):
    allnum = [i for i in range(0,51)]
    return [n for n in allnum if n not in set(a+b+c)]

def largest_prime(a, b, c):
    primes = [2]
    for num in range(3,50,2):
        if all(num%i!=0 for i in range(3,int(math.sqrt(num))+1, 2)):
            primes.append(num)
    available_numbers = avail_nums(a, b, c)
    available_primes = set(available_numbers).intersection(set(primes))
    return max(list(available_primes)) if bool(available_primes) else 0

def test_extract(a, b, c, s):
    assert s.available_numbers == avail_nums(a, b, c)

def test_largest_prime(a, b, c, s):
    assert s.largest_prime() == largest_prime(a, b, c)

def display_arrs(a, b, c):
    idx = 1
    for lst in [a, b, c]:
        print(f'Array {idx}: ')
        lst.sort()
        print(lst)
        idx += 1

def main():
    random.seed(1)
    a = generate_randarr()
    b = generate_randarr()
    c = generate_randarr()
    s = service.Service()
    s.extract(a, b, c)

    test_extract(a, b, c, s)
    test_largest_prime(a, b, c, s)
    print('All tests passed')

    display_arrs(a,b,c)
    print('Available numbers: ')
    print(s.available_numbers)
    lgst_prime = s.largest_prime()
    prime_msg = lgst_prime if lgst_prime != 0 else 'No primes found'
    print('Largest prime: ' + str(prime_msg))

if __name__ == '__main__':
    main()
