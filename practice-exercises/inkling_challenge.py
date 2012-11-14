import random
import math

class Randoms:
  def __init__(self, max_num):
    self.nums = range(max_num)
    random.shuffle(self.nums)
    self.iterator = iter(self.nums)

  def popNext(self):
    try:
      return self.iterator.next()
    except StopIteration:
      return None

class Primes:
  def __init__(self, max_num):
    self.nums = range(2, max_num)
    prime_nums = filter(self.checkPrime, self.nums)
    self.iterator = iter(prime_nums)

  # Determine primality by dividing numbers in the range [2,sqrt(num)]
  # If num divides evenly into any of these numbers, then it is not prime
  def checkPrime(self, num):
    sqrt = int(math.sqrt(num))+1
    num_range = range(2, sqrt)
    for i in num_range:
      if num % i == 0:        
        return False
    return True
    
  def popNext(self):
    try:
      return self.iterator.next()
    except StopIteration:
      return None

class PrimeFactors:
  def __init__(self, max_num):
    self.max_num = max_num
    self.nums = range(2, max_num+1)
    self.prime = Primes(max_num)
    self.prime_factors = filter(self.is_factor_and_prime, self.nums)
    self.iterator = iter(self.prime_factors)

  # Determines whether the number is a factor and whether it's prime
  def is_factor_and_prime(self, num):
    if self.max_num % num == 0 and self.prime.checkPrime(num):
      return True
    return False

  def popNext(self):
    try:
      return self.iterator.next()
    except StopIteration:
      return None

def map(fn, stream):
  outputStream = []
  for item in stream:
    outputStream.append(fn(item))
  return outputStream

def filter(fn, stream):
  outputStream = []
  for item in stream:
    if fn(item):
      outputStream.append(item)
  return outputStream

def zipWith(fn,streamA,streamB):
  #return map(lambda a, b: fn(a,b), streamA, streamB)
  return [fn(a,b) for (a,b) in zip(streamA,streamB)]

def prefixReduce(fn,stream,init):
    iterator = iter(stream)
    if init is None:
      try:
        init = next(iterator)
      except StopIteration:
        raise TypeError('empty list with no initial value')
    accum_value = init
    
    for i in iterator:
      accum_value = fn(accum_value, i)
    return accum_value

def main():
  """
  rand = Randoms(5)
  print rand.popNext()
  print rand.popNext()
  print rand.popNext()
  print rand.popNext()
  print rand.popNext()
  print rand.popNext() #should return None
  print rand.popNext() #should return None
  
  primes = Primes(10)
  print primes.popNext()
  print primes.popNext()
  print primes.popNext()

  primeFactors = PrimeFactors(30)
  print primeFactors.popNext()
  print primeFactors.popNext()
  print primeFactors.popNext()
  print primeFactors.popNext() #should return None
  """

  rand = range(10)
  print map(lambda x: x*3, rand)
  
  filt = range(100)
  print filter(lambda x: x%2 == 0, filt)

  zipwithA = range(50,100)
  zipWithB = range(100,150)
  print zipWith(lambda x,y: x*y, zipwithA, zipWithB)

  prefred = range(10)
  print prefixReduce(lambda x,y: x+y+2, prefred, 0)

if __name__ == '__main__':
  main()
