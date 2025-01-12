a = float(input("enter value of a: "))
b = float(input("enter value of b: "))
bv = a if a>b else b
print("Biggest ({},{})={}".format(a,b,bv))