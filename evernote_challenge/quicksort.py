import random

def main():
  unordered = [76, 87, 5, -10, 65, 70, 0, 55, 23, -29,  98, 54, 45, 12]
  print quicksort(unordered)

def quicksort(arr):
  if len(arr) <= 1:
    return arr

  pivot = select_pivot(arr)
  
  less = []
  greater = []
  
  arr.remove(pivot)

  for x in arr:
    if x < pivot:
      less.append(x)
    else:
      greater.append(x)
  
  temp = quicksort(less)
  temp.append(pivot)
  temp.extend(quicksort(greater))
  return temp

def select_pivot(arr):
  #pick random index and return its value
  r = random.Random()
  rand = r.randint(0, len(arr)-1)
  return arr[rand]

if __name__ == '__main__':
  main()
