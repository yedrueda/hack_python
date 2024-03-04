"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    result = result[:-1] + result[-1].upper()
    return result

resultado = fn_hack_4()
print(resultado)