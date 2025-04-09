resultado = 0
for x in range(5):
    num = int(input("digite um núemro :"))
    if num < 0:
        resultado = resultado + 1

print(f"a quantidade de números impar: {resultado}")
