#Check if 10 is bigger than 15 or not
print (10 > 15)

#If 10 is not bigger than15 print x is smaller than 15

if (10 > 15) == False :
    print("x is smaller than 15")
    
#In which cases we will use all

  

#What is the differences between all , and
# What is the differences between any , or
# If we need all the conditions to be true we will use ….  and

# What is the differences between if , elif

# What is the differences between elif else

# Can we use more than one elif  ----> yes

# Can we use more than one else  --- >  no

# write s simple ternary operator
x=4
print("x>5") if x>5 else  print ("x<5")
# in elif , python will check all the conditions no matter what ? until found the corret one

# in elif we use else for ... ?

''' if we have this list [2,4,6,8,10] :
        check to see if 4 in this list or not
        check to see if 4 and 6 in this list on not
        check to see if 3 or 6 in this list
        check to see if 2 , 4 and 5 in this list '''

li = [1,2,3,4,5]
if 4 in li :
    print ("4 ")
elif 4 and 6 in li :
    print("4 and 6")
elif 3 or 6 in li :
    print("3 or6")
elif 2 and 4 and 5 in li :
    print("2 and 4 and 5")
    