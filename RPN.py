
#citim string-ul in forma infix

s = input()

#vom folosi o lista "stk" pentru a simula o stiva
#si o lista RPN in care vom avea la final expresia in forma poloneza postfixata

stk = []
RPN = []

def is_num( x ):
    if ord('9') >= ord(x) and ord(x) >= ord('0'): return True
    return False

def is_operator( x ):
    if x == '+' or x == '-' or x == '~' or x == '*': return True
    else: return False

def priority( x ):
    if x == '(': return 0
    if x == '+' or x == '-': return 1
    if x == '*': return 2
    if x == '~': return 3
    return 0

stk.append( '(' )
s = s + ')'

i = 0
while i < len(s):
    if is_num( s[i] ):
        var = 0
        while i < len(s) and is_num( s[i] ):
            var = var * 10 + ord( s[i] ) - ord( '0' )
            i += 1
        RPN.append( var )
        continue
    
    if s[i] == '(': 
        stk.append( s[i] )
    
    if is_operator( s[i] ):
        while len(stk) > 0 and priority( s[i] ) <= priority( stk[-1] ):
            RPN.append( stk[-1] )
            stk.pop()
        stk.append( s[i] )
    
    if s[i] == ')':
        while stk[-1] != '(':
            RPN.append( stk[-1] )
            stk.pop()
        stk.pop()
    i += 1

#afiseaza expresia RPN 
print( RPN )

#calculeaza valoarea expresiei

stk = []
for x in RPN:
    if is_operator( x ):
        if x == '~': 
            a = stk[-1]
            stk.pop()
            
            a *= -1
            stk.append(var)
        else:
            a = stk[-2]
            b = stk[-1]

            stk.pop()
            stk.pop()

            if x == '+': stk.append( a + b )
            if x == '-': stk.append( a - b )
            if x == '*': stk.append( a * b )
    else:
       stk.append( x )

print( stk[0] )