#!/usr/bin/python2.7

def revrev(to_rev):

  '''

  Reverse order of letters in word,

  but keep words in the same original order

  

  Example

  Input:  "The quick brown fox"

  Output: "ehT kciuq nworb xof"

  '''

  # Separate into words
  l = to_rev.split()
  #print(l) # Confirm it is propperly split

  # Reverse the words
  l2 = list()
  for s in l:
    l2.append(rev(s))
  #print(l2) # Confirm that they are reversed propperly
  
  # Comine words
  separator = " "

  return separator.join(l2)

def rev(to_rev):
  return to_rev[::-1]


print(revrev("The quick brown fox"))
