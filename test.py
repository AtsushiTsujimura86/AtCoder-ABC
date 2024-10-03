userinput = input()
mydict = {char:i for i, char in enumerate(userinput)}
print(mydict)
print(mydict["a"])
print(mydict.get("a"))
for key in mydict.keys():
    print( key)
print(mydict.keys())