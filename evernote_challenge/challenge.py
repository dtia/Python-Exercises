"""
Write a function that finds the highest 4 integers in an unordered list of numbers and describe its performance in O(n) time. Use any language you desire. Create a solution that is well written and with good performance.
"""

def main():
  unordered = [76, 87, -10, 65, 23, -29,  98, 54, 45, 12]

def find_max_4(list):
  unsorted4 = list[:4]
  max4 = [None, None, None, None]
  global_min = max4[0]
  global_max = max4[3]
  

  for i in list[4:]:
    if i > global_max:
      global_max = i

def sort_sublist(list):
  sorted = []

  for i in range(3):
    curr = unsorted[i]
    next = unsorted[i+1]
    
    if curr > next:
      sorted.append(next).append(curr)
    elif i < global_min:
      global_min = i

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
