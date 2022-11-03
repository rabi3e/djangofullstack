#1 install num2world library
from num2words import num2words
x = int(input(" plz enter a numnber to convert ----> :"))
#select language
lang=  input("plz select uour language : fr, en, it, ar :------>")
print(num2words(x,lang=lang))


