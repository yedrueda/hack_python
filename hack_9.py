"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
  
  result = [1, 2, 3]

  i = 0
  while i < len(result):
    result.insert(i + 1, "@")  # Insert "@" after the current element
    i += 2  # Increment by 2 to skip the newly inserted "@"

  return result

result = fn_hack_9()
print(result) 