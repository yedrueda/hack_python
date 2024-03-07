"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
  
  text = "fooziman"
  result = []

  for char in text:
    if char.isdigit():
      result.append(char)
    elif char == "a":
      result.append("@")
    elif char == "o":
      result.append("0")
    elif char == "i":
      result.append("1")    
    else:
      result.append(char.upper())

  return result

print(fn_hack_10())
