def Fibonacci(n):
  """
  Returns the nth term of the Fibonacci Sequence
  n is zero based indexed
  """
  if n < 0:
    raise Exception("Invalid Argument")
  elif n < 2:
    return n
  else:
    return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(0))
print(Fibonacci(3))