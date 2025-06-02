#5 to 1 number print using recursive function:
def recursive(n):
  if n==0:
    return
  print(n)
  recursive(n-1)
   
print(recursive(5))

#sum of the first n natural numbers:
def sum_recursive(n):
  if n==0:
    return 0
  return sum_recursive(n-1) + n
  

print(sum_recursive(5))    