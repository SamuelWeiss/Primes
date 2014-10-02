from __future__ import division
import multiprocessing
import sys
import math

#dividing by primes will speed things up, but doing it asyncly is not easy
#see 9 and 25, divisible by other primes
#plus I wanna see an example of multiprocessing really speeding things up here

#ffs, this is way faster than my multithreaded solution...

primes = []
numbers = 1000000 #any more gets slow...
def testprime(num):
    for i in primes:
        if i != 0 and i != 1 and i != num and num % i == 0:
            return
    primes.append(num)

def main():
    for i in xrange(numbers):
        testprime(i)
    print primes.__len__()

if __name__ == '__main__':
    main()
