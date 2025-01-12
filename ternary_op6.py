val = float(input("Enter any value :"))
res = "Invalid Input , Don't Enter Zero or Negetive Values" if val <=0 else "Even" if val%2 == 0 else "odd"
print("{} is {}".format(val,res))



