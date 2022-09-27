'''
    required : parameters neded by fuction x and y
    
    keyword : specifier la position du parametre  
    
    default : si en veut donner une valeur par defaut au parametre (x=0,y=0)
'''

def mysum(x,y):
    result = x+y
    return result

#######################################################

'''
    lambda est une fonction qui s ecri une seule ligne
'''
mysum2 = lambda x , y : x + y

print(mysum2(4,6))

###########################################

name = "chatoui"
age = 40
 

s=f" my name {name} and i m {age} years old"
print(s[-1])
s.upper()
s.lower()
s.title()
s.isupper()
s.islower()
s.istitle()
s.replace('c' , 'wwwww')
s.split('')# pour separer un chaine de caractere
