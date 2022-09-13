#Create a Boolean variable named x
x = True
#Create an integer variable named y
y=40
#Create a float variable named z
z = 5,6
#Create a string variable names s
s = "rabie"
#Convert the int variable to float
yy =  float(y)
print(type(yy))
#Can we convert the str to int ?
  # yes if it s numbers
  
tt = "5555"

ss =  int(tt)

print(type(ss))

#Create a list of numbers from 1 to 5
li = [1,2,3,4,5]

#Create a tuple from 10 to 15
tup = (10,11,12,13,14,15)

#Convert the list to tuple
tli = (1,2,3,4,5)
#Create a dict of 3 values
dic = {1 :"chatoui", 2 : "rabie", 3 : 39}

#Can we use semi colon ; with python
   
   # python dosen't use ;

#Python is interpreted or compiled ?   ---> INTERPRETED


#What is the differences between low level & high level
                 #LOW LEVEL : hard to be coded // hard to find errors // can be used only in one device
                 # high level : easy to program // les coding time // easy to corecte // run on any device
                 
#What is the differences between = , ==  :   = for assigning values to variables  //  == for comparison

# What do we mean by using !=   -----  is not equal 

#What is the operator precedence --- B= Bracket --E = Exponentiation --D = Division --M = Multiplication --A = Addition --S = Subtraction

#Create a variable x with value of 10

x = 10
 
#Increase x value by 15 using assignment operators
x += 15
 
print(x)

#Divide the x value by 5 using assignment operators
x/=5
print(x)

#Multiply the x value by 10 using assignment operator
x*=10

#Get module of x on 3 using assignment operators
x%=3
print(x)

#Using python print the module of 11 to 4
print(11%4)
#Print the exponent of 2,3
print ( 2**3 )
#Divide 11 by 3 using python division
res = 11 / 3
print(res)
#Can we divide 11 by 3 and get an integer number ?
res = 11 // 3
print(res)