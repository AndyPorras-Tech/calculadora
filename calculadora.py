def suma (a,b):         print(suma(5,5))
    return a+b

def resta (a,b):        print(resta(10,3))
    return a-b

def division(a,b):      print(division(64,2))
    if b==0:
        raise ValueError("Division entre 0")
    return a/b