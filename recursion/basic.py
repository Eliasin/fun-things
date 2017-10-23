def fibonacci_it(n):
  a = 0
  b = 1
  while n > 0:
    a, b = b, a + b
    n -= 1
  return a

def fibonacci_naive(n):
  return 1 if n == 1 or n == 2 else fibonacci_naive(n - 1) + fibonacci_naive(n - 2)
  
def fibonacci_tail(n):
  def _fibonacci_tail(a, b, n):
    if (n <= 0):
      return a
    return _fibonacci_tail(b, a + b, n - 1)
  return _fibonacci_tail(0, 1, n)

def is_palindrome(s):
  def _is_palindrome(s, l, h):
    if (l == h or l > h):
      return True
    if (s[l] != s[h]):
      return False
    return _is_palindrome(s, l + 1, h - 1)
    
  return _is_palindrome(s, 0, len(s) - 1)
