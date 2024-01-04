
def pgcdRecursive(a, b):
    """ Algorithme d'Euclide récursif pour trouver le PGCD 
        assertion: A > B """
    if b == 0:
        return a
    else:
        return pgcdRecursive(b, a % b)
    
def euclideEtendu(a, b):
    """ 
    Algorithme d'Euclide étendu, permettant de connaître:
    PGCD
    Coefficients de Bézout (u, v)
    Inverse modulaire de B modulo A ---> B * B^-1 mod A = 1 
    """
    modulo = b
    
    x = 0
    y = 1
    u = 1
    v = 0
    
    while a != 0:
        q = b // a
        r = b % a
        
        m = x - u * q
        n = y - v * q
        
        b = a
        a = r
        x = u
        y = v
        u = m
        v = n
    
    ' retourne (pgcd, u, v, inverse modulaire '
    return (b, x, y, x % modulo)

a = 26513
b = 32321

d, u, v, b_ = euclideEtendu(a, b)

print(u,v)