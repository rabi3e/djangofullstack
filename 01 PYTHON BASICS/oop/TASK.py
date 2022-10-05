from operator import truediv


cnd = True
liste = []
lpai =[]
limpai =[]
x = input("plz enter your LIST 'plz seperate by ,'")  
liste = (x.split(","))

print(liste)

for i in liste :
       if int(i)%2 == 0 :
           lpai.append(int(i))
       else :
           limpai.append(int(i))
           
print(lpai)
print(limpai)

