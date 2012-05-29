"""
Write a function that finds the highest 4 integers in an unordered list of numbers and describe its performance in O(n) time. Use any language you desire. Create a solution that is well written and with good performance.
"""

def main():
  unordered = [76, 87, 5, -10, 65, 70, 0, 55, 23, -29,  98, 54, 45, 12]
  print find_max_4(unordered)

def find_max_4(list):
  unsorted4 = list[:4]
  max4 = sort_sublist(unsorted4) 

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

def sort_sublist(unsorted):
  sorted = []

  for i in range(4):
    curr = unsorted[i]

    if i is 0:
      next = unsorted[i+1]
      if curr > next:
        sorted.append(next)
        sorted.append(curr)
      else:
        sorted.append(curr)
        sorted.append(next)

    elif i is 2:
      if curr > sorted[1]:
        sorted.append(curr)
      elif curr < sorted[0]:
        sorted.insert(0, curr)
      else:
        sorted.insert(1, curr)
    
    elif i is 3:
      if curr > sorted[2]:
        sorted.append(curr)
      elif curr < sorted[0]:
        sorted.insert(0, curr)
      elif curr < sorted[1]:
        sorted.insert(1, curr)
      else:
        sorted.insert(2, curr)

  return sorted

if __name__ == '__main__':
  main()
