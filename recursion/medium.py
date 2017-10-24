#Only works on sorted ascending arrays
def binary_search(l, target):
  def _binary_search(l, target, lo, hi):
    
    if (lo > hi):
      return -1
      
    current = int((hi + lo) // 2)
    if (l[current] == target):
      return current
    
    if (l[current] > target):
      return _binary_search(l, target, current + 1, hi)
    else:
      return _binary_search(l, target, lo, current - 1)
      
  
  return _binary_search(l, target, 0, len(l) - 1)
  
A = [1, 2, 3, 4, 5]

print(binary_search(A, 3))
