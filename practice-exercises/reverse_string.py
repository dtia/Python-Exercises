def main():
  sent = ' Reverse this sentence please'
  revSent = revString(sent,0,len(sent))
  
  start = 0
  for i in range(len(revSent)):
    print revSent[i]
    if revSent[i] == ' ':
      print str(start) + ' ' + str(i)
      revSent = revString(revSent,start,i)
      start = i+1

  print revSent

def revString(word, start, end):
  print 'the word: ' + word + ' start: ' + str(start) + ' end: ' + str(end)
  wordlist = list(word)
  length = (end - start) / 2
  j = 0
  for i in range(start, start+length):
    temp = wordlist[i]
    rearIndex = end-j-1
    wordlist[i] = wordlist[rearIndex]
    wordlist[rearIndex] = temp
    j+=1

  return ''.join(wordlist)

if __name__ == '__main__':
  main()
