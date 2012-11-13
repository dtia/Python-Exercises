def main():
  sent = 'Reverse this sentence please.'
  print 'length of sent: ' + str(len(sent))
  revSent = revString(sent,0,len(sent))
  start = 0

  for i in range(len(revSent)):
    if revSent[i] == ' ':
      revString(revSent,start,i)
      start = i

  print revSent

def revString(word, start, end):
  length = (end - start) / 2
  for i in range(start, start+length):
    temp = word[i]
    rearIndex = end-i-1
    print temp
    word[i] = word[rearIndex]
    word[rearIndex] = temp

if __name__ == '__main__':
  main()
