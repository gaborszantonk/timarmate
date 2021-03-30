szoveg = input("Adj meg egy karkatersorozatot: ")
ujszoveg:str =""
for karakter in szoveg:
    if(karakter=="f"):
        ujszoveg+= "ph"
    else:
        ujszoveg +=karakter
print(ujszoveg)