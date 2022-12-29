def wrapBrackets( text ):
  return "(" + text + ")"

def squareBrackets( text, count ):

  return "[" * count + text + "]" * count

def quotesBrackets( text, count ):
  return "<" * count + text + ">" * count

print( wrapBrackets("12345") )
print( squareBrackets(wrapBrackets("12345"), 3))
print( quotesBrackets(squareBrackets(wrapBrackets("12345"), 3), 3))
