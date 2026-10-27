def suma (a,b):         
    return a+b

def resta (a,b):        
    return a-b

def division(a,b):     
    if b==0:
        raise ValueError("Division entre 0")
    return a/b

print(suma(5,5))
print(resta(10,3))
print(division(64,2))