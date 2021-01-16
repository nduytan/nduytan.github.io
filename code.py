from browser import document
def calc(a, b, o):
  d = {'+': a + b,
       '-': a - b,
       '*': a * b,
       '/': a / b,
       '%': a % b
       }
  return f"({a}{o}{b})=({d[o]})"


a = float(input('Enter first number : '))
b = float(input('Enter second number : '))
o = input('Enter the Operator (+,-,*,/,%) : ')

document <= calc(a, b, o)
