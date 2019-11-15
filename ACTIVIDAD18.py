#EJERCICIO1
print("Ingresa un numero")
a=int(input())
print("Ingresa otro numero")
b=int(input())
if a>b:
    for x in range(b,a+1):
        print(x)
elif b>a:
    for x in range(a,b+1):
        print(x)
#EJERCICIO2
total=0
count=0
while total<=1000:
    num=int(input("Ingresa una cantidad para que sea sumada"))
    total=num+total
    count=count+1
print("Cantidad de numeros sumados",count)
print("Suma total de numeros", total)
#EJERCICIO3
print("Escribe un numero")
num=int(input())
if num%2==0:
    print("El numero es perfecto")
elif num%2!=0:
    print("El numero no es perfecto")
