a = float(input("enter value of a: "))
b = float(input("enter value of b: "))
res = a if a>b else b if b>a else "both are equal"
print("Big ({},{})={}".format(a,b,res))