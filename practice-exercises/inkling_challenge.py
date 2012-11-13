import random

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
   self.nums = range(max_nums)


def main():
  rand = Randoms(5)
  print rand.popNext()
  print rand.popNext()
  print rand.popNext()
  print rand.popNext()
  print rand.popNext()
  print rand.popNext() #should return None
  print rand.popNext() #should return None

if __name__ == '__main__':
  main()
