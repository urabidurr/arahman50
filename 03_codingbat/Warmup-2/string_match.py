def string_match(a, b):
  mins = min(len(a), len(b))
  counter = 0
  
  for i in range(mins-1):
    nA = a[i:i+2]
    nB = b[i:i+2]
    if nA == nB:
      counter += 1
  return counter
