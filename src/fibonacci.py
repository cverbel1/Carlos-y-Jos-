n = int(input("Digite hasta que numero desea hacer la serie de fibonacci: "))
secuencia = []
a = 0
b = 1 
piv = 0
for i in range(n):
    secuencia.append(a)
    piv = a
    a = b
    b = piv + b
    
print(f"los primeros 10 numeros de fibonacci son")
print(secuencia)