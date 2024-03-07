"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
  
  result = []
  numero = 5

  while numero >= 0:

    result.append(numero)
    numero -= 1

  return result

