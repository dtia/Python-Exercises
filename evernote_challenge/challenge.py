"""
Write a function that finds the highest 4 integers in an unordered list of numbers and describe its performance in O(n) time. Use any language you desire. Create a solution that is well written and with good performance.
"""

def main():
  unordered = [76, 87, -10, 65, 23, -29,  98, 54, 45, 12]
  unsorted4 = unordered[:4]
  print sort_sublist(unsorted4)

"""
def find_max_4(list):
  unsorted4 = list[:4]
  max4 = [None, None, None, None]
  global_min = max4[0]
  global_max = max4[3]

  for i in list[4:]:
    if i > global_max:
      global_max = i
"""

def sort_sublist(unsorted):
  sorted = []

  for i in range(3):
    curr = unsorted[i]

    if i is 1:
      if curr > unsorted[i+1]:
        sorted.append(next)
        sorted.append(curr)
      else:
        sorted.append(curr)
        sorted.append(next)

    if i is 2:
      if curr > sorted[1]:
        sorted.append(curr)
      elif curr < sorted[0]:
        sorted.insert(0, curr)
      else:
        sorted.insert(1, curr)

    if i is 3:
      if curr > sorted[2]:
        sorted.append(curr)
      elif curr < sorted[0]:
        sorted.insert(0, curr)
      elif curr < sorted[1]:
        sorted.insert(1, curr)
      else:
        sorted.insert(2, curr)
  
    print sorted

  return sorted 

def merge_sort(list):
  if len(list) is 1:
    return list
  elif len(list) is 2:
    if list[0] > list[1]:
      return [list[1], list[0]]
    else:
      return list
  else:
    first_half = len(list)/2
    second_half = len(list)
    print 'first half: %s second half: %s' % (first_half, second_half)
    merge_sort(list[:first_half]).append(merge_sort(list[:second_half]))
    
if __name__ == '__main__':
  main()
