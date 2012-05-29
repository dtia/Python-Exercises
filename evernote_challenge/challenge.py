"""
Write a function that finds the highest 4 integers in an unordered list of numbers and describe its performance in O(n) time. Use any language you desire. Create a solution that is well written and with good performance.
"""

import random

def main():
  unordered = [76, 87, 5, -10, 65, 70, 0, 55, 23, -29,  98, 54, 45, 12]
  print find_max_4(unordered)

def find_max_4(list):
  unsorted4 = list[:4]
  max4 = quicksort(unsorted4) 

  for i in list[4:]:
    if i > max4[0]:
      max4 = insert_int(i, max4)
  return max4

def insert_int(int, max4): 
  i = 0
  while i < 4 and int > max4[i]:
    i += 1

  max4.insert(i, int)
  max4 = max4[-4:]
  return max4

def quicksort(arr):
  if len(arr) <= 1:
    return arr

  less = []
  greater = []
  
  pivot = select_pivot(arr)
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
  r = random.Random()
  rand = r.randint(0, len(arr)-1)
  return arr[rand]

if __name__ == '__main__':
  main()
