Dinter=0
Finter=0
for x in range(10):
    num = int(input("digite um núemro :"))
    if num >= 10 and num <=20:
        Dinter = Dinter + 1
    else:
        Finter = Finter + 1
print( f"a quantidade de número dentro {Dinter} do intervalo e fora do intervalo {Finter}")
