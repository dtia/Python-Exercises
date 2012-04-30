def main():
  num_lines = 0
  
  while num_lines < 1 or num_lines > 50:
    num_lines = int(raw_input('Enter number of items: '))
  
  pos_activities, neg_activities = get_activities(num_lines)
  
  pos_cals = [int(elem) for elem in pos_activities.keys()]
  neg_cals = [int(elem) for elem in neg_activities.keys()]

  find_match(-1, pos_cals, neg_cals)

  # get first pos, then match with first negative
  # if sum results in positive, look for that value in negative
    # else add next biggest negative
  # if sum results in negative, then look back at positive list
  
  output = []

  for pos_cal in pos_cals:
    if -pos_cal in neg_cals:
      return output.append([pos_cal, -pos_cal])
    else
      neg_cal = neg_cals.pop()
      diff = pos_cal + neg_cal
      if diff in pos_cals:
        output.append(diff)
      else:
        #insert this     

def find_match(sum, pos_cals, neg_cals):
  if len(pos_cals) == 0 or len(neg_cals) == 0:
    print 'no solution' 
  
  if sum == 0:
    print 'sum = 0'
    return []
  elif sum > 0:
    neg_cal = neg_cals.pop()
    sum + neg_cal 
    return find_match(sum + neg_cal, pos_cals, neg_cals).append([pos_cal, neg_cal])
  else:
    pos_cal = pos_cals.pop()
    return find_match(sum + pos_cal, pos_cals, neg_cals).append([pos_cal, neg_cal])


def find_neg_match(neg_cal, neg_cals, pos_cals):
  # given a negative number, find its 0
  if len(pos_cals) == 0 or len(neg_cals) == 0:
    print 'no solution' 
  
  pos_cal = pos_cals.pop()
  sum = neg_cal + pos_cal
  
  if sum == 0:
    return [neg_cal, pos_cal]
  elif sum > 0:
    return find_pos_match(sum, neg_cals, pos_cals).append([neg_cal, pos_cal])
  else:
    return find_neg_match(sum, neg_cals, pos_cals).append([neg_cal, pos_cal])

def get_activities(num_lines):
  pos_activities = {}
  neg_activities = {}

  for i in range(num_lines):
    activity, cal = raw_input('').split(' ')
    if int(cal) > 0:
      pos_activities[cal] = activity
    else:
      neg_activities[cal] = activity
  
  return pos_activities, neg_activities

def sort_pos_and_neg_activities(activities):
  pos = {}
  neg = {}

if __name__ == '__main__':
  main()
