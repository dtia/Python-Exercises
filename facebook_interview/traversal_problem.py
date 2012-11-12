#       A
#      / \
#     B   C
#    / \
#   D   E
#      / \
#     F   G
#
# preTrav(T) = T.root + preTrav(T.left) + preTrav(T.right)
# inTrav(T) = inTrav(T.left) + T.root + inTrav(T.right)
# post(T) = post(T.left) + post(T.right) + T.root
#
# preTrav: "ABDEFGC"
# inTrav: "DBFEGAC"
# ---------------
# post: "DFGEBCA"


def findPost(preTrav, inTrav):
  if len(preTrav) > 0:
    root = preTrav[0]
    length = findLeftSubTreeLength(inTrav, root)
    return findPost(getPreLeftSubTree(preTrav,length), getInLeftSubTree(inTrav,root)) + \
           findPost(getPreRightSubTree(preTrav,length), getInRightSubTree(inTrav,root)) + \
           root
  
  else:
     return ''

def findLeftSubTreeLength(inTrav, root):
  index = 0
  for i in range(len(inTrav)):
    if inTrav[i] == root:
      break
    index+=1
  
  return index

def getPreLeftSubTree(preTree, length):
  return preTree[1:length+1]

def getPreRightSubTree(preTree, length):
  return preTree[length+1:]

def getInLeftSubTree(inTree, root):
  return inTree.split(root)[0]

def getInRightSubTree(inTree, root):
  return inTree.split(root)[1]

def main():
  preTrav = "ABDEFGC"
  inTrav = "DBFEGAC"
 
  post = findPost(preTrav, inTrav)
  
  print 'Pre:\t' + preTrav
  print 'In:\t' + inTrav
  print 'Post:\t' + post

if __name__ == '__main__':
  main()
