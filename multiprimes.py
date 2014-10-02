'''
multiprimes.py

By Sam Weiss

Computes a list of prime numbers using multiple threads and no memory sharing
between threads
'''
from __future__ import division
import multiprocessing
import sys
import math
import pdb

#dividing by primes will speed things up, but doing it asyncly is not easy
#see 9 and 25, divisible by other primes
#plus I wanna see an example of multiprocessing really speeding things up here

primes = []
workers = []
numbers = 100000 #any more gets slow...
tests = numbers * (numbers / 2)
threads=4

def testprime(num):
    workers.append(num)
    pdb.set_trace()
    for i in primes:
        if i != 0 and i != 1 and i != num and num % i == 0:
            workers.remove(workers.index(num))
            return
    for i in workers:
        if i != 0 and i != 1 and i != num and num % i == 0:
            workers.remove(workers.index(num))
            return
    workers.remove(workers.index(num))
    primes.append(num)

def main():
    pool = multiprocessing.Pool(processes=threads)
    for i, _ in enumerate(pool.imap_unordered(testprime, xrange(numbers)), 1):
        sys.stdout.write('\rdone ' + str((int((100*i*(i/2))/tests))) + "%")

if __name__ == '__main__':
    main()
